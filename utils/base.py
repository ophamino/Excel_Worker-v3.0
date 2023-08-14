import os
import sys
import json


def resource_path(relative_path: str) -> str:
    """
    Функция для получения абсолютного путь к ресурсу из относительного

    Args:
        relative_path (str): Относительный путь

    Returns:
        str: Абсолютный путь
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_main_dir() -> str:
    """
    Функция для получения названия главной директориии

    Returns:
        str: Название главной директории
    """
    with open ("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)
    return settings["main_directory"]


def clean_directory(path: str) -> None:
    """Функуция для очистки директории

    Args:
        path (str): Путь к директории
    """
    files = os.listdir(path)
    for file in files:
        os.remove(f"{path}\{file}")
