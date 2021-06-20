#from configparser import ConfigParser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.google.com')

# create object of configparser file
#config= ConfigParser()

# to read data from config file
#config.read("C:/Users/Dell/PycharmProjects/PythonTutorials/Read Data From Config File/Config.cfg")

print(config.get("Section1","password"))
