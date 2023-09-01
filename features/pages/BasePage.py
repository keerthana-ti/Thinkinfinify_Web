from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Code to get the locator type
    def getLocatorType(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_type.endswith("_tag_name"):
            element = self.driver.find_element(By.TAG_NAME, locator_value)
        return element

    # Code to click on the specific element
    def click_on_element(self, locator_type, locator_value):
        element = self.getLocatorType(locator_type, locator_value)
        element.click()

    # Code to send keys to the specific elements
    def sendText(self, locator_type, locator_value, text_to_enter):
        element = self.getLocatorType(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_enter)

    # Code to is_Element displayed method
    def isElementDisplayed(self, locator_type, locator_value):
        element = self.getLocatorType(locator_type, locator_value)
        return element.is_displayed()

    # Code to scroll to element method
    def scroll_To(self, locator_type, locator_value):
        element = self.getLocatorType(locator_type, locator_value)
        self.driver.execute_script("window.scrollBy(0, 100);")

