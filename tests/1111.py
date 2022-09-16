import re

import pytest

# @pytest.mark.parametrize('number', [1, 2, 100, -2, -4])
# def test_add(number):
#     assert number > 0

# class HomePageNavHeaderPersonal(SeleniumBase):
#
#     def __init__(self, driver):
#         SeleniumBase.__init__(driver)
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 15, 0.3)
#         self.__nav_link_my_maze: str = 'div>ul>li>a[class*=js-b-autofade-wrap]'
#         self.__header_personal_elements: str = "//ul[contains(@class, 'b-header-b-personal-e-list ul-justify')]/li[position() > 2]"
#         self.__dropdown_menu_my_maze: str = 'ul[class=user-top-menu]>li'
#         self.__orders: str = "//span[contains(text(),'Заказы')]"
#         self.__browsing_history: str = "//span[contains(text(),'История просмотра')]"
#         self.__deferred: str = "//span[contains(text(),'Отложенные')]"
#         self.__balance: str = "//span[contains(text(),'Баланс')]"
#         self.__settings: str = "//span[contains(text(),'Мои данные')]"
#         self.__full_access_to_labyrinth: str = "//span[contains(text(),'Авторизоваться в личном кабинете')]"
#         self.__basket: str = "//a[contains(text(),'Моя корзина')]"

# lst_search_book = [x.text for x in search_field.get_name_of_the_book()]
#
#     def get_nav_link_my_maze(self) -> WebElement:
#         return self.is_visible('css', self.__nav_link_my_maze, 'мой лабиринт')
#
#     def get_header_personal_elements(self) -> List[WebElement]:
#         return self.are_visible('xpath', self.__header_personal_elements, 'сообщения, мой лабиринт, отложено, корзина')
#
#     def get_dropdown_menu_my_maze_link(self) -> List[WebElement]:
#         return self.are_visible('css', self.__dropdown_menu_my_maze, 'выпадающее меню кнопки мой лабиринт')
#
#     def get_orders(self) -> WebElement:
#         return self.is_visible('xpath', self.__orders, 'заказы')
#
#     def get_browsing_history(self) -> WebElement:
#         return self.is_visible('xpath', self.__browsing_history, 'история заказов')
#
#     def get_deferred(self) -> WebElement:
#         return self.is_visible('xpath', self.__deferred, 'отложенные')
#
#     def get_balance(self) -> WebElement:
#         return self.is_visible('xpath', self.__balance, 'баланс')
#
#     def get_settings(self) -> WebElement:
#         return self.is_visible('xpath', self.__settings, 'настройки')
#
#     def get_basket(self) -> WebElement:
#         return self.is_visible('xpath', self.__basket, 'моя корзина')
#
#     def get_full_access_to_labyrinth(self) -> WebElement:
#         return self.is_visible('xpath', self.__full_access_to_labyrinth, 'полный доступ к лабиринту')
#
#     def place_the_cursor(self) -> WebElement:
#         element = self.get_nav_link_my_maze()
#         return ActionChains(self.driver).click_and_hold(element).perform()
#
#     def get_list_header_personal(self) -> List[WebElement]:
#         lst = [self.get_orders(), self.get_orders(), self.get_deferred(), self.get_basket]
#         return lst
#
#     def get_list_dropdown_menu_my_maze(self) -> List[WebElement]:
#         lst = [self.get_orders(), self.get_browsing_history(), self.get_deferred(), self.get_balance(),
#                self.get_settings(), self.get_full_access_to_labyrinth()]
#         return lst


# self.__deferred: str = "//span[contains(text(),'Отложенные')]"
# self.__balance: str = "//span[contains(text(),'Баланс')]"
# self.__settings: str = "//span[contains(text(),'Мои данные')]"
# self.__full_access_to_labyrinth: str = "//span[contains(text(),'Авторизоваться в личном кабинете')]"
# self.__basket: str = "//a[contains(text(),'Моя корзина')]"

