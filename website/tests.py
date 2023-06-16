from django.test import TestCase
from selenium import webdriver
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager



driver = Firefox(executable_path=GeckoDriverManager().install())
driver.get(url='http://127.0.0.1:8000/admin')


# Create your tests here.

def website_responsiveness(w,file):
    height = 768
    driver.set_window_size(w,height)
    driver.save_screenshot(file)

website_responsiveness(600, "test600.png")
# Create your tests here.
