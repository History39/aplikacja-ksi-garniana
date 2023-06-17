from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url='http://127.0.0.1:8000/')

# Create your tests here.

def website_responsiveness(width,file):
    height = 768
    driver.set_window_size(width,height)
    driver.save_screenshot(file)

website_responsiveness(900,"test300.png")

# Create your tests here.