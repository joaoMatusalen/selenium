#%%

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.com/aula_06_a.html'

browser = Firefox()

browser.get(url)

#%%

# Usando - Atributo Type
nome = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
senha = browser.find_element(By.CSS_SELECTOR, '[type="password"]')
btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

nome.send_keys('Joao')
senha.send_keys('12345')
btn.click()

#%%

# Outras formas de procurar os elementos - Atributo Name
nome = browser.find_element(By.CSS_SELECTOR, '[name="nome"]')
senha = browser.find_element(By.CSS_SELECTOR, '[name="senha"]')
btn = browser.find_element(By.CSS_SELECTOR, '[name="l0c0"]')

nome.send_keys('Joao')
senha.send_keys('12345')
btn.click()


