# from selenium.webdriver.support.wait import WebDriverWait
#
# from base.seleniumbase import SeleniumBase
# from selenium.webdriver.remote.webelement import WebElement
# from typing import List
#
#
# class HomepageNav(SeleniumBase):
#
#     def __init__(self, driver):
#         # super().__init__(driver)
#         self.wait = WebDriverWait(driver, 15, 0.3)
#         self.driver = driver
#         self.__nav_links_header: str = '#minwidth > div.top-header > div.b-header-outer > div.b-header-b-sec-menu.col-md-12 > div > ul>li'
#         self.__get_nav_header_personal: str = 'div[class=b-header-b-personal-wrapper]>ul[class*=ul-justify]'
#
#     def get_nav_links_header(self) -> List[WebElement]:
#         return self.are_visible('css', self.__nav_links_header, 'Header панель меню')
#
#     def get_nav_links_header_text(self) -> str:
#         nav_links_header = self.get_nav_links_header()
#         nav_links_header_text = [link.text for link in nav_links_header]
#         return ",".join(nav_links_header_text)
#
#     def get_nav_header_personal(self) -> List[WebElement]:
#         return self.are_visible('css', self.__nav_links_header, 'Header панель с корзиной')
