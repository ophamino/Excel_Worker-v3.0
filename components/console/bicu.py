from utils.const import MONTH_LIST
from service.bicu import BicuService
from service.log import BicuLog


def start_bicu():
    service = BicuService()
    menu = [
        "",
        "---------------------БИКУ----------------------",
        "Выберите действие, которое хотите совершить: ",
        "1. Сверить статические данные",
        "2. Сформировать сводную ведомость",
        "3. Сформировать расчетную ведомость",
        "0. Главное меню",
        "________________________________________________",
        ""
    ]
    print(*menu, sep='\n')
    action = int(input("Выберите порядковый номер действия: " ))
    while True:
        if action == 0:
            break
        
        if action == 1:
            BicuLog().search_changes()
        
        if action == 2:
            [print(f"{number}. {month}") for number, month in enumerate(MONTH_LIST, 1)]
            month = int(input('Введите номер месяца: '))
            service.collect_data_in_svod(month)
        
        if action == 3:
            [print(f"{number}. {month}") for number, month in enumerate(MONTH_LIST, 1)]
            month = int(input('Введите номер месяца: '))
            service.create_new_statement(month)
        break
