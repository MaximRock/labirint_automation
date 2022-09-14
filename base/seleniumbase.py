from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from typing import List, Any


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)

    def __get_selenium_by(self, find_by: str) -> dict:
        """Список локаторов в котором ключ это - строка локатор списка, значения связанны значениями поиска"""
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Ожидание элемента и возврат WebElement, если он виден"""
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Ожидание элемента и возврат WebElement, если он присутствует в DOM"""
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Ожидание, пока элемент не исчезнет"""
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """Ожидание элементов и возврат WebElements, если они видны"""
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """Ожидание элементов и возврат WebElements, если они присутствуют в DOM."""
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Ожидание элемента, пока элемент станет кликабельным"""
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def screenshot(self, file_name: str) -> str:
        """Создание скриншота"""
        return self.driver.save_screenshot(file_name)

    def get_refresh(self) -> WebElement:
        """Обновить страницу"""
        return self.driver.refresh()

    def get_current_url(self) -> WebElement:
        """url страницы на которой находимся"""
        return self.driver.current_url

    def place_the_cursor(self, element: WebElement) -> WebElement:
        """Выбор выпадающего меню"""
        return ActionChains(self.driver).click_and_hold(element).perform()

    def get_adding_element_to_list(self, elements: List[WebElement]) -> list[str]:
        """Создание списка текста WebElement - ов"""
        return [element.text for element in elements]

    def alert_confirmation(self) -> WebElement:
        """
        Подтверждение оповщения на странице.
        :return:
        """
        alert_obj = self.driver.switch_to.alert
        return alert_obj.accept()

