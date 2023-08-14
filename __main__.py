import logging
from components import start_consumer, start_analytics, start_balance, start_bicu

def main():
    print()
    print("Welcome!")
    main_action = [
        "",
        "----------------Меню---------------------------",
        "Выберите действие, которое хотите совершить: ",
        "1. Потребители",
        "2. БИКУ",
        "3. Сформировать сводный баланс",
        "4. Сформировать аналитику"
        "________________________________________________"
        ""
    ]
    while True:
        print(*main_action, sep='\n')
        action = int(input("Выберите порядковый номер действия: "))
        if action == 1:
            start_consumer()
        if action == 2:
            start_bicu()
        if action == 3:
            start_balance()
        if action == 4:
            start_analytics()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="log.log", filemode="a", encoding="utf-8", format="[%(levelname)s] %(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    main()
