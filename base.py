import unittest
from selenium import webdriver


class TestBase(unittest.TestCase):

    chrome = True
    site = "https://dev-1.clicktrans.pl/register-test/courier"

    def setUp(self):

        if self.chrome:
            self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        else:
            self.driver = webdriver.Firefox(executable_path='../drivers/geckodriver.exe')

        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.site)

    def tearDown(self):
        self.driver.quit()