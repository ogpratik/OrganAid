from flask import Flask,render_template,session,request,redirect,url_for,flash
from flaskext.mysql import MySQL
import matplotlib.pyplot as plt
import numpy as np


mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root@404'
app.config['MYSQL_DATABASE_DB'] = 'DBMS_PROJECT'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
mycursor = mysql.connect().cursor()

conn = mysql.connect()
conn.autocommit(True)




