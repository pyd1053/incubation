from flask import Flask
app = Flask(__name__)

import taxFileRead
import os

@app.route('/')
def hello():
    return '<h1>Hello Totoro1241241231233!</h1>'

@app.route('/readTaxFile')
def readTaxFile():
    path = 'C:\\Users\\Petter\\Desktop\\彭寅冬\\疫情期间工作\\20200202\\承运公司'
    for filename in getFileList(path):
        taxFileRead.insertIntoDB(path + '\\' + filename)
    return 'success'

def getFileList(p):
    p = str(p)
    if p == "":
        return []
    p = p.replace("/", "\\")
    if p[-1] != "\\":
        p = p + "\\"
    a = os.listdir(p)
    b = [x for x in a if os.path.isfile(p + x)]
    return b
