#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import ast

def preencher_form(browser, nome, email, senha, telefone):

    browser.find_element(By.ID, 'nome').send_keys(nome)
    browser.find_element(By.ID, 'email').send_keys(email)
    browser.find_element(By.ID, 'senha').send_keys(senha)
    browser.find_element(By.ID, 'telefone').send_keys(telefone)

    browser.find_element(By.ID, 'btn').click()

def transform_url(browser):

    resultados = browser.current_url.replace('%40', '@').split('?')[-1].split('&')
    resultado_url = {}

    for resultado in resultados:
        dict = resultado.split('=')
        resultado_url.update({dict[0]:dict[-1]})

    return resultado_url


#%%

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_04.html'

browser.get(url)

sleep(1)

preencher_form(browser, 'Joao', 'joao@email.com', '12345652', '55987654321')

sleep(1)

resulado_textArea = ast.literal_eval(browser.find_element(By.TAG_NAME, 'textarea').text)

resultado_url = transform_url(browser)

resultado_url.popitem()

print(resulado_textArea == resultado_url)
print(resulado_textArea, resultado_url)
