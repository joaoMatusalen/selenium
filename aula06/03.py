#%%

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.com/aula_06_a.html'

browser = Firefox()

browser.get(url)

#%%

browser.find_elements(By.CSS_SELECTOR, 'div.form-group + br')