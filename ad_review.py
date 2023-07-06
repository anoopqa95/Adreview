import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from promodata import id, pass_
import logging
def case1():
    #test_case1
    print("success")
    logging.info("This is a log message")
    driver = webdriver.Chrome(executable_path=r"C:\Users\AnoopMishra\Downloads\chromedriver_win32 (2)\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://myintrics.io/")
    driver = WebDriverWait(driver, 100)
    driver.until(EC.visibility_of_element_located((By.NAME, "loginfmt"))).send_keys(id)
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']"))).click()
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='i0118']"))).send_keys(pass_)
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']"))).click()
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='KmsiCheckboxField']"))).click()
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']"))).click()
    print('User should be able to login promo applaction')
    return driver
    #test_case2

def test_case(driver):
    driver.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Collapsed navigation button']"))).click()
    print('hello')
    test_case3
    driver.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='nav-option'][normalize-space()='Promotions']"))).click()
    # test_case4
    driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[2]/div[3]/div/a[1]"))).click()
    time.sleep(10)
    # test_case5
    driver.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Collapsed navigation button']"))).click()
    # test_case6
    driver.until(EC.visibility_of_element_located((By.XPATH, "//rdui-option[@checked='checked']//input[@name='undefined']"))).click()
    # test_case7
    driver.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Search']"))).click()
    #time.sleep(120)
    # test_case8
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='350251']"))).click()
    # test_case9
    driver.until(EC.visibility_of_element_located((By.XPATH, "//label[@class='download-text']"))).click()
    # test_case10
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='fileName']"))).send_keys("intricsindia")
    #test_case11
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='defaultDataCheck']"))).click()
    #test_case12
    driver.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Download']"))).click()
    #time.sleep(10)
    #test_case14
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='350251']"))).click()
    driver.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='view_headline']"))).click()
    driver.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/rd-root[1]/app-ad-review[1]/div[1]/div[3]/div[1]/div[3]/app-list-view[1]/div[1]/rdui-grid[1]/div[1]/kendo-grid[1]/div[1]/kendo-grid-list[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[8]/div[1]/a[1]/img[1]"))).click()
    time.sleep(20)














































#def test_case2():
    #print("When the user clicks on the promotion button the two options is coming (Ad review) with the orange color")
    #time.sleep(5)
# def test_case3():
#     print("User should be able to click on the Ad review link")
#     time.sleep(3.2)
#
# def test_case4():
#     print("User should be able to open navigation button")
#     time.sleep(2.6)
#
# def test_case5():
#     print("User should be able to select date input on the search page")
#     time.sleep(1.9)
#
# def test_case6():
#     print("User should be able to click search button and get data on the grid")
#     time.sleep(3.3)
#
# def test_case7():
#     print("User should be able to select single selection of checkbox in single circular")
#     time.sleep(1.2)
#
# def test_case8():
#     print("User should be able to click on the download button and download pop-up should be open")
#     time.sleep(1)
#
# def test_case9():
#     print("User should be able to fill download filename")
#     time.sleep(1.8)
#
# def test_case10():
#     print("User should be able to uncheck data icon in download pop-up window")
#     time.sleep(1.9)
#
# def test_case11():
#     print("User should be able to click on the download button and get download file")
#     time.sleep(2.1)
#
# def test_case12():
#     print("User should be able to unselect single circular on the ad review page")
#     time.sleep(1.4)
#
# def test_case13():
#     print("User should be able to click on the list view page")
#     time.sleep(1)
#
# def test_case14():
#     print("User should be able to open view ad details page")
#     time.sleep(1.8)
#
