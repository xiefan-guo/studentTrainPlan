# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, flash, redirect
from utils.query import query

# 创建flask对象
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    sql = 'select * from student'
    print(sql)
    result = query(sql)
    print(result)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


