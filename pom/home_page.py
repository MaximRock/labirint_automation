import time

from selenium.webdriver import ActionChains

from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from typing import List


class HomePage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = WebDriverWait(driver, 15, 0.3)
        self.__nav_link_my_maze: str = 'div>ul>li>a[class*=js-b-autofade-wrap]'
        self.__nav_link_email: str = 'input[class*=formvalidate-error]'
        self.__nav_link_sig_in: str = '[value="Войти"]'
        self.__code: str = 'input[class*=formvalidate-error]'
        self.__check_and_login: str = 'form[id="auth-email-sent"]>[type="submit"]'
        self.__personal_cabinet: str = "//span[starts-with(text(),'Личный кабинет')]"
        self.__sleep: float = 10
        self.__other_login_methods: str = '//a[starts-with(text(),"Другие способы входа")]'
        self.__auth_social_elements: str = "//ul[@class='new-auth__auth-social-list']/li"
        self.__button_sig_in: str = 'input[id=g-recap-0-btn]'
        self.__nav_link_my_maze: str = 'div>ul>li>a[class*=js-b-autofade-wrap]'
        self.__header_personal_elements: str = "//ul[contains(@class, 'b-header-b-personal-e-list ul-justify')]/li[position() > 2]"
        self.__dropdown_menu_my_maze: str = 'ul[class=user-top-menu]>li'
        self.__orders: str = "//span[contains(text(),'Заказы')]"
        self.__browsing_history: str = "//span[contains(text(),'История просмотра')]"
        self.__deferred: str = "//span[contains(text(),'Отложенные')]"
        self.__balance: str = "//span[contains(text(),'Баланс')]"
        self.__settings: str = "//span[contains(text(),'Мои данные')]"
        self.__full_access_to_labyrinth: str = "//span[contains(text(),'Авторизоваться в личном кабинете')]"
        self.__basket: str = "//a[contains(text(),'Моя корзина')]"

    def get_nav_link_my_maze(self) -> WebElement:
        return self.is_visible('css', self.__nav_link_my_maze, 'мой лабиринт')

    def get_nav_link_mail(self) -> WebElement:
        return self.is_visible('css', self.__nav_link_email, 'поле ввода email')

    def get_nav_link_sig_in(self) -> WebElement:
        return self.is_visible('css', self.__nav_link_sig_in, 'кнопка войти')

    def get_code(self) -> WebElement:
        return self.is_visible('css', self.__code, 'поле ввода кода')

    def get_check_and_login(self) -> WebElement:
        return self.is_visible('css', self.__check_and_login, 'кнопка проверить и войти')

    def personal_cabinet(self) -> str:
        return self.is_visible('xpath', self.__personal_cabinet, 'личный кабинет').text[:-2]

    def get_other_login_methods(self) -> WebElement:
        return self.is_visible('xpath', self.__other_login_methods, 'другие способы входа')

    def get_auth_social_elements(self) -> List[WebElement]:
        return self.are_visible('xpath', self.__auth_social_elements, 'иконки социальных сетей')

    def get_button_sig_in(self) -> WebElement:
        return self.is_visible('css', self.__button_sig_in, 'кнопка Войти для фикстуры')

    def sleep(self) -> object:
        return time.sleep(self.__sleep)

    def get_discount_phone_mail(self, discount_phone_mail) -> None:
        self.get_nav_link_my_maze().click()
        self.get_nav_link_mail().clear()
        self.get_nav_link_mail().send_keys(discount_phone_mail)

    def get_my_discount_code(self, my_discount_code) -> None:
        self.get_nav_link_sig_in().click()
        self.get_code().send_keys(my_discount_code)
        self.get_check_and_login().click()

    def get_auth_social_link(self) -> None:
        self.get_nav_link_my_maze().click()
        self.get_other_login_methods().click()

    # def get_nav_link_my_maze(self) -> WebElement:
    #     return self.is_visible('css', self.__nav_link_my_maze, 'мой лабиринт')

    def get_header_personal_elements(self) -> List[WebElement]:
        return self.are_visible('xpath', self.__header_personal_elements, 'сообщения, мой лабиринт, отложено, корзина')

    def get_dropdown_menu_my_maze_link(self) -> List[WebElement]:
        return self.are_visible('css', self.__dropdown_menu_my_maze, 'выпадающее меню кнопки мой лабиринт')

    def get_orders(self) -> WebElement:
        return self.is_visible('xpath', self.__orders, 'заказы')

    def get_browsing_history(self) -> WebElement:
        return self.is_visible('xpath', self.__browsing_history, 'история заказов')

    def get_deferred(self) -> WebElement:
        return self.is_visible('xpath', self.__deferred, 'отложенные')

    def get_balance(self) -> WebElement:
        return self.is_visible('xpath', self.__balance, 'баланс')

    def get_settings(self) -> WebElement:
        return self.is_visible('xpath', self.__settings, 'настройки')

    def get_basket(self) -> WebElement:
        return self.is_visible('xpath', self.__basket, 'моя корзина')

    def get_full_access_to_labyrinth(self) -> WebElement:
        return self.is_visible('xpath', self.__full_access_to_labyrinth, 'полный доступ к лабиринту')

    def place_the_cursor(self) -> WebElement:
        element = self.get_nav_link_my_maze()
        return ActionChains(self.driver).click_and_hold(element).perform()

    def get_list_header_personal(self) -> List[WebElement]:
        lst = [self.get_orders(), self.get_orders(), self.get_deferred(), self.get_basket]
        return lst

    def get_list_dropdown_menu_my_maze(self) -> List[WebElement]:
        lst = [self.get_orders(), self.get_browsing_history(), self.get_deferred(), self.get_balance(),
               self.get_settings(), self.get_full_access_to_labyrinth()]
        return lst

