import time

import pytest

from pom.authorization import HomePageNavAuthorization, HomePageNavHeaderPersonal
from settings import my_code, my_login, my_cabinet, list_my_discount_code_negative, list_discount_phone_mail_negative, \
    list_discount_phone_mail_positive, list_social_elements, list_header_personal, \
    list_header_personal_button_my_maze_dropdown_menu


# lst_auto_link_text

@pytest.mark.usefixtures('setup')
class TestAuthorization:

    def test_auth_my_maze(self):
        """тест полной авторизации на сайте с использованием кода скидки
         полученной в рузультате ручной авторизации, проверка скриншот
         страницы "личный кабинет, my_cabinet.png"""

        auth_page = HomePageNavAuthorization(self.driver)
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

        auth_page = HomePageNavAuthorization(self.driver)
        auth_page.get_discount_phone_mail(discount_phone_mail)

        assert auth_page.get_nav_link_sig_in().is_enabled() is True

    @pytest.mark.parametrize("discount_phone_mail", list_discount_phone_mail_negative)
    def test_nav_link_email_negative(self, discount_phone_mail):
        """негативный тест проверки поля для ввода кода скидки, телефона, почты,
        вводимые данные в файле settings.py, в списке list_discount_phone_mail_negative,
        проверка неактивная кнопка "Войти"""

        auth_page = HomePageNavAuthorization(self.driver)
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

        auth_page = HomePageNavAuthorization(self.driver)
        auth_page.get_discount_phone_mail(my_login)
        auth_page.get_my_discount_code(my_discount_code)

        print(f"Вводимое значение - {my_discount_code}")

        assert auth_page.get_check_and_login().is_enabled() is False

    def test_icons_auth_social_elements(self):
        """тест проверки работоспособности иканок авторизации через социальные сети,
        провереа скриншот страницы авторизации соц. сети
        в папке tests/screenshot/1_authorization/"""

        auth_page = HomePageNavAuthorization(self.driver)
        auth_page.get_auth_social_link()

        for index in range(5):
            auth_page.get_auth_social_elements()[index].click()
            auth_page.screenshot(f'tests/screenshot/1_authorization/{list_social_elements[index]}.png')
            auth_page.driver.back()
            auth_page.get_auth_social_link()


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('auth_my_maze')
class TestHeaderPersonalMenu:

    def test_header_personal_click(self):
        """тест проверки меню сообщения мой лабиринт отложенно корзина
        проверка скриншоты в папке:
        tests/screenshot/2_home_page_header_personal"""

        header_personal = HomePageNavHeaderPersonal(self.driver)

        for element in range(4):
            header_personal.get_header_personal_elements()[element].click()
            header_personal.screenshot(f'tests/screenshot/2_home_page_header_personal/{list_header_personal[element]}.png')

    def test_dropdown_menu_my_maze_click(self):
        """тест проверки выпадающего меню мой лабиринт: заказы, вы смотрели, отложенные, болонс, настройки, выход
        проверка скринщоты в папке :
        tests/screenshot/3_home_page_header_personal_button_my_maze"""

        header_personal = HomePageNavHeaderPersonal(self.driver)
        header_personal.get_refresh()
        header_personal.place_the_cursor()

        for element in range(6):
            header_personal.get_dropdown_menu_my_maze_link()[element].click()
            header_personal.screenshot(
                f'tests/screenshot/3_home_page_header_personal_button_my_maze/'
                f'{list_header_personal_button_my_maze_dropdown_menu[element]}.png')
            header_personal.place_the_cursor()




