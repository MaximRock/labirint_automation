import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

# from abstract.selenium_listener import MyListener
from pom.home_page import HomePage
from settings import my_code


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--windows-size=800,600')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver: WebDriver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    # driver = EventFiringWebDriver(driver, MyListener())
    url = 'https://www.labirint.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def auth_my_maze(setup):
    auth_page = HomePage(setup)
    auth_page.get_discount_phone_mail(my_code)
    auth_page.get_button_sig_in().click()
    auth_page.sleep()



