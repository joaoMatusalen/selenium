#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Firefox()

browser.get(url)

sleep(1)

a = browser.find_element(By.TAG_NAME, 'a')

for click in range(10):
    a.click()
    p = browser.find_elements(By.TAG_NAME, 'p')[-1]
    
print(f'O texto de a: {a.text}')
print(f'O ultimo texto de p: {p.text}')


browser.quit()
# %%