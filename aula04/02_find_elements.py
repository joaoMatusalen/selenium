#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

def find_element_by_text(browser, tag, text):
    '''
    Encontrar o elemento com o texto `text`
    
    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...].
        - tag = tag onde o texto será procurado.
        - text = conteúdo que deve estar na tag.
    '''

    elementos = browser.find_elements(By.TAG_NAME, tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento
        
def find_element_by_href(browser, link):
    '''
    Encontrar o `link` do elemento `a`
    
    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...].
        - link = link que estamos procurando na tag `a`.
    '''

    elementos = browser.find_elements(By.TAG_NAME, 'a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento



#%%

url = 'https://selenium.dunossauro.com/aula_04_a.html'

browser = Firefox()

browser.get(url)

sleep(1)

elemento_ddg = find_element_by_text(browser, 'li', 'DuckDuckGo')

link_ddg = find_element_by_href(browser, 'ddg')

print(link_ddg.get_attribute('href'))

browser.quit()


# %%