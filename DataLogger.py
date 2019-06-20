import pandas as pd
from typing import List, Optional
import datetime
import os
from threading import Thread, RLock
import time


class DataLogger(Thread):

    def __init__(self, stack_size: Optional[int] = 1000, columns: Optional[List[str]] = [],
                 file_identifier: Optional[str] = "Log",
                 path: Optional[str] = "Logs/", file_size: Optional[int] = 100_000,
                 delay_save: Optional[int] = 60) -> None:
        """
        Creat a new DataLogger
        :param stack_size:
        The maximal size of the stack, if the length of the stack is greater or equal to this value the stack will be
        saved in a csv file and then it will be cleared.
        :param columns:
        The names of the columns of the stack
        :param file_identifier:
        The name of the save file
        :param path:
        The path to the directory containing the saved files
        :param file_size:
        The max size of the save file, if the length of the stack + the length of the file is greater than this number,
        the DataLogger will creat a new file.
        """
        Thread.__init__(self)
        self.stack = pd.DataFrame(columns=columns)
        self.stack_size = stack_size
        self.file_identifier = file_identifier
        self.n_file = 1

        self.path = path
        self.file_size = file_size
        self.last_save = time.time()
        self.delay_save = delay_save
        self.is_running = False
        self.date = datetime.datetime.now()
        self.start()

    def __repr__(self):
        return "{}".format(self.stack)

    def add(self, new_lines: pd.DataFrame) -> None:
        """
        Add a DataFrame to the stack if its dimensions are correct
        :param new_lines:
        The DataFrame we want to add.
        :return:
        None
        """
        if new_lines.ndim == self.stack.ndim:
            if new_lines.shape[1] == self.stack.shape[1]:
                new_lines.columns = self.stack.keys()
                self.stack = pd.concat([self.stack, new_lines])
        if len(self.stack) >= self.stack_size:
            self.save_stack()

    def clear_stack(self) -> None:
        """
        Clear the stack
        :return:
        None
        """
        self.stack.drop(self.stack.index[:], inplace=True)

    def save_stack(self):
        """
        Save the stack in the save file and clear the stack.
        Creat new file if it is needed
        :return:
        None
        """
        saver = self.SaveMachine(self.path, self.file_identifier, self.file_size, self.date, self.stack)
        saver.start()
        saver.join()
        self.clear_stack()
        self.last_save = time.time()

    def change_columns(self, new_columns: List[str]) -> None:
        """
        If the lenght of the input is equal to the number of columns of the stack, change the names of the columns.
        If it is not equal, it the actual stack is replaced by an empty stack with the new columns name.
        :param new_columns:
        The list of new columns name
        :return:
        None
        """
        if len(new_columns) == self.stack.shape[1]:
            self.stack.columns = new_columns
        else:
            self.stack = pd.DataFrame(columns=new_columns)

    def periodic_save(self) -> None:
        """
        Save the stack when the difference between the actual time and the last save is greater than
        self.last_save
        :return:
        None
        """
        while self.is_running:
            if time.time() - self.last_save >= self.delay_save:
                self.save_stack()
            time.sleep(0.1)

    def run(self) -> None:
        """
        Run the Thread that save the stack if it haven't been saved for a time greater
        than self.delay_save
        :return:
        None
        """
        self.is_running = True
        self.periodic_save()

    def stop(self) -> None:
        """
        Save the stack and stop the Logger
        :return:
        None
        """
        self.save_stack()
        self.is_running = False

    class SaveMachine(Thread):

        def __init__(self, path: str, file_identifier: str, file_size: int, date: datetime.datetime,
                     stack: pd.DataFrame) -> None:
            """
            Creat a new Thread to save the stack without slowing down the program
            :param path:
            The path to the directory containing the saved files
            :param file_identifier:
            The name of the save file
            :param file_size:
            The max size of the save file, if the length of the stack + the length of the file is greater than this number,
            the DataLogger will creat a new file.
            :param date:
            The date of the Logger's start
            :param stack:
            The stack we want to save
            """
            Thread.__init__(self)
            self.date = date
            self.path = path
            self.file_identifier = file_identifier
            self.file_size = file_size
            self.n_file = 1
            self.file_name = ""
            self.new_file_name()
            self.stack = stack

        def run(self) -> None:
            """
            Start the Thread and save the stack
            :return:
            """
            self.save_stack()

        def save_stack(self):
            """
            Save the stack in the save file and clear the stack.
            Creat new file if it is needed
            :return:
            None
            """
            with RLock():
                if self.stack.shape[0] > 0:
                    if os.path.exists(self.path + self.file_name):
                        temp = pd.read_csv(self.path + self.file_name)
                        if temp.shape[1] + self.stack.shape[1] <= self.file_size:
                            temp = pd.concat([temp, self.stack])
                            temp.to_csv(self.path + self.file_name, index=False)
                        else:
                            self.n_file += 1
                            self.new_file_name()
                            self.stack.to_csv(self.path + self.file_name, index=False)

                    else:
                        self.stack.to_csv(self.path + self.file_name, index=False)

        def new_file_name(self) -> None:
            """
            Creat a new file name based on the name we want for the file, the date of creation of the DataLogger and the
            number of file already created by the DataLogger
            :return:
            None
            """
            date = self.date
            self.file_name = self.file_identifier + "_" + str(date.year) + "_" + str(date.month) + "_" + str(
                date.day) + "_" + str(
                date.hour) + ":" + str(date.minute) + ":" + str(date.second) + "_file_" + str(self.n_file) + ".csv"
