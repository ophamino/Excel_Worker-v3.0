import os
from datetime import datetime
from typing import Dict, Union
from abc import ABC, abstractmethod

from openpyxl import load_workbook


MONTH_LIST = [
    "Январь", "Февраль", "Март",
    "Апрель", "Май", "Июнь",
    "Июль", "Август", 'Сентябрь',
    'Октябрь', 'Ноябрь', 'Декабрь'
]


class AccrualsRepository(ABC):

    @abstractmethod
    def getEmptyID():
        raise NotImplementedError

    @abstractmethod
    def getExpensesSvod():
        raise NotImplementedError


class AccrualsCommerceRepository(AccrualsRepository):
    """
    Класс для начисления показаний для коммерческих потребителей
    """
    

    def getExpensesBicu(self, month: str) -> Dict[str, Dict[str, int]]:
        path = "..\\Dagenergy\\Сводный баланс энергопотребления\\Сводный баланс 2023\\Сводная ведомость БИКУ\\Сводная ведомость БИКУ.xlsx"
        file = load_workbook(path, data_only=True)
        sheet = file[month]
        data = {}
        
        for row in range(8, sheet.max_row + 1):
            index = sheet.cell(row, 3).value
            if index[6:8] == "MC":
                data[sheet.cell(row, 3).value] = {
                    "value": sheet.cell(row, 18).value
                }
        return data


    def getEmptyID(self, month) -> Dict[str, Dict[str, Union[str, int]]]:

        path = "..\\Dagenergy\\Сводный баланс энергопотребления\\Сводный баланс 2023\\Сводная ведомость потребителей\\Сводная ведомость Коммерческих потребителей.xlsx"
        file = load_workbook(path, data_only=True)
        sheet = file[month]
        data = {}
        
        for row in range(6, sheet.max_row + 1):
            if not sheet.cell(row, 23).value:
                data[sheet.cell(row, 3).value] = {
                    "value": 0,
                    "index": sheet.cell(row, 23).value if len(sheet.cell(row, 39).value) > 6 and  sheet.cell(row, 39).value[6:8] == "MC" else None,
                }
        return data
    
    def getExpensesSvod(self, path: str, month: str) ->  Dict[str, Dict[str, int]]:
        # path = "..\\Dagenergy\\Сводный баланс энергопотребления\\Сводный баланс 2023\\Сводная ведомость потребителей\\Сводная ведомость Коммерческих потребителей.xlsx"
        file = load_workbook(path, data_only=True)
        sheet = file[month]
        data = {}
        
        for row in range(6, sheet.max_row + 1):
            if sheet.cell(row, 21).value:
                data[sheet.cell(row, 3).value] = {
                    "value": int(sheet.cell(row, 22).value) - int(sheet.cell(row, 21).value if sheet.cell(row, 21).value else 0)
                }
        return data
    


class AccrualsInividualRepository(AccrualsRepository):
    pass


class AccrualsService:
    pass


class AccrualsCommerceService(AccrualsService):
    
    repo = AccrualsCommerceRepository()
    
    def checkPreviousYear(self, empty_data: Dict[str, Dict[str, Union[str, int]]], month: str):
        year = datetime.now().year - 1
        path = f"..\\Dagenergy\\Сводный баланс энергопотребления\\Сводный баланс {year}\\Сводная ведомость потребителей\\Сводная ведомость Коммерческих потребителей.xlsx"
        data = self.repo.getExpensesSvod(path, month)

        if not os.path.exists(path):
            return

        for item in empty_data.keys():
            if item in data.keys():
                empty_data[item]["value"] += data[item]["value"]

        return data
    
    
    def check_nearest_month(self, empty_data: Dict[str, Dict[str, Union[str, int]]],  month: str):
        month =  MONTH_LIST.index(month)
        year = datetime.now().year
        path = f"..\\Dagenergy\\Сводный баланс энергопотребления\\Сводный баланс {year}\\Сводная ведомость потребителей\\Сводная ведомость Коммерческих потребителей.xlsx"
        file = load_workbook(path)

        
        for month in reversed(MONTH_LIST[ :month]):
            if not empty_data:
                break
            sheet = file[month]
            for row in range(6, sheet.max_row + 1):
                key = sheet.cell(row, 3).value
                expenses = sheet.cell(row, 23).value
                if key and expenses:
                    empty_data[]
            
            


class AccrualsIndividualService(AccrualsService):
    pass
