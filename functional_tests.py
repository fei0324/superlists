from selenium import webdriver

browser = webdriver.Chrome("C:/Users/fl783/Downloads/chromedriver_win32/chromedriver")
browser.get('http://localhost:8000')

assert 'Django' in browser.title