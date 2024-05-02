from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("file:///Users/liranreznik/Downloads/tip_calc/index.html")
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
s = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]")
s.click()
s = driver.find_element(by="xpath", value="//*[@id=\"musiclvl\"]/option[1]")
s.click()
s = driver.find_element(by="xpath", value="//*[@id=\"peopleamt\"]")
s.send_keys("5")
s = driver.find_element(by="xpath", value="//*[@id=\"calculate\"]")
s.click()
actual = driver.find_element(by="id", value="tip").text
expected = "7.00"
if expected == actual:
    print("Test is done and it works")
else:
    print("Test have been failed")

sleep(5)
driver.close()
