import os
from typing import Dict, Union
from abc import ABC, abstractmethod

from openpyxl import load_workbook


class AccrualsRepository(ABC):
    def __init__(self, month: str) -> None:
        self.month = month

    @abstractmethod
    def getEmptyID():
        raise NotImplementedError

    @abstractmethod
    def getExpensesSvod():
        raise NotImplementedError


class AccrualsCommerceRepository(AccrualsRepository):
    """
    Класс для 
    """
    

    def getExpensesBicu(self) -> Dict[str, Dict[str, int]]:
        path = "..\\Dagenergy\\Сводный баланс энергопотребления\\Сводный баланс 2023\\Сводная ведомость БИКУ\\Сводная ведомость БИКУ.xlsx"
        file = load_workbook(path, data_only=True)
        sheet = file[self.month]
        data = {}
        
        for row in range(8, sheet.max_row + 1):
            index = sheet.cell(row, 3).value
            if index[6:8] == "MC":
                data[sheet.cell(row, 3).value] = {
                    "value": sheet.cell(row, 18).value
                }
        return data


    def getEmptyID(self) -> Dict[str, Dict[str, Union[str, int] ]]:

        path = "..\\Dagenergy\\Сводный баланс энергопотребления\\Сводный баланс 2023\\Сводная ведомость потребителей\\Сводная ведомость Коммерческих потребителей.xlsx"
        file = load_workbook(path, data_only=True)
        sheet = file[self.month]
        data = {}
        
        for row in range(6, sheet.max_row + 1):
            if not sheet.cell(row, 23).value:
                data[sheet.cell(row, 3).value] = {
                    "value": 0,
                    "index": sheet.cell(row, 23).value if len(sheet.cell(row, 39).value) > 6 and  sheet.cell(row, 39).value[6:8] == "MC" else None,
                }
        return data
    
    def getExpensesSvod(self) ->  Dict[str, Dict[str, int]]:
        path = "..\\Dagenergy\\Сводный баланс энергопотребления\\Сводный баланс 2023\\Сводная ведомость потребителей\\Сводная ведомость Коммерческих потребителей.xlsx"
        file = load_workbook(path, data_only=True)
        sheet = file[self.month]
        data = {}
        
        for row in range(6, sheet.max_row + 1):
            if sheet.cell(row, 21).value:
                data[sheet.cell(row, 3).value] = {
                    "value": int(sheet.cell(row, 22).value) - int(sheet.cell(row, 21).value if sheet.cell(row, 21).value else 0)
                }
        return data
    


class AccrualsInividualRepository(AccrualsRepository):
    pass


test = AccrualsCommerceRepository("Июнь").getExpensesSvod()
print(test)
