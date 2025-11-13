#%%

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep


def click_in_all_elements(browser, tag):
    '''
    Clica em todos os elementos pela `tag` informada.
    
    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...].
        - tag = `tag` onde o texto será procurado.
    '''

    elementos = browser.find_elements(By.TAG_NAME, tag)

    for elemento in elementos:
        sleep(0.3)
        elemento.click()
        
#%%

url = 'https://selenium.dunossauro.com/aula_04_b.html'

browser = Firefox()

browser.get(url)

sleep(1)
 
click_in_all_elements(browser, "div")

for i in range(4):
    sleep(0.3)
    browser.back()

for i in range(4):
    sleep(0.3)
    browser.forward()

