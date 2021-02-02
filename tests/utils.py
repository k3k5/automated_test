from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def accept_all_cookies(driver):
    btn_allow_all_cookies = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/button[1]")
    if btn_allow_all_cookies:
        btn_allow_all_cookies.click()

def move_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()