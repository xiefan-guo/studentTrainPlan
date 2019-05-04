# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, flash,  jsonify, redirect,url_for,session
from utils import query
import os
# 创建flask对象
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gsolvit'

@app.route('/index', methods=['GET', 'POST'])
def index():
    hello=session.get('stu_id')
    print(hello+'session')
    return render_template('index.html')


@app.route('/course_discussion', methods=['GET', 'POST'])
def course_discussion():
    return render_template('course_discussion.html')


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        stu_id = request.form.get('stu_id')
        password = request.form.get('password')
        sql = "select * from STUDENT where STU_NO = '%s'" % stu_id
        result = query.query(sql)
        print(result)
        if len(result) != 0:
            #print(result[0][6], password)
            if result[0][6] == password:
                session['stu_id'] = result[0][2]
                session.permanent=True
                return redirect(url_for('index'))
            else:
                return u'账号或密码错误'
        else:
            return u'不存在这个用户'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        stu_id = request.form.get('stu_id')
        user = request.form.get('user')
        password = request.form.get('password')
        password1 = request.form.get('password1')
        print(stu_id, user, password, password1)

        if(password1 != password):
            return u'两次输入密码不同，请检查'
        else:
            sql = "select * from STUDENT where STU_NO = '%s'" % stu_id
            print(sql)
            result = query.query(sql)
            print(result)
            if len(result) != 0:
                return u'已经有这个用户了'
            else:
                sql = "INSERT INTO STUDENT VALUES('%s', 'SEX', '%s', 'COLLEGE', 'MAJOR', 'AD_YEAR', '%s', 'ID')" % (user, stu_id, password)
                print(sql)
                query.update(sql)
                return redirect(url_for('login'))


@app.route('/news_center', methods=['GET', 'POST'])
def news_center():
    return render_template('news_center.html')


@app.route('/personal_information', methods=['GET', 'POST'])
def personal_information():
    return render_template('personal_information.html')








@app.route('/train_plan', methods=['GET', 'POST'])
def train_plan():
    data = {'name': '我的课程', 'children': [{'name': '123123123', 'children': [{'name': 'FlareVis', 'value': 4116, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'scale', 'children': [{'name': 'TimeScale', 'value': 5833, 'categories': 1, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'display', 'children': [{'name': 'DirtySprite', 'value': 8833, 'itemStyle': {'borderColor': 'red'}}]}]}
    return render_template('train_plan.html')

@app.route('/get_info', methods=['GET', 'POST'])
def get_info():
    data = {'name': '数据转换成功', 'children': [{'name': '123123123', 'children': [{'name': 'FlareVis', 'value': 4116, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'scale', 'children': [{'name': 'TimeScale', 'value': 5833, 'categories': 1, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'display', 'children': [{'name': 'DirtySprite', 'value': 8833, 'itemStyle': {'borderColor': 'red'}}]}]}
    print(data)
    return jsonify(data)

@app.route('/submit_train_plan', methods=['GET', 'POST'])
def submit_train_place():
    train_plan = request.get_json(force=True)
    train_plan['name'] = "数据转换成功"
    print(train_plan)
    return jsonify(train_plan)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)


