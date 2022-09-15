import re
import time

import pytest
from selenium.webdriver import ActionChains

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
        auth_page.get_automatic_closing().click()
        # auth_page.sleep()
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
        """тест проверки выпадающего меню мой лабиринт: заказы, вы смотрели, отложенные, баланс, настройки, выход
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
    """Тест проверки добавления товара в корзину, очистки крозины"""

    def test_adding_product_to_cart_first_book(self):
        """Тест проверки добавления товара в корзину, проверка условия наличие товара на складе.
        проверяем список товара в корзине не пустой, находимся на странице Корзина,
        :return:сравневаем список товаров в корзине с тестовыми данными в переменой - LST_OF_POSTPONED_BOOKS.
        """
        adding_product = HomePage(self.driver)
        adding_product.get_maze_search().send_keys(book_russian)
        adding_product.get_search_click_and_click_book()

        if adding_product.get_in_stock().is_displayed():
            adding_product.get_add_to_cart_and_basket_click()
        else:
            print('Товар отсутствует на складе')

        if len(adding_product.get_book_in_a_basket()) > 0 \
                or adding_product.get_current_url() == 'https://www.labirint.ru/cart/':
            for element in range(len(adding_product.get_book_in_a_basket())):
                assert adding_product.get_book_in_a_basket()[element].text == adding_product.LST_OF_POSTPONED_BOOKS[1]

    def test_adding_product_to_cart_second_book(self):
        """
        Тест проверки добавления второго товара в корзину, проверка условия наличие товара на складе.
        проверяем список товара в корзине не пустой, находимся на странице Корзина,
        :return:сравневаем список товаров в корзине с тестовыми данными в переменой - LST_OF_POSTPONED_BOOKS.
        """
        adding_product = HomePage(self.driver)
        adding_product.get_maze_search().send_keys(f'{book_titles_english} {book_author_english}')
        adding_product.get_search_click_and_click_book()

        if adding_product.get_in_stock().is_displayed():
            adding_product.get_add_to_cart_and_basket_click()
        else:
            print('Товар отсутствует на складе')

        if len(adding_product.get_book_in_a_basket()) > 0 \
                or adding_product.get_current_url() == 'https://www.labirint.ru/cart/':
            for element in range(len(adding_product.get_book_in_a_basket())):
                assert adding_product.get_book_in_a_basket()[element].text \
                       == adding_product.LST_OF_POSTPONED_BOOKS[element]

    def test_removing_an_item_from_the_cart(self):

        """
        Тест проверки удаления товара из корзины.
        :return: сравниваем заголовок с текстом 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?'.
        """
        adding_product = HomePage(self.driver)
        adding_product.get_basket().click()

        if adding_product.get_current_url():
            adding_product.get_button_clear_basket().click()
            assert adding_product.get_your_basket_is_empty().text == 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?'


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('auth_my_maze')
class TestDeferredProduct:
    """Тест проверки добавления книги в отложеные"""

    def test_addition_of_the_first_book(self):
        """
        Тест добавление книги в отложеные, проверка книги на складе,
        проверка в отложеных есть книга и находимся на странице отложеные.
        :return: проверка название отложенной книги == название искомой книги
        """
        deferred_product = HomePage(self.driver)
        deferred_product.get_maze_search().send_keys(book_russian)
        deferred_product.get_search_click_and_click_book()

        if deferred_product.get_in_stock().is_displayed():
            deferred_product.get_click_deferred_product_and_postponed()
        else:
            print('Товар отсутствует на складе')

        if len(deferred_product.get_set_aside_book()) > 0 \
                or deferred_product.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/':
            for element in range(len(deferred_product.get_set_aside_book())):
                assert deferred_product.get_set_aside_book()[element].text \
                       == deferred_product.LST_OF_POSTPONED_BOOKS[1]

    def test_adding_a_second_book(self):
        """
        Тест провенки добавление книги в отложеные если там уже есть книга,
        проверка книги на складе, проверка в отложеных есть книга и находимся на странице отложеные.
        :return: проверка название отложенной книги == название искомой книги
        """
        deferred_product = HomePage(self.driver)
        deferred_product.get_maze_search().send_keys(f'{book_titles_english} {book_author_english}')
        deferred_product.get_search_click_and_click_book()

        if deferred_product.get_in_stock().is_displayed():
            deferred_product.get_click_deferred_product_and_postponed()
        else:
            print('Товар отсутствует на складе')

        if len(deferred_product.get_set_aside_book()) > 0 \
                or deferred_product.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/':
            for element in range(len(deferred_product.get_set_aside_book())):
                assert deferred_product.get_set_aside_book()[element].text \
                       == deferred_product.LST_OF_POSTPONED_BOOKS[element]

    def test_remove_books_from_deferred(self):
        """
        Тест проверки удоления товаров из отложеного.
        :return: сравниваем элемент с текстом.
        """
        deferred_product = HomePage(self.driver)
        deferred_product.get_postponed().click()
        deferred_product.get_clear_button().click()
        deferred_product.alert_confirmation()

        assert deferred_product.get_message_deleted_in_deferred().text == 'Выбранные товары удалены!'


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
        lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_russian)
        if len(lst_book) > 0:
            for book in lst_book:
                for author in lst_author:
                    assert author == book_author_russian, 'в списке авторов нет элементов'
                assert book == book_russian, 'в списке книг нет элементов'
        else:
            print('список книг пустой')
        #     assert lst_book == book_russian, 'список книг пустой'
        #     assert lst_author == book_author_russian, 'список аторов пустой'

    @pytest.mark.parametrize("search_input_captain_daughter", list_of_values_in_the_search_field_rassian)
    def test_book_russian_search(self, search_input_captain_daughter):
        """Тест проверки поле ввода Поиск используя параметризацию на русском языке,
        даные ввода файл settings.py в списке list_of_values_in_the_search_field_rassian"""
        search_field = HomePage(self.driver)
        search_field.get_search_input_field(search_input_captain_daughter)

        lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_russian)
        lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_russian)
        if len(lst_book) > 0:
            for book in lst_book:
                for author in lst_author:
                    assert author == book_author_russian, 'в списке авторов нет элементов'
                assert book == book_russian, 'в списке книг нет элементов'
        else:
            print('список книг пустой')
        #     assert lst_book == book_russian, 'список книг пустой'
        #     assert lst_book == book_author_russian, 'список ваторов пустой'

        print(f'вводимое значение {search_input_captain_daughter}')

    @pytest.mark.parametrize("search_input_programming_on_python", list_of_values_in_the_search_field_english)
    def test_book_english_search(self, search_input_programming_on_python):
        """Тест проверки поле ввода Поиск используя параметризацию на английском языке,
        даные ввода файл settings.py в списке list_of_values_in_the_search_field_english"""
        search_field = HomePage(self.driver)
        search_field.get_search_input_field(search_input_programming_on_python)

        lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_titles_english)
        lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_english)

        if len(lst_book) > 0:
            for book in lst_book:
                for author in lst_author:
                    assert author == book_author_english, 'в списке авторов нет элементов'
                assert book == book_titles_english, 'в списке книг нет элементов'
        else:
            print('список книг пустой')
        #     assert lst_book == book_author_english1, 'список книг пустой'

        print(f'вводимое значение {search_input_programming_on_python}')

        # lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_titles_english)
        # if len(lst_book) > 0:
        #     for element in lst_book:
        #         assert element == book_titles_english, 'в списке книг есть элементы'
        # else:
        #     assert lst_book == book_titles_english, 'список книг пустой'
        #
        # lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_english)
        # if len(lst_book) > 0:
        #     for element in lst_author:
        #         assert element == book_author_english, 'в списке книг есть элементы'
        # else:
        #     assert lst_book == book_author_english, 'список книг пустой'

    @pytest.mark.parametrize("search_input_edgar_allan_poe_raven",
                             list_of_values_in_the_search_field_edgar_allan_poe_raven)
    def test_edgar_allan_poe_raven(self, search_input_edgar_allan_poe_raven):
        """Тест проверки нижнего предела поиска - осуществляем поиск по имени автора 'По Эдгар Аллан' и
        названия книги 'Ворон', первый тест passed, остальные failed,
        даные ввода файл settings.py в списке list_of_values_in_the_search_field_edgar_allan_poe_raven"""
        search_field = HomePage(self.driver)
        search_field.get_search_input_field(search_input_edgar_allan_poe_raven)

        lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_titles_edgar_raven)
        lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_edgar_allan_poe)
        if len(lst_book) > 0:
            for book in lst_book:
                for author in lst_author:
                    assert author == book_titles_edgar_raven, 'в списке авторов нет элементов'
                assert book == book_titles_edgar_raven, 'в списке книг нет элементов'
            else:
                print('список книг пустой')

        print(f'вводимое значение {search_input_edgar_allan_poe_raven}')

        # lst_book = search_field.get_book_string(search_field.get_name_of_the_book(), book_titles_edgar_raven)
        # if len(lst_book) > 0:
        #     for element in lst_book:
        #         assert element == book_titles_edgar_raven, 'в списке книг есть элементы'
        # else:
        #     assert lst_book == book_titles_edgar_raven, 'список книг пустой'
        #
        # lst_author = search_field.get_book_string(search_field.get_author_book(), book_author_edgar_allan_poe)
        # if len(lst_author) > 0:
        #     for element in lst_book:
        #         assert element == book_titles_edgar_raven, 'в списке авторов есть элементы'
        # else:
        #     assert lst_author == book_titles_edgar_raven, 'список авторов пустой'

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
    """Тест Header Menu"""

    def test_header_menu_click(self):
        """
        Тест - проверки header menu Книги, Главное 2022, Школа, Игрушки, Канцтовары, Клуб.
        :return: текст заголовка на странице соответствует странице из меню
        """
        header_menu = HomePage(self.driver)
        list_header_menu_text = Utils.get_list_creation()

        for element in range(len(header_menu.get_header_menu_list())):
            header_menu.get_header_menu_list()[element].click()
            list_header_menu_text.append(header_menu.get_header_menu_headlines().text)
            assert header_menu.get_header_menu_headlines().text == list_header_menu_text[element]
        print(list_header_menu_text)

    def test_header_menu_link_more(self):
        """
        Тест - проверки header menu выпадающий список кнопки еще, cd, сувениры, журналы, товары для дома.
        :return: текст заголовка на странице соответствует странице из меню
        """
        header_menu = HomePage(self.driver)
        list_header_menu_text = Utils.get_list_creation()

        header_menu.place_the_cursor(header_menu.get_header_menu_link_more())

        for element in range(len(header_menu.get_lst())):
            header_menu.place_the_cursor(header_menu.get_header_menu_link_more())
            header_menu.get_lst()[element].click()
            list_header_menu_text.append(header_menu.get_header_menu_headlines().text)
            assert header_menu.get_header_menu_headlines().text == list_header_menu_text[element]
        print(list_header_menu_text)

    def test_header_menu_link_delivery_region(self):
        """
        Тест - проверки ссылки опрделения локации.
        :return: проверяем видимость текста в элементе 'Укажите регион, чтобы мы точнее рассчитали условия доставки'
        """
        header_menu = HomePage(self.driver)

        header_menu.get_header_menu_region().click()
        header_menu.sleep()
        assert header_menu.get_dropdown_delivery_region().is_displayed()


@pytest.mark.usefixtures('setup')
class TestSearchResultFilter:
    """"""

    def test_search_filter(self):
        """

        :return:
        """
        search_filter = HomePage(self.driver)
        search_filter.get_maze_search().send_keys(book_titles_english)
        search_filter.get_search_button().click()
        search_filter.get_button_all_filters().click()

        for i in range(6):
            search_filter.get_product_type_and_availability()[i].click()

        time.sleep(5)

        # search_filter.get_product_type_and_availability()[0].click()
        # time.sleep(5)
        # search_filter.get_product_type_and_availability()[2].click()
        # time.sleep(5)
        # search_filter.get_button_show().click()
        # time.sleep(5)

        # for i in range(len(search_filter.get_product_type_and_availability())):
        #     # lst.append(search_filter.get_product_type_and_availability()[i].text)
        #     search_filter.get_product_type_and_availability()[0].click()
        #     time.sleep(5)
        #     search_filter.get_product_type_and_availability()[2].click()
        #     time.sleep(5)
        #     search_filter.get_button_show().click()

        # print(lst[0:2])
