from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#Test objective: This test case will go through the women solid tops items, proceed with the checkout and filling both billing address and credit card information

driver = webdriver.Firefox();
driver.maximize_window()
wait = WebDriverWait(driver, timeout=8)

#Removing the Pop-ups and changing language to english
driver.get("https://www.uniformadvantage.com/")
driver.implicitly_wait(5)
driver.find_element(By.ID, 'globalePopupWrapper').click()
driver.find_element(By.CLASS_NAME, 'ltkpopup-close-button').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'English').click()

#Selecting the item
time.sleep(4)
menu = driver.find_element(By.XPATH, '//html/body/div[3]/header/div/div/div/div[4]/div/nav/div[2]/ul/li[1]/a')
ActionChains(driver).move_to_element(menu).perform()
time.sleep(4)
driver.find_element(By.LINK_TEXT, 'Solid Tops').click()
driver.find_element(By.CSS_SELECTOR, '.image-pdp-link').click()
driver.find_element(By.XPATH, '//html/body/div[3]/div[4]/div[1]/div[3]/div[4]/div[2]/div[3]/div[2]/div/div/div[3]/button[4]/span').click()
time.sleep(8)

#Proceeding with the checkout
buybutton = driver.find_element(By.XPATH, '//html/body/div[3]/div[4]/div[1]/div[3]/div[4]/div[2]/div[3]/div[8]/div/div/div[1]/div[2]/button')
driver.execute_script("arguments[0].click();", buybutton)
time.sleep(8)
driver.find_element(By.XPATH, '//html/body/div[14]/div/div/div[2]/div/div[3]/a').click()
driver.find_element(By.XPATH, '//html/body/div[3]/div[4]/div[6]/div[1]/div[2]/div/div[1]/div[2]/div[6]/div/div/div/a').click()
driver.find_element(By.XPATH, '//html/body/div[3]/div[4]/div[1]/div/div[1]/div/div[2]/a').click()

#Filling billing information
time.sleep(13)
frame = driver.find_element(By.ID, 'Intrnl_CO_Container')
driver.switch_to.frame(frame)
driver.find_element(By.ID, 'CheckoutData_BillingFirstName').send_keys("Claude")
driver.find_element(By.ID, 'CheckoutData_BillingLastName').send_keys("Schlosser")
driver.find_element(By.ID, 'CheckoutData_Email').send_keys("claudeschlosser21@gmail.com")
countryid = Select(driver.find_element(By.ID, 'BillingCountryID'))
countryid.select_by_visible_text('United States')
driver.find_element(By.ID, "CheckoutData_BillingAddress1").send_keys("12500 E 86th St N #101")
driver.find_element(By.ID, "CheckoutData_BillingAddress2").send_keys("706 N Lynn Riggs Blvd")
driver.find_element(By.ID, "BillingCity").send_keys("Owasso")
driver.find_element(By.ID, "BillingZIP").send_keys("74055")
driver.find_element(By.ID, "CheckoutData_BillingPhone").send_keys("(918) 274-0931")
state = Select(driver.find_element(By.ID, 'BillingStateID'))
state.select_by_visible_text('Oklahoma')

#Filling credit card information
iframe = driver.find_element(By.ID, 'secureWindow')
driver.switch_to.frame(iframe)
driver.find_element(By.ID, "cardNum").send_keys("4111 1111 1111 1111")
expmonth = Select(driver.find_element(By.ID, 'cardExpiryMonth'))
expmonth.select_by_value('10')
expyear = Select(driver.find_element(By.ID, 'cardExpiryYear'))
expyear.select_by_value('2025')
driver.find_element(By.ID, "cvdNumber").send_keys("123")
#Test case finished.
