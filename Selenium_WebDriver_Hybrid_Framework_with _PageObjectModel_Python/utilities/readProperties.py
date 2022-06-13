import configparser

config = configparser.RawConfigParser()  #to be used for reading data from .ini file
config.read(".\\Configuration\\config.ini")

class readConfig:

    @staticmethod
    def getApplURL():
        url = config.get('login info', 'base_url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login info', 'password')
        return password

