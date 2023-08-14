from utils.const import MONTH_LIST
from service.analytics import BalanceAnalitic

def start_analytics():
    [print(f"{number}. {month}") for number, month in enumerate(MONTH_LIST, 1)]
    month = int(input('Введите номер месяца: '))
    BalanceAnalitic().create_analytics(month)