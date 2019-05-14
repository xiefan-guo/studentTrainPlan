from flask import Flask, render_template, request, flash,  jsonify, redirect, url_for, session
from utils import query
import json
import os
# 创建flask对象
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gsolvit'

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/course_discussion', methods=['GET', 'POST'])
def course_discussion():
    if request.method == 'GET':
        return render_template('course_discussion.html')
    else:
        topic = request.form.get('topic')
        comments = request.form.get('comments')
        commenter = request.form.get('commenter')
        # print(len(topic))
        # print('course_discussion')
        # print(topic, commenter, comments)
        sql = "INSERT INTO NEWS(TOPIC, COMMENTS, COMMENTER) VALUES ('%s', '%s', '%s')" % (topic, comments, commenter)
        print(sql)
        query.update(sql)
        return redirect(url_for('news_center'))

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
            #print(sql)
            result = query.query(sql)
            #print(result)
            if len(result) == 0:
                return u'没有这个用户了'
            else:
                if result[0][6] == user:
                    sql = "UPDATE student SET PASSWORD='%s' WHERE STU_NO='%s'" % (password, stu_id)
                    query.update(sql)
                    return redirect(url_for('login'))
                else:
                    return u'密码错误'

@app.route('/news_center', methods=['GET', 'POST'])
def news_center():
    sql = "select * from NEWS"
    result = query.query(sql)
    print(result)
    return render_template('news_center.html', result=result)

@app.route('/recommed', methods=['GET', 'POST'])
def recommed():
    return render_template('recommed.html')

@app.route('/personal_information', methods=['GET', 'POST'])
def personal_information():
    """
    功能(个人中心界面): 根据"stu_id"从数据库中得到学生基本信息，用于个人中心信息显示
    :return:
    """
    stu_no = session.get('stu_id')
    print(stu_no + ' is stu_no')
    sql = "SELECT * FROM student WHERE STU_NO = '%s'" % stu_no
    result = query.query(sql)
    return render_template('personal_information.html', result=result)

@app.route('/train_plan', methods=['GET', 'POST'])
def train_plan():
    return render_template('train_plan.html')

@app.route('/get_info', methods=['GET', 'POST'])
def get_info():
    """
    功能(培养计划界面): 初始进入培养计划界面，根据stu_id从数据库中得到数据并将其转换为计划树所需json格式数据
    :return: planTree:(json) 计划树所需数据
    """
    stu_id = session.get('stu_id')
    planTree = query.getPlanTreeJson(stu_id)
    return jsonify(planTree)

@app.route('/submit_train_plan', methods=['GET', 'POST'])
def submit_train_place():
    """
    功能1：实现数据库学生选课信息的更新
    功能2: 实现计划树以及进度条的提交更新。
    :return:
    """
    """功能1："""
    train_plan = request.get_json(force=True)
    stu_id = session.get('stu_id')
    query.updateDatabase(stu_id, train_plan)

    """功能2："""
    train_plan_str = json.dumps(train_plan)
    train_plan_str = train_plan_str.replace("yellow", "green")
    train_plan = json.loads(train_plan_str)
    return jsonify(train_plan)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)

