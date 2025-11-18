#%%

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.com/aula_05_a.html'

browser = Firefox()

browser.get(url)

browser.find_element(By.ID, 'haskell').text

