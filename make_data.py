import openpyxl
import os


class DataFromTable:

    def __init__(self):
        self.wb = openpyxl.load_workbook('src/data.xlsx')
        self.sheet = self.wb['Лист1']

    def get_value(self, index):
        return self.sheet[f'A{index}'].value


class File:

    def __init__(self):
        if os.path.exists("src/credit.txt"):
            os.remove("src/credit.txt")

    @staticmethod
    def write_in_file(summ, pay):
        with open('src/credit.txt', 'a') as f:
            f.write(f'Сумма кредита: {summ}, ежемесячный платеж: {pay}\n')