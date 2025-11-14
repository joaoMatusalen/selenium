#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://selenium.dunossauro.com/aula_04_a.html'

browser = Firefox()

browser.get(url)

sleep(1)

#browser.quit()
# %%