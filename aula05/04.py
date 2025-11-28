#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.com/aula_05.html'

browser = Firefox()

browser.get(url)

def preeche_form(browser, nome, email, senha, telefone):
    browser.find_element(By.NAME, 'nome').send_keys(nome)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'senha').send_keys(senha)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'btn').click()