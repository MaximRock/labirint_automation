
from selenium.webdriver.support.events import AbstractEventListener
from pom.home_page import HomePage

class MyListener(AbstractEventListener):
    def after_find(self, by, value, driver):
        HomePage(driver).get_nav_link_my_maze().click()
        HomePage(driver).get_nav_link_mail().clear()



    # def after_navigate_to(self, url, driver):
    #     print("After navigate to %s" % url)