import pymysql
import os

class DB():

    def getConn(self):
        return pymysql.connect('192.168.5.61', 'root', '123456', 'pyd')