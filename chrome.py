from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.chrome.options.Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get("http://selenium.dev")

ps = driver.find_elements(By.TAG_NAME, "p")
print(ps[0].text)
print(ps[1].text)
print(ps[2].text)
