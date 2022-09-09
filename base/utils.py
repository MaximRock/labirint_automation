import re
from typing import List, Any

from selenium.webdriver.remote.webelement import WebElement


class Utils:

    @staticmethod
    def get_join_string(lst_string: List[str]) -> str:
        return ", ".join(lst_string)
