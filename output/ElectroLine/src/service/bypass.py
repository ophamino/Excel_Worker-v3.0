from openpyxl import load_workbook
from src.repository.bypass import BypassRepository



class BypassService:
    
    def __init__(self) -> None:
        self.repo = BypassRepository()
    
    def create_clear_bypass(self, month: str) -> None:
        book = load_workbook(".\\src\\template\\accouting.xlsx")
        sheet = book.worksheets[0]
        individual_bypass_id = self.repo.get_bypass_id(month)
        bypass_data: dict = self.repo.serializeCommerce() | self.repo.serializeIndividual(individual_bypass_id)
        [sheet.append(row) for row in bypass_data.values()]
        book.save("../Обхожной лист.xlsx")
        
    def download_bypass(self, month: str) -> None:
        pass