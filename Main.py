from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servicee = Service(executable_path=r'C:\Users\darsh\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=servicee)

driver.get('https://www.nvidia.com/en-in/geforce/buy/')


time.sleep(5)

# gpus = driver.find_elements(By.CSS_SELECTOR, 'h3.title')

gpus = []

gpu_elements = driver.find_elements(By.CSS_SELECTOR, 'h3.title')
for element in gpu_elements:
    gpu_name = element.text.strip()
    if gpu_name.startswith('Starting at'):
        pass
    else:
        gpus.append(gpu_name)

# print(gpus)

na = [2,3,4]

starting_prices = []
price_elements = driver.find_elements(By.CLASS_NAME, 'startingprice')
for index, element in enumerate(price_elements):
    text = element.text.strip()
    if index in na:
        starting_prices.append("N/A")
    if text.startswith('Starting at'):
        starting_price = text.split('Starting at ')[1].strip()
        starting_prices.append(starting_price)

driver.quit()

# for i in range(len(price_elements)):
#     print(f"Gpu Name: {gpus[i]}\nPrice: {starting_prices[i]}\n")

gpu_prices = {}

for i in range(len(gpus)):
    gpu_name = gpus[i]
    starting_price_text = starting_prices[i]
    gpu_prices[gpu_name] = starting_price_text

print(gpu_prices)