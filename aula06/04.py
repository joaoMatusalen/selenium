#%%

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.com/aula_06.html'

browser = Firefox()

browser.get(url)
