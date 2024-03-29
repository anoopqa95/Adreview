import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from promodata import id, pass_

driver = webdriver.Chrome(executable_path=r"C:\Users\AnoopMishra\Downloads\chromedriver_win32 (2)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://myintrics.io/")
# time.sleep(10)
# Page login
driver = WebDriverWait(driver, 100)

# used to Enter the email_id
driver.until(EC.visibility_of_element_located((By.NAME, "loginfmt"))).send_keys(id)

# used to click on next button
driver.find_element(By.XPATH,
                    "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input").click()

#used to Enter  the pass

driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input"))).send_keys(pass_)

# used to click on next buttion
driver.find_element(By.XPATH,
                    "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input").click()
# used to final Login
driver.find_element(By.XPATH,
                    "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input").click()

driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[1]/div[1]/button/img"))).click()
#time.sleep(1)
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[2]/div[3]/a"))).click()
#time.sleep(1)
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[2]/div[3]/div/a[1]"))).click()
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[1]/div[1]/button/img"))).click()
# Click on the three dot line > Promotion Button
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[1]/div[1]/button/img"))).click()
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[2]/div[3]/a"))).click()
# Click on the Ad review button
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[2]/div[3]/div/a[1]"))).click()
# # Click on the three dot line to come back
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/rdui-menubar/div[1]/div[1]/div[1]/button/img"))).click()
# Click on the search filter button
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[1]/app-breadcrum/div[1]/div/button"))).click()
# Select date Range
driver.until(EC.visibility_of_element_located((By.XPATH, "html/body/rd-root/app-ad-review/div/div[1]/app-breadcrum/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/rdui-option/input"))).click()
# Click on the search button
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[1]/app-breadcrum/div[2]/div/div/div[2]/button[1]/span"))).click()
time.sleep(30)
driver.until(EC.presence_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[3]/div/div[3]/app-grid-view/div[1]/button"))).click()
# time.sleep(10)
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[3]/div/div[3]/app-grid-view/div[1]/button"))).click()
# time.sleep(10)
# Click on the List view window
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[3]/div/div[2]/app-view-buttons/div/span[2]"))).click()
# List view > click on the View Ad details link
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[3]/div/div[3]/app-list-view/div/rdui-grid/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[8]/div/a"))).click()
# Click on the download from the ad details page
time.sleep(30)
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[2]/app-sort/div/div/div/div/div/button/span/label"))).click()
# Enter file name
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[2]/app-sort/rdui-confirm-popup/kendo-dialog/div[2]/div/div/div/ul/li[1]/div[2]/rdui-input/div/div/input"))).send_keys("anoopkumarmishra")
time.sleep(2)
#select data from the dropdown
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[2]/app-sort/rdui-confirm-popup/kendo-dialog/div[2]/div/div/div/ul/li[2]/div[2]/div[2]/rdui-select/div/kendo-dropdownlist/span/span[2]"))).click()
#CLICK ON THE DOWNLOAD BUTTON
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[2]/app-sort/rdui-confirm-popup/kendo-dialog/div[2]/kendo-dialog-actions/div/button[2]/span"))).click()
# Click on the cross button to close download pop-up window
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[2]/app-sort/rdui-confirm-popup/kendo-dialog/div[2]/kendo-dialog-titlebar/div[2]/a"))).click()
#CLICK ON THE Breadcrumbs BUTTON TO GO BACK ON THE PREVIOUS PAGE
driver.until(EC.visibility_of_element_located((By.XPATH, "/html/body/rd-root/app-ad-review/div/div[3]/div/div/app-ad-details/div/rdui-bread-crumb/kendo-breadcrumb/ol/li[1]/div/button"))).click()


