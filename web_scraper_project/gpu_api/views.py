from django.http import JsonResponse
# from rest_framework.response import Response
# from rest_framework.views import APIView
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# from .models import GPU
# from .serializers import GPUSerializer

def fetch_gpu_data(request):
    service = Service(executable_path=r'C:\Users\darsh\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        driver.get('https://www.nvidia.com/en-in/geforce/buy/')
        time.sleep(5)

        gpu_elements = driver.find_elements(By.CSS_SELECTOR, 'h3.title')
        gpus = []

        for element in gpu_elements:
            gpu_name = element.text.strip()
            if not gpu_name.startswith('Starting at'):
                gpus.append(gpu_name)
                print(f"{gpu_name}")

        na = [2, 3, 4]
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

        gpu_prices = {}

        for i in range(len(gpus)):
            gpu_prices[gpus[i]] = starting_prices[i]
            print(f"{starting_prices[i]}")
        print(gpu_prices)
        return JsonResponse(gpu_prices)

    except Exception as e:
        driver.quit()
        return JsonResponse({'error': str(e)})
