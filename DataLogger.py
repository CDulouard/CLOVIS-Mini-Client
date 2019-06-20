import pandas as pd
from typing import List, Optional
import datetime
import os
import re


class DataLogger:

    def __init__(self, stack_size: Optional[int] = 1000, columns: Optional[List[str]] = [], file_name: Optional[str] = "Log",
                 path: Optional[str] = "Logs/", file_size: Optional[int] = 100_000) -> None:
        """
        Creat a new DataLogger
        :param stack_size:
        The maximal size of the stack, if the length of the stack is greater or equal to this value the stack will be
        saved in a csv file and then it will be cleared.
        :param columns:
        The names of the columns of the stack
        :param file_name:
        The name of the save file
        :param path:
        The path to the save file
        :param file_size:
        The max size of the save file, if the length of the stack + the length of the file is greater than this number,
        the DataLogger will creat a new file.
        """
        self.stack = pd.DataFrame(columns=columns)
        self.stack_size = stack_size
        self.file_identifier = file_name
        self.n_file = 1
        self.file_name = ""
        self.new_file_name()
        self.path = path
        self.file_size = file_size

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

    def new_file_name(self) -> None:
        """
        Creat a new file name based on the name we want for the file, the date of creation of the DataLogger and the
        number of file already created by the DataLogger
        :return:
        None
        """
        date = datetime.datetime.now()
        self.file_name = self.file_identifier + "_" + str(date.year) + "_" + str(date.month) + "_" + str(date.day) + "_" + str(
            date.hour) + ":" + str(date.minute) + ":" + str(date.second) + "_file_" + str(self.n_file) + ".csv"

    def save_stack(self):
        """
        Save the stack in the save file and clear the stack.
        Creat new file if it is needed
        :return:
        None
        """
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
        self.clear_stack()

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


