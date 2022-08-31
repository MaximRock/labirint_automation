import time

from selenium.webdriver import ActionChains

from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class HomePage(SeleniumBase):
    """Класс домашней страницы,
    super - наследуем класс SeleniumBase,
    переменные - локаторы домашней страницы"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
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


    def get_nav_link_my_maze(self) -> WebElement:
        """Панель личного кабинета ссылка - мой лобиринт"""
        return self.is_visible('css', self.__nav_link_my_maze, 'мой лабиринт')

    def get_nav_link_mail(self) -> WebElement:
        """Регистрация - поле ввода email"""
        return self.is_visible('css', self.__nav_link_email, 'поле ввода email')

    def get_nav_link_sig_in(self) -> WebElement:
        """Регистрация - кнопка войти"""
        return self.is_visible('css', self.__nav_link_sig_in, 'кнопка войти')

    def get_code(self) -> WebElement:
        """Регистрация - поле ввода скидочного кода"""
        return self.is_visible('css', self.__code, 'поле ввода кода')

    def get_check_and_login(self) -> WebElement:
        """Регистрация - конопка проверить и войти"""
        return self.is_visible('css', self.__check_and_login, 'кнопка проверить и войти')

    def personal_cabinet(self) -> str:
        """Заголовок - личный кабинет"""
        return self.is_visible('xpath', self.__personal_cabinet, 'личный кабинет').text[:-2]

    def get_other_login_methods(self) -> WebElement:
        """Регистрация - кнопка другие способы входа"""
        return self.is_visible('xpath', self.__other_login_methods, 'другие способы входа')

    def get_auth_social_elements(self) -> List[WebElement]:
        """Список - иконки социальных сетей"""
        return self.are_visible('xpath', self.__auth_social_elements, 'иконки социальных сетей')

    def get_button_sig_in(self) -> WebElement:
        """кнопка Войти для фикстуры"""
        return self.is_visible('css', self.__button_sig_in, 'кнопка Войти для фикстуры')

    def sleep(self) -> object:
        """3-х секундное ожидание входа"""
        return time.sleep(self.__sleep)

    def get_discount_phone_mail(self, discount_phone_mail) -> None:
        """Метод класса - кликаем на поле ввода, очищаем поле ввода,
        ввод позитивных и негативных проверок поля ввода email"""
        self.get_nav_link_my_maze().click()
        self.get_nav_link_mail().clear()
        self.get_nav_link_mail().send_keys(discount_phone_mail)

    def get_my_discount_code(self, my_discount_code) -> None:
        """Метод класса - кликаем на поле ввода, очищаем поле ввода,
        ввод позитивных и негативных проверок поля ввода кода скидки"""
        self.get_nav_link_sig_in().click()
        self.get_code().send_keys(my_discount_code)
        self.get_check_and_login().click()

    def get_auth_social_link(self) -> None:
        """Метод класса - кликаем на поле ввода, очищаем поле ввода,
        ввод позитивных и негативных проверок поля ввода email"""
        self.get_nav_link_my_maze().click()
        self.get_other_login_methods().click()

    def get_header_personal_elements(self) -> List[WebElement]:
        """Список - меню личного кабинета сообщения, мой лабиринт, отложено, корзина"""
        return self.are_visible('xpath', self.__header_personal_elements, 'сообщения, мой лабиринт, отложено, корзина')

    def get_dropdown_menu_my_maze_link(self) -> List[WebElement]:
        """Список - выпадающее меню кнопки мой лабиринт"""
        return self.are_visible('css', self.__dropdown_menu_my_maze, 'выпадающее меню кнопки мой лабиринт')

    def place_the_cursor(self) -> WebElement:
        """Метод класса - выбор выпадающего меню кнопки мой лобиринт"""
        element = self.get_nav_link_my_maze()
        return ActionChains(self.driver).click_and_hold(element).perform()
