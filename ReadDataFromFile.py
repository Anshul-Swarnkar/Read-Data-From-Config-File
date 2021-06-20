from configparser import ConfigParser

# create object of configparser file
config= ConfigParser()

# to read data from config file
config.read("C:/Users/Dell/PycharmProjects/PythonTutorials/Read Data From Config File/Config.cfg")

print(config.get("Section1","password"))
