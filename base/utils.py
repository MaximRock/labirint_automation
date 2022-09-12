import re
from typing import List, Any

from selenium.webdriver.remote.webelement import WebElement


class Utils:

    @staticmethod
    def get_join_string(lst_string: List[str]) -> str:
        """Преобразование списка в строку list in string"""
        return ", ".join(lst_string)

    @staticmethod
    def get_list_creation() -> list:
        lst = list()
        return lst

