#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.com/aula_05_c.html'

browser = Firefox()

browser.get(url)

def melhor_filme(browser, filme, email, telefone):
    """
    Preenche o formulario com melhor filme na minha opnião na data de hoje.
    """

    browser.find_element(By.NAME, 'filme').send_keys(filme)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)

melhor_filme(browser, 'Senhor das armas', 'joao@123.com', '(055)987654321')

