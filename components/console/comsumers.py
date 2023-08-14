from utils.const import MONTH_LIST
from service.consumers import ConsumersService
from repository.log import ConsumerLog
from service.log import Log

def start_consumer():
    servie = ConsumersService()
    menu = [
         "",
        "----------------Потребители-------------------",
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
            Log().search_changes()
        
        if action == 2:
            [print(f"{number}. {month}") for number, month in enumerate(MONTH_LIST, 1)]
            month = int(input('Введите номер месяца: '))
            print("1. Бытовое потребление", '2. Комерческое потребление', "3. Общая", sep='\n')
            status = int(input("Выберите статус сводной ведомости: "))
            if status == 1:
                servie.collect_individual_svod(month)
            if status == 2:
                servie.collect_commerce_svod(month)
            if status == 3:
                servie.collect_total_svod(month)
        
        if action == 3:
            [print(f"{number}. {month}") for number, month in enumerate(MONTH_LIST, 1)]
            month = int(input('Введите номер месяца: '))
            print("1. Бытовое потребление", '2. Комерческое потребление', sep='\n')
            status = int(input("Выберите статус сводной ведомости: "))
            
            if status == 1:
                servie.create_individual_statement(month)
            if status == 2:
                servie.create_commerce_statement(month)
        break