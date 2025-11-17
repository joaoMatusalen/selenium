#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

def get_next_link():

    links = (browser.find_element(By.TAG_NAME, 'main')
               .find_elements(By.TAG_NAME, 'a'))
    
    link_diabao = 'https://curso-python-selenium.netlify.app/diabao.html'

    for link in links:

        if link == link_diabao:
            next

        return link

#%%

url = "https://curso-python-selenium.netlify.app/exercicio_03.html"

browser = Firefox()
    
browser.get(url)

sleep(1)

for i in range(4):
    get_next_link().click()
    sleep(1)

browser.refresh()
