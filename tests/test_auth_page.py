import re
import time

import pytest

from base.utils import Utils
from pom.home_page import HomePage
from settings import my_code, my_login, my_cabinet, list_my_discount_code_negative, list_discount_phone_mail_negative, \
    list_discount_phone_mail_positive, list_social_elements, list_header_personal, \
    list_header_personal_button_my_maze_dropdown_menu, book_russian, list_of_values_in_the_search_field_rassian, \
    book_author_russian, list_of_values_in_the_search_field_english, book_author_english, book_titles_english, \
    book_titles_edgar_raven, book_author_edgar_allan_poe, list_of_values_in_the_search_field_edgar_allan_poe_raven, \
    list_of_values_in_the_search_field_empty_spaces


@pytest.mark.usefixtures('setup')
class TestAuthorization:
    """Тест авторизации на сайте"""

    def test_auth_my_maze(self):
        """тест полной авторизации на сайте с использованием кода скидки
         полученной в рузультате ручной авторизации, проверка скриншот
         страницы "личный кабинет, my_cabinet.png"""

        auth_page = HomePage(self.driver)
        auth_page.get_discount_phone_mail(my_login)
        auth_page.get_my_discount_code(my_code)
        auth_page.sleep()
        auth_page.get_nav_link_my_maze().click()
        auth_page.screenshot('tests/screenshot/1_authorization/my_cabinet.png')

        print(f'{auth_page.personal_cabinet()} == {my_cabinet}')

        assert auth_page.personal_cabinet() == my_cabinet

    @pytest.mark.parametrize("discount_phone_mail", list_discount_phone_mail_positive)
    def test_nav_link_email_positive(self, discount_phone_mail):
        """позитивный тест, вводим код скидки используемый при авторизации,
        корректный номер телефона, корректный почтовый адрес,
        проверка активнаная кнопка "Войти"""

        auth_page = HomePage(self.driver)
        auth_page.get_discount_phone_mail(discount_phone_mail)

        assert auth_page.get_nav_link_sig_in().is_enabled() is True

    @pytest.mark.parametrize("discount_phone_mail", list_discount_phone_mail_negative)
    def test_nav_link_email_negative(self, discount_phone_mail):
        """негативный тест проверки поля для ввода кода скидки, телефона, почты,
        вводимые данные в файле settings.py, в списке list_discount_phone_mail_negative,
        проверка неактивная кнопка "Войти"""

        auth_page = HomePage(self.driver)
        auth_page.get_discount_phone_mail(discount_phone_mail)

        print(f"Вводимое значение - {discount_phone_mail}")

        if auth_page.get_nav_link_sig_in().is_enabled() is True:
            auth_page.get_nav_link_sig_in().click()
            assert auth_page.get_nav_link_sig_in().is_enabled() is False
        else:
            assert auth_page.get_nav_link_sig_in().is_enabled() is False

    @pytest.mark.parametrize("my_discount_code", list_my_discount_code_negative)
    def test_nav_link_my_code_negative(self, my_discount_code):
        """негативный тест проверки поля для ввода кода скидки,
        вводимые данные в файле settings.py, в списке list_my_discount_code_negative,
        проверка неактивная кнопка "проверить код и войти"""

        auth_page = HomePage(self.driver)
        auth_page.get_discount_phone_mail(my_login)
        auth_page.get_my_discount_code(my_discount_code)

        print(f"Вводимое значение - {my_discount_code}")

        assert auth_page.get_check_and_login().is_enabled() is False

    def test_icons_auth_social_elements(self):
        """тест проверки работоспособности иканок авторизации через социальные сети,
        провереа скриншот страницы авторизации соц. сети
        в папке tests/screenshot/1_authorization/"""

        auth_page = HomePage(self.driver)
        auth_page.get_auth_social_link()

        for index in range(5):
            auth_page.get_auth_social_elements()[index].click()
            auth_page.screenshot(f'tests/screenshot/1_authorization/{list_social_elements[index]}.png')
            auth_page.driver.back()
            auth_page.get_auth_social_link()


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('auth_my_maze')
class TestHeaderMenuPersonal:
    """Тест добавления товара в корзину"""

    def test_header_personal_click(self):
        """тест проверки меню сообщения мой лабиринт отложенно корзина
        проверка скриншоты в папке:
        tests/screenshot/2_home_page_header_personal"""

        header_personal = HomePage(self.driver)

        for element in range(len(header_personal.get_header_personal_elements())):
            header_personal.get_header_personal_elements()[element].click()
            header_personal.screenshot(
                f'tests/screenshot/2_home_page_header_personal/{list_header_personal[element]}.png')

    def test_dropdown_menu_my_maze_click(self):
        """тест проверки выпадающего меню мой лабиринт: заказы, вы смотрели, отложенные, балонс, настройки, выход
        проверка скринщоты в папке :
        tests/screenshot/3_home_page_header_personal_button_my_maze"""

        header_personal = HomePage(self.driver)
        header_personal.get_refresh()
        header_personal.place_the_cursor(header_personal.get_nav_link_my_maze())

        for element in range(len(header_personal.get_dropdown_menu_my_maze_link())):
            header_personal.get_dropdown_menu_my_maze_link()[element].click()
            header_personal.screenshot(
                f'tests/screenshot/3_home_page_header_personal_button_my_maze/'
                f'{list_header_personal_button_my_maze_dropdown_menu[element]}.png')
            header_personal.place_the_cursor(header_personal.get_nav_link_my_maze())


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('auth_my_maze')
class TestAddingProduct:

    def test_adding_product_to_cart(self):
        """Тест проверки добавления товара в корзину,
        проверка: видимость заголовка 'В корзине', если товар отсутствует на склоде выводим сообщение,
        проверяем всегда первую левую книгу"""

        adding_product = HomePage(self.driver)

        adding_product.get_maze_search().send_keys(book_russian)
        adding_product.get_search_click_and_click_book()
        if adding_product.get_in_stock().is_displayed():
            adding_product.get_add_to_cart_and_basket_click()
            assert adding_product.get_in_the_basket() == 'В корзине'
        else:
            print('Товар отсутствует на складе')


