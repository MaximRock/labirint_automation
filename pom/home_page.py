import time
import re

from selenium.webdriver import ActionChains

from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Any

from base.utils import Utils


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
        self.__maze_search: str = '//input[@placeholder="Поиск по Лабиринту"]'
        self.__search_button: str = '//span[starts-with(text(),"Искать")]'
        self.__book: str = "//div[contains(@class, 'genres-carousel__container  products-row')]/div[position()=1]"
        self.__add_to_cart: str = "//span[starts-with(text(),'в корзину')]"
        self.__basket: str = "//span[starts-with(text(),'Корзина')]"
        self.__in_the_basket: str = "//span[starts-with(text(),'В корзине')]"
        self.__in_stock: str = "//span[starts-with(text(),'На складе')]"
        self.__name_of_the_book: str = "//a[@class='product-title-link']/span"
        self.__author_book: str = "//div[@class='product-author']/a/span"
        self.__search_error_book: str = "//div[@class='search-error bestsellers']/h1"
        self.__header_menu_list: str = "//ul[@class='b-header-b-menu-e-list']/li[position()<6]"
        self.__header_menu_headlines: str = "//h1"
        self.__header_menu_link_more: str = "//span[contains(text(),'Еще')]"


#//span[contains(text(),'Еще')]
#//ul[@class='b-header-b-menu-e-list'] /li
#//div[@class='search-error bestsellers'] /h1
    #//div[@class='product-author']/a/span
    #//a[@class='product-title-link']/span
    # //a[@title='Пушкин Александр Сергеевич']/span[contains(text(),'Пушкин Александр Сергеевич')]
    # //a[@class='product-title-link']/span[starts-with(text(),'Капитанская дочка')]
    # //span[starts-with(text(),'Капитанская дочка')]
    # //span[starts-with(text(),'На складе')]
    # //span[starts-with(text(),'В корзине')]
    # //span[starts-with(text(),"в корзину")].
    # //div[contains(@class, 'genres-carousel__container  products-row' )]/div[position()=1]

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

    def get_maze_search(self) -> WebElement:
        """Поле ввода поиск по лабиринту"""
        return self.is_visible('xpath', self.__maze_search, 'Поле ввода Поиск по Лабиринту')

    def get_search_button(self) -> WebElement:
        """Кнопка искать в поле поиска по лабиринту"""
        return self.is_visible('xpath', self.__search_button, 'кнопка искать в поле поиска по лабиринту')

    def get_book(self) -> WebElement:
        """Добавление товара в карзину - первая книга результат поиска"""
        return self.is_visible('xpath', self.__book, 'первая книга результат поиска')

    def get_add_to_cart(self) -> WebElement:
        """Добавление товара в карзину - кнопка 'добавить в корзину'"""
        return self.is_visible('xpath', self.__add_to_cart, 'кнопка добавить в корзину')

    def get_basket(self) -> WebElement:
        """Добавление товара в карзину - кнопка 'корзина'"""
        return self.is_visible('xpath', self.__basket, 'кнопка моя корзина')

    def get_in_the_basket(self) -> str:
        """Добавление товара в карзину - проверка товара в корзине"""
        return self.is_visible('xpath', self.__in_the_basket, 'проверка товара в корзине').text

    def get_in_stock(self) -> WebElement:
        """Добавление товара в карзину - проверка наличия товара на складе"""
        return self.is_visible('xpath', self.__in_stock, 'проверка наличия товара на складе')

    def get_search_click_and_click_book(self) -> None:
        """Добавление товара в карзину - метод класса,
        нажать на кнопку искать и на книгу"""
        self.get_search_button().click()
        self.get_book().click()

    def get_add_to_cart_and_basket_click(self) -> None:
        """Добавление товара в карзину - метод класса,
        нажать на добавить в корзину и корзина"""
        self.get_add_to_cart().click()
        self.get_basket().click()

    def get_name_of_the_book(self) -> List[WebElement]:
        """Строка поиска - список книг результат поиска"""
        return self.are_visible('xpath', self.__name_of_the_book, 'список книг результат поиска')

    def get_author_book(self) -> List[WebElement]:
        """Строка поиска - список автора книги результат поиска"""
        return self.are_visible('xpath', self.__author_book, 'список авторов')

    def get_search_error_book(self) -> WebElement:
        return self.is_visible('xpath', self.__search_error_book, 'неудачный поиск книги')

    def get_search_input_field(self, search_element: str) -> None:
        """Поле поиска - вводим значение и нажимаем кнопку искать"""
        self.get_maze_search().send_keys(search_element)
        self.get_search_button().click()

    def get_book_string(self, lst_webelement: List[WebElement], search_variable: str) -> list[Any]:
        """Поле поиска - создает список, преобразует в строку и находит элемент по шаблону"""
        lst_book = self.get_adding_element_to_list(lst_webelement)  # создает список
        check_lst_book = Utils.get_join_string(lst_book)  # преобразует в строку
        return re.findall(search_variable, check_lst_book)  # находит элемент

    def get_header_menu_list(self) -> List[WebElement]:
        """"""
        return self.are_visible('xpath', self.__header_menu_list, 'header меню список')

    def get_header_menu_headlines(self) -> WebElement:
        """"""
        return self.is_visible('xpath', self.__header_menu_headlines, 'заголовок')

    def get_header_menu_link_more(self):
        """"""
        return self.are_visible('xpath', self.__header_menu_link_more, 'ссылка ЕЩЕ')