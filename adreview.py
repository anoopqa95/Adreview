import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from promodata import id, pass_
import logging

#pytest.mark.smoke
driver = webdriver.Chrome(executable_path=r"C:\Users\AnoopMishra\Downloads\chromedriver_win32 (2)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://myintrics.io/")
#1.Actual result: User should be able to login applaction
driver = WebDriverWait(driver, 100)
driver.until(EC.visibility_of_element_located((By.NAME, "loginfmt"))).send_keys(id)
driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']"))).click()
driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='i0118']"))).send_keys(pass_)
driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']"))).click()
driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='KmsiCheckboxField']"))).click()
driver.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']"))).click()
#Login completed
#2.Actual result:When the user clicks on the promotion button the two options is coming (Ad review) with the orange color.
driver.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Collapsed navigation button']"))).click()
#3.Actual result:User should be able to click on the Promotion button
driver.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='nav-option'][normalize-space()='Promotions']"))).click()
time.sleep(5)
#4.Actual result:User should be able to click on the Ad block review
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[2]/div[3]/div/a[2]"))).click()
time.sleep(5)
#4.Actual result:User should be able to closed navigation window
driver.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Collapsed navigation button']"))).click()
#8.Actual result:User should be able to select baby product on the department dropdown
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-block-review/div/div[1]/app-breadcrum/div[2]/div/div/div[1]/div[4]/div/div[2]/div/div/div/rdui-tree-view/kendo-treeview/ul/li[3]/div/kendo-checkbox/input"))).click()
#9.Actual result:User should be able to click on the search button and get grid view page
driver.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Search']"))).click()
time.sleep(20)
#10.Actual result:User should be able to select list view button
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[3]/div/div[2]/app-view-buttons/div/span[2]"))).click()
time.sleep(2)
#11.Actual result:User should be able to open product page
driver.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/rd-root[1]/app-ad-block-review[1]/div[1]/div[3]/div[1]/div[3]/app-list-view[1]/div[1]/rdui-grid[1]/div[1]/kendo-grid[1]/div[1]/kendo-grid-list[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/a[1]"))).click()
time.sleep(30)






