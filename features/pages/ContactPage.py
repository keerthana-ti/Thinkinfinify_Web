import time

from features.pages.BasePage import BasePage
import logging

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='login_Page.log', level='INFO', format=log_format)


class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Element xpath values
    contact_page_xpath = "//a[contains(text(), 'Contact')]"
    name_xpath = "//input[@id = 'userName']"
    email_xpath = "//input[@id = 'email']"
    phone_xpath = "//input[@id = 'phoneno']"
    register_option_xpath = "//button[@type='button']"

    # Navigation to contact page
    def contact_page_nav(self):
        self.click_on_element("contact_page_xpath", self.contact_page_xpath)
        logging.info("Contact page launched")

    # Enters name
    def enter_name(self, name):
        self.sendText("name_xpath", self.name_xpath, name)
        logging.info("Name entered")

    # Enters email
    def enter_email(self, email):
        self.sendText("email_xpath", self.email_xpath, email)
        logging.info("Email entered")

    # Enters phone number
    def enter_phone(self, phone):
        self.sendText("phone_xpath", self.phone_xpath, phone)
        logging.info("Phone number entered")
        time.sleep(10)

    # Clicks submit button
    def click_submit(self):
        self.scroll_To("register_option_xpath", self.register_option_xpath)
        self.click_on_element("register_option_xpath", self.register_option_xpath)
        logging.info("Submit button clicked")

