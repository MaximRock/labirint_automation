from typing import List


class Utils:

    @staticmethod
    def get_join_string(lst_string: List[str]) -> str:
        """Преобразование списка в строку list in string"""
        return ", ".join(lst_string)

    @staticmethod
    def get_list_creation(lst=None) -> list:
        """
        Создание списка
        :param lst: неопределен
        :return: list
        """
        if lst is None:
            lst = []
        return lst
