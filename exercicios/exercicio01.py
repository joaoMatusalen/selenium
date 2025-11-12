# Crie um programa com selenium que:
# ● Gere um dicionário, onde a chave é a tag h1
#    ○ O valor deve ser um novo dicionário
#    ○ cada chave do valor deverá ser o valor de 'atributo'
#    ○ cada valor deve ser o texto contido no elemento

#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep


url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser = Firefox()

browser.get(url)

sleep(1)

elemento = browser.find_elements(By.TAG_NAME, 'p')

atributosNomes = [i.get_attribute('atributo') for i in elemento]

elementoValor = [i.text for i in elemento]

my_dict = {"h1":{}}

for i in range(len(atributosNomes)):
    my_dict["h1"][atributosNomes[i]] = elementoValor[i]


print(my_dict)


browser.quit()

# %%