@pytest.mark.usefixtures('setup')
class TestSearch:
    """Тест поля "Поиска" на главной странице"""

    def test_search_relevance_check(self):
        """Тест релевантности поиска по названию книги,
        создаем список результатов поиска на главной странице,
        проверка - название и автор книги совпадают с ожидаемым рзультатом"""
        search_field = HomePage(self.driver)
        search_field.get_search_input_field(book_russian)

        lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_russian)
        if len(lst_book) > 0:
            for element in lst_book:
                assert element == book_russian, 'в списке книг есть элементы'
        else:
            assert lst_book == book_russian, 'список книг пустой'

        lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_russian)
        if len(lst_book) > 0:
            for element in lst_author:
                assert element == book_author_russian, 'в списке книг есть элементы'
        else:
            assert lst_book == book_author_russian, 'список книг пустой'

    @pytest.mark.parametrize("search_input_captain_daughter", list_of_values_in_the_search_field_rassian)
    def test_book_russian_search(self, search_input_captain_daughter):
        """Тест проверки поле ввода Поиск используя параметризацию на русском языке,
        даные ввода файл settings.py в списке list_of_values_in_the_search_field_rassian"""
        search_field = HomePage(self.driver)
        search_field.get_search_input_field(search_input_captain_daughter)

        lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_russian)
        if len(lst_book) > 0:
            for element in lst_book:
                assert element == book_russian, 'в списке книг есть элементы'
        else:
            assert lst_book == book_russian, 'список книг пустой'

        lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_russian)
        if len(lst_book) > 0:
            for element in lst_author:
                assert element == book_author_russian, 'в списке книг есть элементы'
        else:
            assert lst_book == book_author_russian, 'список книг пустой'

        print(f'вводимое значение {search_input_captain_daughter}')

    @pytest.mark.parametrize("search_input_programming_on_python", list_of_values_in_the_search_field_english)
    def test_book_english_search(self, search_input_programming_on_python):
        """Тест проверки поле ввода Поиск используя параметризацию на английском языке,
        даные ввода файл settings.py в списке list_of_values_in_the_search_field_english"""
        search_field = HomePage(self.driver)
        search_field.get_search_input_field(search_input_programming_on_python)

        lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_titles_english)
        if len(lst_book) > 0:
            for element in lst_book:
                assert element == book_titles_english, 'в списке книг есть элементы'
        else:
            assert lst_book == book_titles_english, 'список книг пустой'

        lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_english)
        if len(lst_book) > 0:
            for element in lst_author:
                assert element == book_author_english, 'в списке книг есть элементы'
        else:
            assert lst_book == book_author_english, 'список книг пустой'

        print(f'вводимое значение {search_input_programming_on_python}')

    @pytest.mark.parametrize("search_input_edgar_allan_poe_raven",
                             list_of_values_in_the_search_field_edgar_allan_poe_raven)
    def test_edgar_allan_poe_raven(self, search_input_edgar_allan_poe_raven):
        """Тест проверки нижнего предела поиска - осуществляем поиск по имени автора 'По Эдгар Аллан' и
        названия книги 'Ворон', первый тест passed, остальные failed,
        даные ввода файл settings.py в списке list_of_values_in_the_search_field_edgar_allan_poe_raven"""
        search_field = HomePage(self.driver)
        search_field.get_search_input_field(search_input_edgar_allan_poe_raven)

        lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_titles_edgar_raven)
        if len(lst_book) > 0:
            for element in lst_book:
                assert element == book_titles_edgar_raven, 'в списке книг есть элементы'
        else:
            assert lst_book == book_titles_edgar_raven, 'список книг пустой'

        lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_edgar_allan_poe)
        if len(lst_author) > 0:
            for element in lst_book:
                assert element == book_titles_edgar_raven, 'в списке авторов есть элементы'
        else:
            assert lst_author == book_titles_edgar_raven, 'список авторов пустой'

        print(f'вводимое значение {search_input_edgar_allan_poe_raven}')

    @pytest.mark.parametrize("search_input_empty_spaces",
                             list_of_values_in_the_search_field_empty_spaces)
    def test_field_empty_spaces(self, search_input_empty_spaces):
        """Тест проверки поиска при пустом значении, при вводе одного пробела, двух пробелов"""
        search_field = HomePage(self.driver)
        search_field.get_search_input_field(search_input_empty_spaces)
        current_url = search_field.get_current_url()
        if current_url == 'https://www.labirint.ru/':
            assert current_url == 'https://www.labirint.ru/', 'если url страниц равны тест passed'
        else:
            assert search_field.get_search_error_book().is_displayed(), 'видим на странице - Мы ничего не нашли по ' \
                                                                        'вашему запросу! Что делать? '

        print(f'вводимое значение {search_input_empty_spaces}')

@pytest.mark.usefixtures('setup')
class TestHeaderMenu:
    """"""
    def test_header_menu_click(self):
        """"""
        header_menu = HomePage(self.driver)
        list_header_menu_text = []
        for element in range(len(header_menu.get_header_menu_list())):
            header_menu.get_header_menu_list()[element].click()
            list_header_menu_text.append(header_menu.get_header_menu_headlines().text)
            assert header_menu.get_header_menu_headlines().text == list_header_menu_text[element]
        print(list_header_menu_text)

    def test_header_menu_link_more(self):
        """"""
        header_menu = HomePage(self.driver)

        header_menu.place_the_cursor(header_menu.get_header_menu_link_more()).click()






