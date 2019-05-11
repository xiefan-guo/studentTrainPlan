from flask import Flask, render_template, request, flash,  jsonify, redirect,url_for,session
from utils import query

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
            print(sql)
            result = query.query(sql)
            print(result)
            if len(result) != 0:
                return u'已经有这个用户了'
            else:
                sql = "INSERT INTO STUDENT VALUES('%s', 'SEX', '%s', 'COLLEGE', 'MAJOR', 'AD_YEAR', '%s', 'ID')" % (user, stu_id, password)
                # print(sql)
                query.update(sql)
                return redirect(url_for('login'))


@app.route('/news_center', methods=['GET', 'POST'])
def news_center():
    sql = "select * from NEWS"
    result = query.query(sql)
    print(result)
    return render_template('news_center.html', result=result)


@app.route('/personal_information', methods=['GET', 'POST'])
def personal_information():
    stu_no = session.get('stu_id')
    print(stu_no + ' is stu_no')
    sql = "SELECT * FROM student WHERE STU_NO = '%s'" % stu_no
    result = query.query(sql)
    return render_template('personal_information.html', result=result)




@app.route('/train_plan', methods=['GET', 'POST'])
def train_plan():
    data = {'name': '数据转换成功', 'children': [{'name': '123123123', 'children': [{'name': 'FlareVis', 'value': 4116, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'scale', 'children': [{'name': 'TimeScale', 'value': 5833, 'categories': 1, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'display', 'children': [{'name': 'DirtySprite', 'value': 8833, 'itemStyle': {'borderColor': 'red'}}]}]}
    return render_template('train_plan.html')


@app.route('/get_info', methods=['GET', 'POST'])
def get_info():
    stu_id = session.get('stu_id')
    print(stu_id)
    sql = "select FINISHED_CO from EDU_STU_PLAN WHERE STU_NO='%s'" % stu_id
    result = query.query(sql)
#    print(result)
    finished_co = result[0][0]
    print(finished_co)

    data = {}
    data['name'] = '总进度'
    children = []

    children1 = {}
    children1['name'] = '思想政治理论'
    children1_list =[]
    children2 = {}
    children2['name'] = '外语'
    children2_list = []
    children3 = {}
    children3['name'] = '文化素质教育必修'
    children3_list = []
    children4 = {}
    children4['name'] = '体育'
    children4_list = []
    children5 = {}
    children5['name'] = '军事'
    children5_list = []
    children6 = {}
    children6['name'] = '健康教育'
    children6_list = []
    children7 = {}
    children7['name'] = '数学'
    children7_list = []
    children8 = {}
    children8['name'] = '物理'
    children8_list = []
    children9 = {}
    children9['name'] = '计算机'
    children9_list = []
    children10 = {}
    children10['name'] = '学科基础'
    children10_list = []
    children11 = {}
    children11['name'] = '专业选修'
    children11_list = []
    aid = 1
    for co in finished_co:
        course_add = {}
        aid_str = str(aid)
        sql = "select CLASSIFICATION, START_TIME, CO_NAME, IS_MUST from education_plan WHERE CO_100='%s'" % aid_str
        co_name = query.query(sql)
        # print(co_name)
        aid = aid + 1
        add_time_list = []
        add_is_list = []

        add_curse = {}
        add_is = {}
        add_time = {}
        if co == '0':
            #print(co_name)
            add_curse['name'] = co_name[0][2]
            add_curse['itemStyle'] = {'borderColor': 'red'}

            add_is['name'] = str(co_name[0][3])
            add_is_list.append(add_curse)
            add_is['children'] = add_is_list
            add_time['name'] = str(co_name[0][1])
            add_time_list.append(add_is)
            add_time['children'] = add_time_list
        else:
            add_curse['name'] = co_name[0][2]
            add_curse['itemStyle'] = {'borderColor': 'green'}
            add_is['name'] = str(co_name[0][3])
            add_is_list.append(add_curse)
            add_is['children'] = add_is_list
            add_time['name'] = str(co_name[0][1])
            add_time_list.append(add_is)
            add_time['children'] = add_time_list


        if co_name[0][0] == '思想政治理论':
            children1_list.append(add_time)
        if co_name[0][0] == '外语':
            children2_list.append(add_time)
        if co_name[0][0] == '文化素质教育必修':
            children3_list.append(add_time)
        if co_name[0][0] == '体育':
            children4_list.append(add_time)
        if co_name[0][0] == '军事':
            children5_list.append(add_time)
        if co_name[0][0] == '健康教育':
            children6_list.append(add_time)
        if co_name[0][0] == '数学':
            children7_list.append(add_time)
        if co_name[0][0] == '物理':
            children8_list.append(add_time)
        if co_name[0][0] == '计算机':
            children9_list.append(add_time)
        if co_name[0][0] == '学科基础':
            children10_list.append(add_time)
        if co_name[0][0] == '专业选修':
            children11_list.append(add_time)

    children1['children'] = children1_list
    children2['children'] = children2_list
    children3['children'] = children3_list
    children4['children'] = children4_list
    children5['children'] = children5_list
    children6['children'] = children6_list
    children7['children'] = children7_list
    children8['children'] = children8_list
    children9['children'] = children9_list
    children10['children'] = children10_list
    children11['children'] = children11_list
    children.append(children1)
    children.append(children2)
    children.append(children3)
    children.append(children4)
    children.append(children5)
    children.append(children6)
    children.append(children7)
    children.append(children8)
    children.append(children9)
    children.append(children10)
    children.append(children11)
    data['children'] = children
    #data = {'name': '数据转换成功', 'children': [{'name': '123123123', 'children': [{'name': 'FlareVis', 'value': 4116, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'scale', 'children': [{'name': 'TimeScale', 'value': 5833, 'categories': 1, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'display', 'children': [{'name': 'DirtySprite', 'value': 8833, 'itemStyle': {'borderColor': 'red'}}]}]}
    print(data)
    return jsonify(data)


@app.route('/submit_train_plan', methods=['GET', 'POST'])
def submit_train_place():
    train_plan = request.get_json(force=True)
    #train_plan['name'] = "数据转换成功"
    print(train_plan)
    data = train_plan['children']
    array_finish = [0]*120
    print(array_finish)
    for data_children in data:
        data_children = data_children['children']
        for data_children_child in data_children:
            name = data_children_child['children'][0]['children'][0]['name']
            color = data_children_child['children'][0]['children'][0]['itemStyle']['borderColor']
            #print(name, color)
            sql = "select CO_100 from education_plan WHERE CO_NAME='%s'" % name
            co_100 = query.query(sql)
            co_100 = co_100[0][0]

            if color == 'red':
                array_finish[int(co_100)] = 0
            else:
                array_finish[int(co_100)] = 1
    finish_co = ''
    for i in range(1, 119):
        if array_finish[i] == 1:
            finish_co += '1'
        else:
            finish_co += '0'
    print(finish_co)
    #print(array_finish)
    sql = "UPDATE edu_stu_plan SET FINISHED_CO='%s'" %finish_co
    query.update(sql)
    return jsonify(train_plan)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)

