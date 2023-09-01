from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utilities import ConfigReader


def before_scenario(context,scenario):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))
    context.driver.maximize_window()


def after_scenario(context,scenario):
    context.driver.quit()
