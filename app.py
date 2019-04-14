# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, flash, redirect
import pymysql
from model import config

# 创建flask对象
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    db = pymysql.connect('localhost', 'root', config['MYSQL_PASSWORD'], config['DATABASE_NAME'], charset='utf8')
    cur = db.cursor()
    sql = 'select * from student'
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    db.commit()
    cur.close()
    db.close()
    return render_template('index.html')



if __name__ == '__main__':
    app.run()


import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gsolvit'

    @staticmethod
    def init_app(app):
        pass


config = {
    'default': Config,
    'MYSQL_PASSWORD': '123456',
    'DATABASE_NAME': 'studentTrainPlan'
}
