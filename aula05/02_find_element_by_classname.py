#%%

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.com/aula_05_b.html'

browser = Firefox()

browser.get(url)

#%%
topico = browser.find_element(By.CLASS_NAME, 'topico').text

linguagens = browser.find_elements(By.CLASS_NAME, 'linguagens')

linguagens[2].text