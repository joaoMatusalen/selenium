#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


url = 'https://selenium.dunossauro.com/aula_04_b.html'

browser = Firefox()

browser.get(url)

url_parse = urlparse(browser.current_url)
# %%

url_parse.path