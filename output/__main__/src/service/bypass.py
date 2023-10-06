import os

from openpyxl import load_workbook
from src.repository.bypass import BypassRepository
from src.utils.const import MAIN_DIR


class BypassService:
    
    def __init__(self) -> None:
        self.repo = BypassRepository()
    
    def create_clear_bypass(self, month: str) -> None:
        book = load_workbook(os.path.join("src", "template", "accouting.xlsx"))
        sheet = book.worksheets[0]
        individual_bypass_id = self.repo.get_bypass_id(month)
        bypass_data: dict = self.repo.serializeCommerce() | self.repo.serializeIndividual(individual_bypass_id)
        [sheet.append(row) for row in bypass_data.values()]
        book.save(os.path.join(MAIN_DIR, "Шаблоны расчетных ведомостей", "Обходной лист", "Обходной лист.xlsx"))
        
    def download_bypass(self, month: str) -> None:
        pass