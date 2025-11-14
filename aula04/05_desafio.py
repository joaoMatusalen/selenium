#%%
"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://selenium.dunossauro.com/aula_04.html'

browser = Firefox()

browser.get(url)

sleep(1)

def get_links(browser, elemento:str):

    """
    Pega todos os links dentro de um elemento

    - browser = a instância do navegador
    - element = webelement [aside, main, body, ul, ol]
    """

    links = (browser.find_element(By.TAG_NAME, elemento)
                         .find_elements(By.TAG_NAME, 'a'))

    dict_links = {}

    for link in links:
        dict_links[link.text] = link.get_attribute('href')

    return dict_links

aulas_links = get_links(browser, 'aside')
exercicios_links = get_links(browser, 'main')

browser.get(exercicios_links['Exercício 3'])

#%%
