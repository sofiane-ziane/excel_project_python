import configparser
config=configparser.RawConfigParser()
config.read("C:\\Users\\ADMIN\\PycharmProjects\\Excel_project\\configurations\\configurate.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('info','URL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('info','password')
        return password

    @staticmethod
    def get_login_title():
        password = config.get('info', 'login_title')
        return password

    @staticmethod
    def get_billing_title():
        password = config.get('info', 'billing_title')
        return password

    @staticmethod
    def get_contact_title():
        password = config.get('info', 'contact_title')
        return password
