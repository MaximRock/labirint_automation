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

