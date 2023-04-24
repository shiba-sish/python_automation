import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class Read_config:
    @staticmethod
    # since we are using static annotation self keyword is not reqq
    def getApplicationurl():
       # fetching the baseURL from the config.ini file
       url=config.get("common info","baseURL")
       return url
    # if we want to read some other data like username from that config.ini file
    @staticmethod
    def getusername():
        username=config.get("common info","username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("common info", "password")
        return password