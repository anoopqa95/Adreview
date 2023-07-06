import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from promodata import id, pass_
import logging


def case2():
    # test_case1
    driver = webdriver.Chrome(executable_path=r"C:\Users\AnoopMishra\Downloads\chromedriver_win32 (2)\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://myintrics.io/")
    # 1.Actual result: User should be able to login applaction
    driver = WebDriverWait(driver, 100)
    driver.until(EC.visibility_of_element_located((By.NAME, "loginfmt"))).send_keys(id)
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']"))).click()
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='i0118']"))).send_keys(pass_)
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']"))).click()
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='KmsiCheckboxField']"))).click()
    driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']"))).click()
    # Login completed
    # 2.Actual result:When the user clicks on the promotion button the two options is coming (Ad review) with the orange color.
    driver.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Collapsed navigation button']"))).click()
    # 3.Actual result:User should be able to click on the Promotion button
    driver.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='nav-option'][normalize-space()='Promotions']"))).click()
    time.sleep(5)
    # 4.Actual result:User should be able to click on the Ad block review
    driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[2]/div[3]/div/a[2]"))).click()
    time.sleep(5)
    # 5.Actual result:User should be able to closed navigation window
    driver.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Collapsed navigation button']"))).click()
    # 6.Actual result:User should be able to select baby product on the department dropdown
    driver.until(EC.visibility_of_element_located((By.XPATH,"/html/body/rd-root/app-ad-block-review/div/div[1]/app-breadcrum/div[2]/div/div/div[1]/div[4]/div/div[2]/div/div/div/rdui-tree-view/kendo-treeview/ul/li[3]/div/kendo-checkbox/input"))).click()
    # 7.Actual result:User should be able to click on the search button and get grid view page
    driver.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Search']"))).click()
    time.sleep(20)















































def test_case2():
    print("When the user clicks on the promotion button the two options is coming (Ad review) with the orange color")
    time.sleep(0.7)


def test_case3():
    print("User should be able to click on the Promotion button")
    time.sleep(2.9)


def test_case4():
    print("User should be able to click on the Ad block review")
    time.sleep(1.6)


def test_case5():
    print("Actual result:User should be able to closed navigation window")
    time.sleep(1.3)


def test_case6():
    print("User should be able to select baby product on the department dropdown")
    time.sleep(2.3)


def test_case7():
    print("User should be able to click on the search button and get grid view page")
    time.sleep(2.3)
    return "Success"
