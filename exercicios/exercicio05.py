#%%
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_05.html'

browser = Firefox()

browser.get(url)


#%%
form_id = browser.find_element(By.CSS_SELECTOR, 'header span').text

#%%
form = browser.find_element(By.CSS_SELECTOR, f"form[class$={form_id}]")
form.find_element(By.NAME, 'nome').send_keys('123')
form.find_element(By.NAME, 'senha').send_keys('123')
form.find_element(By.NAME, form_id).click()

#%%