import configparser

import pytest

config = configparser.RawConfigParser()

config.read("D:\\Software Testing\\TK OrangeHRM\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def geturl():
        url = config.get("common info","Url")
        return url

    @staticmethod
    def getUsername():
        Username = config.get("common info", "Username")
        return Username

    @staticmethod
    def getPassword():
        Password = config.get("common info", "Password")
        return Password

    @staticmethod
    def searchItem():
        Search = config.get("common info","Search")
        return Search