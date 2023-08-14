from typing import Optional, Dict, Any, List
from repository.base import ExcelRepository
from utils.excel import open_excel
from utils.base import resource_path, get_main_dir
from datetime import datetime
import os
import logging


class LogRepository(ExcelRepository):
    change_path: Optional[str] = None
    static_path: Optional[str] = None
    upload_to: Optional[str] = None
    column_count: Optional[int] = 0
    directory = get_main_dir()
    
    def serialaze_data(self, path: str)-> Dict[str,  Dict[str, Any]]:
        data = {}
        file = open_excel(path)
        sheet = file.worksheets[0]
        
        for row in range(self.skip_rows, sheet.max_row + 1):
            data[sheet.cell(row=row, column=4).value] = {
                "values": [sheet.cell(row=row, column=col).value for col in range(1, self.column_count)],
                "coordinate": [sheet.cell(row=row, column=col).coordinate for col in range(1, self.column_count)]
            }
        return data

    
    def  collect_changes(self) -> List:
        data = []
        changes = self.serialaze_data(self.change_path)
        static = self.serialaze_data(self.static_path)
        
        for key in changes.keys():
            if key not in static.keys():
                data.append([1, key, "", "", "", "", "Добавлено", datetime.now().date(), datetime.now().time()])
                data.append(changes[key])
            
            if key in static.keys():
                new_values = static[key]["values"]
                old_values = changes[key]["values"]
                if new_values != old_values:
                    for index in range(len((new_values))):
                        if new_values[index] != old_values[index]:
                            coordinate = changes[key]["coordinate"][index]
                            data.append([1, key, "", coordinate, old_values[index], new_values[index], "Изменено", datetime.now().date(), datetime.now().time()])
                static.pop(key)
            
            if static.keys():
                for key in static.keys():
                    data.append([1, key, "", "", "", "", "Удалено", datetime.now().date(), datetime.now().time()])
                    data.append(static[key])
        return data
    
    def insert_changes(self):
        data = self.collect_changes()
        path = path = self.upload_to
        if not os.path.exists(path):
            file = open_excel('template/Журнал изменений.xlsx')
            file.save(path)
        file = open_excel(path)
        sheet = file[str(datetime.now().year)]
        
        for row in data:
            if (not row[4]) and (not row[5]) and (row[6] == "Изменено"):
                continue
            sheet.append(row)
        
        file.save(path)

    def search_changes(self):
        self.insert_changes()
        file = open_excel(self.change_path)
        file.save(self.static_path)
        

class BicuLog(LogRepository):
    skip_rows = 5
    directory = get_main_dir()
    changs_path = f"{directory}/Реестровая база данных/Реестр БИКУ/Реестр БИКУ.xlsx"
    static_path = "./template/Реестр БИКУ для сравнения.xlsx"
    col_id = 3
    column_count = 47
    upload_to = f"{directory}/Реестровая база данных/Реестр БИКУ/Журнал изменений.xlsx"
    
    def search_changes(self):
        logging.info("Обновлен журнал изменений БИКУ")
        return super().search_changes()


class ConsumerLog(LogRepository):
    skip_rows = 9
    directory = get_main_dir()
    change_path = f"{directory}\Реестровая база данных\Реестр потребителей\Реестр потребителей.xlsx"
    static_path = "template\Реестр потребителей для сравнения.xlsx"
    upload_to = f"{directory}\Реестровая база данных\Реестр потребителей\Журнал изменений.xlsx"
    col_id = 4
    column_count = 55

    def search_changes(self):
        logging.info("Обновлен журнал изменений потребителей")
        return super().search_changes()
