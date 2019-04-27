# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, flash, redirect
from utils.query import query

# 创建flask对象
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/course_discussion', methods=['GET', 'POST'])
def course_discussion():
    return render_template('course_discussion.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/news_center', methods=['GET', 'POST'])
def news_center():
    return render_template('news_center.html')


@app.route('/personal_information', methods=['GET', 'POST'])
def personal_information():
    return render_template('personal_information.html')


@app.route('/train_plan', methods=['GET', 'POST'])
def train_plan():
    return render_template('train_plan.html')


if __name__ == '__main__':
    app.run()


