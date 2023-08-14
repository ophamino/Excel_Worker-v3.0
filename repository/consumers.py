from typing import Dict, Any

from .base import ExcelRepository
from utils.excel import open_excel
from utils.base import get_main_dir


class ComsumerRepository(ExcelRepository):
    id_col = 3
    skip_rows = 6
    keys = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD",
        "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ"
    ]
    directory = get_main_dir()
    
    def get_total_svod_data(self, month: str) -> Dict[str, Dict[str, Any]]:
        """
        Функция для полученния всех данных о потребителях: коммерчсеких и бытовых

        Args:
            month (int): Месяц за который нужно получить данные

        Returns:
            Dict[str, Dict[str, Any]]: _description_
        """
        path = f"{self.directory}\Сводный баланс энергопотребления\Сводный баланс 2023\Сводная ведомость потребителей"
        individual = self.serialize_all_data(f"{path}\РВ Потребителей {month}\РВ Бытовых потребителей") 
        commerce = self.serialize_all_data(f"{path}\РВ Потребителей {month}\РВ Коммерческих потребителей")
        data = individual | commerce
        
        return data

    def get_file_by_status(self, status: str):
        if status == "cc":
            return "Сводная ведомость Коммерческих потребителей.xlsx"
        if status == "ch":
            return "Сводная ведомость Бытовых потребителей.xlsx"
    
    def serialize_register(self, status: str) -> Dict[str, Dict[str, Any]]:
        """
        Функция для сериализации данных реестра Потребителей, необходимых для формирования новых рачетных ведомостей
            
        Returns:
            Dict[str, Dict[str, Any]]: Необходимые данные
        """
        path = f"{self.directory}\Реестровая база данных\Реестр потребителей\Реестр потребителей.xlsx"
        file = open_excel(path)
        sheet = file.worksheets[0]
        data = {}
        
        for row in range(9, sheet.max_row +1):
            if sheet.cell(row, 55).value == "Активен" and sheet.cell(row, 2).value == status:
                data[sheet.cell(row, 4).value] = {
                    "A": 1, "B": sheet.cell(row, 3).value, "C": sheet.cell(row, 4).value, "D": sheet.cell(row, 5).value, "E": sheet.cell(row, 6).value,
                    "F": str(sheet.cell(row, 7).value), "G": sheet.cell(row, 8).value,"H": sheet.cell(row, 9).value, "I": sheet.cell(row, 12).value,
                    "J": sheet.cell(row, 13).value, "K": sheet.cell(row, 14).value, "L": sheet.cell(row, 20).value, "M": sheet.cell(row, 21).value,
                    "N": sheet.cell(row, 22).value, "O": sheet.cell(row, 23).value, "P": sheet.cell(row, 24).value, "Q": sheet.cell(row, 27).value,
                    "R": sheet.cell(row, 28).value, "S": str(sheet.cell(row, 29).value), "T": sheet.cell(row, 30).value, "AM": sheet.cell(row, 54).value,
                    "Z": sheet.cell(row, 53).value, "AD": sheet.cell(row, 26).value,  "AI": sheet.cell(row, 35).value, "AJ": sheet.cell(row, 36).value, "AO": "",
                    "AK": sheet.cell(row, 37).value, "AL": sheet.cell(row, 52).value,
                }
        
        return data
    
    def serialize_svod(self, month: str, status: str) -> Dict[str, Dict[str, Any]]:
        """
        Функция для сериализации данных Сводной ведомости Потребителей, необходимых для формирования новых рачетных ведомостей

        Args:
            path (str): Путь к сводной ведомости
            month (str): Название месяца, за который нужно сериализовать данные

        Returns:
            Dict[str, Dict[str, Any]]: Необходимые данные
        """
        file = self.get_file_by_status(status)
        path = f"{self.directory}\Сводный баланс энергопотребления\Сводный баланс 2023\Сводная ведомость потребителей\{file}"
        file = open_excel(path)
        sheet = file[month]
        data = {}
        
        for row in range(self.skip_rows, sheet.max_row + 1):
            data[sheet.cell(row, self.id_col).value] = {
                "U": sheet.cell(row, 22).value, "V": "", "W": "", "X": "", "Y": "",
                "AA": "", "AB": "", "AC": "", "AE": "",  "AF": "", "AG": "", "AH": "", "AN": "", "AO": "",
                "AP": sheet.cell(row, 40).value, "AQ": sheet.cell(row, 41).value,
            }
        
        return data

    def get_statment(self, month: str, status: str):
        registry = self.serialize_register(status)
        svod = self.serialize_svod(month, status)
        data = {}
        
        for key in registry.keys():
            if key in svod.keys():
                data[key] = svod[key] | registry[key]
            if key not in svod.keys():
                empty_list = ["U", "V", "W", "X", "Y", "AA", "AB", "AC", "AE",  "AF", "AG", "AH", "AN", "AO", "AP", "AQ"]
                data[key] = {key: "" for key in empty_list} | registry[key]
        
        return data