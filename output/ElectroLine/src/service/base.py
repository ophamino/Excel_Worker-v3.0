from typing import Dict, Any

from openpyxl.worksheet.worksheet import Worksheet

from src.utils.base import get_main_dir


class BaseService:
    """
    Базовый класс всех сервисоов
    """
    directory = get_main_dir()
    
    def insert_data(self, sheet: Worksheet, data: Dict[str, Dict[str, Any]]) -> None:
        """
        Функция для вставки данных в документ Excel

        Args:
            sheet (Worksheet): Лиcт Excel
            data (Dict[str, Dict[str, Any]]): Данные
        """
        for row in data.values():
            sheet.append([row[key] for key in self.repository.keys])
            
    def insert_data_by_departament(self, sheet: Worksheet, data: Dict[str, Dict[str, Any]], departament_id: str):
        """
        Функция для вставки данных по отделениям в документ Excel
        Args:
            sheet (Worksheet): Лиcт Excel
            data (Dict[str, Dict[str, Any]]): Данные
            departament_id (str): ID отделения
        """
        for key, values in data.items():
                if key[2:4] == departament_id:
                    sheet.append([values[key] for key in self.repository.keys])