# def get_nav_link_my_maze(self) -> WebElement:
#     return self.is_visible('css', self.__nav_link_my_maze, 'мой лабиринт')

# self.__orders: str = "//span[contains(text(),'Заказы')]"
# self.__browsing_history: str = "//span[contains(text(),'История просмотра')]"
# def get_orders(self) -> WebElement:
#     """"""
#     return self.is_visible('xpath', self.__orders, 'заказы')
#
# def get_browsing_history(self) -> WebElement:
#     """"""
#     return self.is_visible('xpath', self.__browsing_history, 'история заказов')
#
# def get_deferred(self) -> WebElement:
#     """"""
#     return self.is_visible('xpath', self.__deferred, 'отложенные')
#
# def get_balance(self) -> WebElement:
#     """"""
#     return self.is_visible('xpath', self.__balance, 'баланс')
#
# def get_settings(self) -> WebElement:
#     return self.is_visible('xpath', self.__settings, 'настройки')
#
# def get_basket(self) -> WebElement:
#     """"""
#     return self.is_visible('xpath', self.__basket, 'моя корзина')

# def get_full_access_to_labyrinth(self) -> WebElement:
#     """"""
#     return self.is_visible('xpath', self.__full_access_to_labyrinth, 'полный доступ к лабиринту')


# def get_list_header_personal(self) -> List[WebElement]:
#     """"""
#     lst = [self.get_orders(), self.get_orders(), self.get_deferred(), self.get_basket]
#     return lst
#
# def get_list_dropdown_menu_my_maze(self) -> List[WebElement]:
#     """"""
#     lst = [self.get_orders(), self.get_browsing_history(), self.get_deferred(), self.get_balance(),
#            self.get_settings(), self.get_full_access_to_labyrinth()]
#     return lst


# lst_search_book = search_field.get_adding_element_to_list(search_field.get_name_of_the_book())
# lst_book = Utils.get_join_string(lst_search_book)
# lst = ", ".join(lst_search_book)
# w = re.findall(book_russian, lst_book)

# search_field.get_maze_search().send_keys(search_input_captain_daughter)
# search_field.get_search_button().click()

# lst = search_field.get_adding_element_to_list(search_field.get_name_of_the_book())
        # lst_1 = Utils.get_join_string(lst)
        # # # lst = ", ".join(lst_search_book)
        # w = re.findall(book_titles_edgar_raven, lst_1)
        #
        #
        # # lst = search_field.get_adding_element_to_list(search_field.get_name_of_the_book())
        # # lst_1 = ", ".join(lst)
        # # w = re.findall(book_titles_english, lst_1)
        # print(lst)
        # print('==============================================================================================')
        # print(lst_1)
        # print('==============================================================================================')
        # print(w)
        #
        # for element in w:
        #     assert element == book_titles_edgar_raven

# lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_russian)
# if len(lst_book) > 0:
#     for element in lst_book:
#         assert element == book_russian, 'в списке книг есть элементы'
# else:
#     assert lst_book == book_russian, 'список книг пустой'
#
# lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_russian)
# if len(lst_book) > 0:
#     for element in lst_author:
#         assert element == book_author_russian, 'в списке книг есть элементы'
# else:
#     assert lst_book == book_author_russian, 'список книг пустой'
#
# lst = ['Капитанская дочка',
#        'Капитанская дочка. Подробный иллюстрированный комментарий к роману А.С. Пушкина "Капитанская дочка"',
#        'Капитанская дочка. Сборник', 'Капитанская дочка', 'Евгений Онегин. Повести Белкина. Капитанская дочка',
#        'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка',
#        'Капитанская дочка. Избранное', 'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка',
#        'Капитанская дочка. Повести', 'Капитанская дочка: повести', 'Дубровский. Капитанская дочка', 'Капитанская дочка',
#        'Дубровский. Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка',
#        'Пушкин А. С. Проза: Повести покойного Ивана Петровича Белкина; Дубровский; Кнская дочка. Повесть',
#        'Капитанская дочка (Подробный комментарий, учебный материал, интерпретации)', 'CD Капитанская дочка (CDmp3)',
#        'Пушкин А.С.: "Евгений Онегин", "Дубровский", "Капитанская дочка"', 'Капитанская дочка',
#        'Капитанская дочка: 7-8 классы. Комментарий, указатель, учебный материал', 'Капитанская дочка (CDmp3)',
#        'Капитанская дочка', 'Капитанская дочка',
#        'Капитанская дочка. Дубровский. Повести покойного Ивана Петровича Белкина',
#        'Повести покойного Ивана Петровича Белкина; Пиковая дама; Капитанская дочка [и др.]',
#        'Повести покойного Ивана Петровича Белкина. Капитанская дочка. Дубровский', 'Капитанская дочка',
#        'Капитанская дочка', 'Дубровский. Капитанская дочка. Повести Белкина', 'Капитанская дочка', 'Капитанская дочка',
#        'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка. Полтава. Дубровский. Медный всадник',
#        'Капитанская дочка (CDmp3)', 'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка']
#
# ghg = ['Капитанская дочка',
#        'Капитанская дочка. Подробный иллюстрированный комментарий к роману А.С. Пушкина "Капитанская дочка"',
#        'Капитанская дочка. Сборник', 'Капитанская дочка', 'Евгений Онегин. Повести Белкина. Капитанская дочка',
#        'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка',
#        'Капитанская дочка. Избранное', 'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка',
#        'Капитанская дочка. Повести', 'Капитанская дочка: повести', 'Дубровский. Капитанская дочка', 'Капитанская дочка',
#        'Дубровский. Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка',
#        'Пушкин А. С. Проза: Повести покойного Ивана Петровича Белкина; Дубровский; Капитанская дочка (CDmp3)',
#        'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка',
#        'Капитанская дочка. Ремастированный (DVD)', 'Капитанская дочка (CDmp3)',
#        'Капитанская дочка (исполнитель А.Котов) (CDmp3)', 'Капитанская дочка',
#        'Капитанская дочка и другие произведения', 'Капитанская дочка: Повесть',
#        'Пишем сочинения по повести А.С. Пушкина "Капитанская дочка"', 'Капитанская дочка (CD)',
#        'История Пугачева. Капитанская дочка', 'Капитанская дочка. Повесть',
#        'Капитанская дочка (Подробный комментарий, учебный материал, интерпретации)', 'CD Капитанская дочка (CDmp3)',
#        'Пушкин А.С.: "Евгений Онегин", "Дубровский", "Капитанская дочка"', 'Капитанская дочка',
#        'Капитанская дочка: 7-8 классы. Комментарий, указатель, учебный материал', 'Капитанская дочка (CDmp3)',
#        'Капитанская дочка', 'Капитанская дочка',
#        'Капитанская дочка. Дубровский. Повести покойного Ивана Петровича Белкина',
#        'Повести покойного Ивана Петровича Белкина; Пиковая дама; Капитанская дочка [и др.]',
#        'Повести покойного Ивана Петровича Белкина. Капитанская дочка. Дубровский', 'Капитанская дочка',
#        'Капитанская дочка', 'Дубровский. Капитанская дочка. Повести Белкина', 'Капитанская дочка', 'Капитанская дочка',
#        'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка. Полтава. Дубровский. Медный всадник',
#        'Капитанская дочка (CDmp3)', 'Капитанская дочка', 'Капитанская дочка', 'Капитанская дочка']
#
# captain_daughter = 'Капитанская дочка'
# str: str = ", ".join(ghg)
# w = re.findall(r'Капитанская дочка', str)
#
# print(str)
# print(w)
#
# for i in w:
#     assert i == 'Капитанская дочка'

# for i in w:
#     if i == 'Капитанская дочка1':
#         print('не равно')
#     else:
#         print('равно')
#


lst = [
    (0, 3, 2), (0, 4, 3)
]

print(lst[1])

