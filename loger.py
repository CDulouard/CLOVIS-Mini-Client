import os
import pandas as pd
import re


class loger:

    def __init__(self):  # Notre méthode constructeur
        self.stack = pd.DataFrame({'log': [1]})
        TestNum = 0
        self.CsvName = "test0.csv"

        name_check = False
        turn = 0
        sortir = 0
        while not name_check:
            for i in os.listdir('./' + '.'):
                print(i)
                if re.match(r"test[0-9]*.csv$", i) is not None and turn == 0:
                    TestNum += 1
                elif re.match("test" + str(TestNum) + ".csv", i) is not None and turn > 0:
                    TestNum += 1
                    sortir += 1
                elif sortir == 0 and turn > 0:
                    name_check = True
            sortir = 0
            turn += 1
        self.CsvName = "test" + str(TestNum) + ".csv"
        self.stack.to_csv(self.CsvName, index=False, header=True)
        self.loggsave = pd.DataFrame()
        self.stack = pd.DataFrame()

    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.stack = pd.DataFrame()

    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "{}".format(self.stack)

    def archive(self):
        print("lol")
        if len(pd.read_csv(self.CsvName)) == 1:
            self.stack.to_csv(self.CsvName, index=False, header=True)
            self.effacer()
        else:
            self.loggsave = pd.read_csv(self.CsvName)
            self.loggsave = pd.concat([self.loggsave, self.stack])
            self.loggsave.to_csv(self.CsvName, index=False, header=True)
            self.effacer()

    def __add__(self, liste_a_ajouter):
        """L'objet à ajouter est une liste"""
        self.stackADD = pd.DataFrame({'log': [liste_a_ajouter]})
        self.stack = pd.concat([self.stack, self.stackADD])
        if len(self.stack) >= 10:
            self.archive()
        print(len(self.stack))
