from base import TestBase
import unittest
import time


class TestRegistrationForm(TestBase):
    def test_1_contact(self):

        full_company_name = self.driver.find_element_by_id("user_register_company_name")
        full_company_name.send_keys("testowa nazwa")

        email = self.driver.find_element_by_id("user_register_email")
        email.send_keys("test@test.pl")

        name_and_surname = self.driver.find_element_by_id("user_register_name")
        name_and_surname.send_keys("test testerski")

        phone_country = self.driver.find_element_by_id("user_register_phoneCode")
        phone_country.click()

        phone_poland = self.driver.find_element_by_xpath("//option[contains(text(),'(+48) Polska')]")
        phone_poland.click()

        phone_number = self.driver.find_element_by_id("user_register_phone")
        phone_number.send_keys("123456789")

        password = self.driver.find_element_by_id("user_register_plainPassword")
        password.send_keys("testtest")

        regulations_approval = self.driver.find_element_by_id("user_register_settings_agreementRegulations")
        regulations_approval.click()

        data_processing_approval = self.driver.find_element_by_id("user_register_settings_agreementPersonalData")
        data_processing_approval.click()

        register_button = self.driver.find_element_by_id("user_register_submit")
        register_button.click()
        time.sleep(1)

        registration_message = self.driver.find_element_by_xpath("//div[@class='ui success message']").text
        self.assertEqual(registration_message, "OK - some registration logic is mocked")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)