#Crie um programa com selenium que:
#   ● Jogue o jogo
#   ● Quando você ganhar o script deve parar de ser executado

#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

browser = Firefox()

browser.get(url)

sleep(1)

clique_aqui = browser.find_element(By.TAG_NAME, 'a')

elementos = browser.find_elements(By.TAG_NAME, 'p')

numeroEsperado = int(elementos[1].text.split(":")[-1])

while True:
    clique_aqui.click()

    resposta = int(browser.find_elements(By.TAG_NAME, 'p')[-1]
                           .text
                           .split(":")[-1]
                    )
    
    if resposta == numeroEsperado:
        print(f'Parabéns você ganhou! O número esperado: {numeroEsperado} é igual a reposta {resposta}.')
        break

    print(f'O número esperado {numeroEsperado} é diferente de {resposta}, clique de novo.')    

    
browser.quit()

#%%
