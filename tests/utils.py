from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def accept_all_cookies(driver):
    """
    Closes cookie message with allowing all cookies

    :param driver: Selenium webdriver
    """
    btn_allow_all_cookies = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/button[1]")
    if btn_allow_all_cookies:
        btn_allow_all_cookies.click()

def move_to_element(driver, element):
    """
    Moves driver to element. Can be used e.g. for hovering above field.

    :param driver: Selenium webdriver
    :param element: WebElement the pointer should go to
    """
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

def solve_reCaptcha(driver):
    """
    TODO / TBD
    Helper method to solve reCaptcha (Google reCaptcha v2)

    :param driver: Selenium webdriver
    """
    pass
