from typing import Dict, Any

from .base import ExcelRepository
from src.utils.excel import open_excel
from src.utils.base import get_main_dir


class BicuReposiitory(ExcelRepository):
    
    directory = get_main_dir()
    skip_rows = 8
    id_col = 3
    keys = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z", "AA", "AB"
    ]

    def collect_svod(self, month: str) -> Dict[str, Dict[str, Any]]:
        """
        Фуекция для получения данных сводной ведомости

        Args:
            month (str): Название месяца

        Returns:
            Dict[str, Dict[str, Any]]: Все данные с рачетных ведомостей
        """
        path = (f"{self.directory}\Сводный баланс энергопотребления\Сводный баланс 2023\Сводная ведомость БИКУ\РВ БИКУ {month}")
        data = self.serialize_all_data(path)
        return data
    
    def serialize_register(self) -> Dict[str, Dict[str, Any]]:
        """
        Функция для сериализации данных реестра БИКУ, необходимых для формирования новых рачетных ведомостей
            
        Returns:
            Dict[str, Dict[str, Any]]: Необходимые данные
        """
        path = f"{self.directory}\Реестровая база данных\Реестр БИКУ\Реестр БИКУ.xlsx"
        file = open_excel(path)
        sheet = file.worksheets[0]
        data = {}
        
        for row in range(5, sheet.max_row +1):
            if sheet.cell(row, 47).value == "Активен":
                data[sheet.cell(row, 3).value] = {
                    "A": 1, "B": sheet.cell(row, 2).value, "C": sheet.cell(row, 3).value, "D": sheet.cell(row, 4).value, "E": sheet.cell(row, 5).value,
                    "F": str(sheet.cell(row, 8).value), "G": sheet.cell(row, 9).value, "H": sheet.cell(row, 10).value, "I": sheet.cell(row, 13).value,
                    "J": sheet.cell(row, 14).value, "K": sheet.cell(row, 15).value, "L": sheet.cell(row, 20).value, "M": sheet.cell(row, 21).value,
                    "N": sheet.cell(row, 22).value, "O": sheet.cell(row, 23).value, "U": sheet.cell(row, 46).value, "X": sheet.cell(row, 27).value,
                    "Y": sheet.cell(row, 28).value, "Z": sheet.cell(row, 29).value, "AA": sheet.cell(row, 32).value, "AB": sheet.cell(row, 45).value,
                }
        
        return data
    
    def serialize_svod(self, month: str) -> Dict[str, Dict[str, Any]]:
        """
        Функция для сериализации данных Сводной ведомости БИКУ, необходимых для формирования новых рачетных ведомостей

        Args:
            path (str): Путь к сводной ведомости
            month (str): Название месяца, за который нужно сериализовать данные

        Returns:
            Dict[str, Dict[str, Any]]: Необходимые данные
        """
        path = f"{self.directory}\Сводный баланс энергопотребления\Сводный баланс 2023\Сводная ведомость БИКУ\Сводная ведомость БИКУ.xlsx"
        file = open_excel(path)
        sheet = file[month]
        data = {}
        
        for row in range(6, sheet.max_row + 1):
            data[sheet.cell(row, 3).value] = {
                "P": sheet.cell(row, 17).value, "Q": "", "R": "", "S": "", "T": "", "V": "", "W": "",
            }
        
        return data
    
    def get_new_statement(self, month: str) -> Dict[str, Dict[str, Any]]:
        """
        Функция для объединения необходимых данных для формирования новых расчетных ведомостей

        Args:
            month (int): Номер месяца

        Returns:
            Dict[str, Dict[str, Any]]: Общие необходимые данные
        """
        registry = self.serialize_register()
        svod = self.serialize_svod(month)
        data = {}
        
        for key in registry.keys():
            if key in svod.keys():
                data[key] = svod[key] | registry[key]
            if key not in svod.keys():
                data[key] = {"P": "", "Q": "", "R": "", "S": "", "T": "", "V": "", "W": ""} | registry[key]
        
        return data
