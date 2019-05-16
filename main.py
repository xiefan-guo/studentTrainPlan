from flask import Flask, render_template, request, flash,  jsonify, redirect, url_for, session
from utils import query, map_student_course, recommed_module
import json
import time
import os
# 创建flask对象
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gsolvit'


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/manager', methods=['GET', 'POST'])
def manager():
    sql = "select * from STUDENT"
    result = query.query(sql)
    return render_template('manager.html', result=result)


@app.route('/managerAdd', methods=['GET', 'POST'])
def managerAdd():
    stu_id = session.get('stu_id')
    #print(stu_id)
    if stu_id == 'admin':
        if request.method == 'GET':
            #print('1111')
            return  render_template('managerAdd.html')
        else:
            #print('222')
            name = request.form.get('name')
            sex = request.form.get('sex')
            stu_no = request.form.get('stu_no')
            college = request.form.get('college')
            major = request.form.get('major')
            ad_year = request.form.get('ad_year')
            password = request.form.get('password')
            sql="INSERT INTO STUDENT VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (name,sex,stu_no,college,major,ad_year,password,stu_no)
            #print(sql)
            query.update(sql)
            return redirect(url_for('manager'))
    else:
        return u'页面不存在'


@app.route('/managerDelete', methods=['GET', 'POST'])
def managerDelete():
    stu_id = session.get('stu_id')
    #print(stu_id)
    if stu_id == 'admin':
        if request.method == 'GET':
            #print('1111')
            return render_template('managerDelete.html')
        else:
            #print('222')
            stu_no = request.form.get('stu_no')
            sql="DELETE FROM STUDENT WHERE STU_NO='%s'" % stu_no
            #print(sql)
            query.update(sql)
            return redirect(url_for('manager'))
    else:
        return u'页面不存在'


@app.route('/managerEdit', methods=['GET', 'POST'])
def managerEdit():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('managerEdit.html')
        else:
            stu_no = request.form.get('stu_no')
            name = request.form.get('name')
            sex = request.form.get('sex')
            college = request.form.get('college')
            major = request.form.get('major')
            ad_year = request.form.get('ad_year')
            password = request.form.get('password')

            sql="select * from STUDENT WHERE STU_NO='%s'" % stu_no
            result=query.query(sql)
            if name=='':
                name=result[0][0]
            if sex=='':
                sex=result[0][1]
            if college=='':
                college=result[0][3]
            if major=='':
                major=result[0][4]
            if ad_year=='':
                ad_year=result[0][5]

            sql="UPDATE STUDENT SET NAME='%s',SEX='%s',COLLEGE='%s',MAJOR='%s',AD_YEAR='%s',PASSWORD='%s',ID='%s' WHERE STU_NO='%s'" % (name, sex, college, major, ad_year, password, stu_no, stu_no)
            #print(sql)
            query.update(sql)
            return redirect(url_for('manager'))
    else:
        return u'页面不存在'


@app.route('/course_discussion', methods=['GET', 'POST'])
def course_discussion():
    if request.method == 'GET':
        return render_template('course_discussion.html')
    else:
        topic = request.form.get('topic')
        comments = request.form.get('comments')
        #commenter = request.form.get('commenter')
        # print(len(topic))
        # print('course_discussion')
        # print(topic, commenter, comments)
        stu_id = session.get('stu_id')
        sql = "select NAME from STUDENT where STU_NO = '%s'" % stu_id
        stu_name = query.query(sql)
        stu_name = stu_name[0][0]
        now = time.time()
        now = time.strftime('%Y-%m-%d', time.localtime(now))
        now = str(now)
        news_id = stu_name + now
        sql = "INSERT INTO NEWS(TOPIC, COMMENTS, COMMENTER, NEWS_ID, IS_FIRST) VALUES ('%s', '%s', '%s', '%s', '0')" % (topic, comments, stu_name, news_id)
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
                if stu_id=='admin':
                    return redirect(url_for('manager'))
                else:
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
    sql = "select * from NEWS WHERE IS_FIRST='0'"
    result = query.query(sql)
    print(result)
    return render_template('news_center.html', result=result)


@app.route('/detail/<question>', methods=['GET', 'POST'])
def detail(question):
    print(question)
    #question=str(question)
    if request.method=='GET':
        sql="SELECT TOPIC, COMMENTS, COMMENTER, CREATE_TIME FROM NEWS WHERE NEWS_ID='%s'" % question
        title=query.query(sql)
        #print(title)
        title=title[0]
        sql="SELECT * FROM NEWS WHERE IS_FIRST='%s'" % question
        result=query.query(sql)
        return render_template('detail.html', title=title, result=result)
    else:
        comments = request.form.get('comments')
        stu_id = session.get('stu_id')
        sql = "select NAME from STUDENT where STU_NO = '%s'" % stu_id
        stu_name = query.query(sql)
        stu_name = stu_name[0][0]
        now = time.time()
        now = time.strftime('%Y-%m-%d', time.localtime(now))
        now = str(now)
        news_id = stu_name + now
        sql = "INSERT INTO NEWS(TOPIC, COMMENTS, COMMENTER, NEWS_ID, IS_FIRST) VALUES ('回复', '%s', '%s', '%s', '%s')" % (comments, stu_name, news_id,question)
        print(sql)
        query.update(sql)

        sql = "SELECT TOPIC, COMMENTS, COMMENTER, CREATE_TIME FROM NEWS WHERE NEWS_ID='%s'" % question
        title = query.query(sql)
        # print(title)
        title = title[0]
        sql = "SELECT * FROM NEWS WHERE IS_FIRST='%s'" % question
        result = query.query(sql)
        return render_template('detail.html', title=title, result=result)


@app.route('/recommed', methods=['GET', 'POST'])
def recommed():
    return render_template('recommed.html')

@app.route("/getRecommedData", methods=['GET','POST'])
def getRecommedData():
    stu_no = session.get('stu_id')
    id2Student, id2Course, stuNo2MatId = map_student_course.get_map_student()
    scoreMatrix = map_student_course.get_matrix(id2Student)
    """
    函数，recommedCourse：使用SVD进行课程推荐：
    返回:(课程1ID， 课程1评分)
    """
    topNCourse, topNStudent = recommed_module.recommedCoursePerson(scoreMatrix, stuNo2MatId[stu_no], N=20)
    """
    将得到的Course与Person装换为前端图标需要的json格式:
     {
        "source": [
            [2.3, "计算机视觉"],
            [1.1, "自然语言处理"],
            [2.4, "高等数学"],
            [3.1, "线性代数"],
            [4.7, "计算机网络"],
            [5.1, "离散数学"]
        ]
     }   
    """

    id2Student = {i:id2Student[i][0] for i in id2Student.keys()}
    print(id2Student)
    print(id2Course)
    courseJson = recommed_module.toBarJson(topNCourse, id2Course)
    personJson = recommed_module.toBarJson(topNStudent, id2Student)
    courseJson = recommed_module.regularData(courseJson, 1, 5)
    personJson = recommed_module.regularData(personJson, 0, 1)

    coursePersonJson = {}
    coursePersonJson['course'] = courseJson
    coursePersonJson['person'] = personJson
    return jsonify(coursePersonJson)

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
    print(planTree)
    return jsonify(planTree)


@app.route('/submit_train_plan', methods=['GET', 'POST'])
def submit_train_place():
    """
    功能1：实现数据库学生选课信息的更新
    功能2: 实现计划树以及进度条的提交更新。
    :return:
    """
    """功能1："""
    twoData = request.get_json(force=True)
    train_plan = twoData['tree']
    scores = twoData['scores']

    #train_plan['name'] = "数据转换成功"
    print('反馈回来的数据是：')
    print(train_plan)
    data = train_plan['children']
    array_finish = [0]*120
    #print(array_finish)
    for data_children in data:
        data_children = data_children['children']
        #print(data_children)
        for data_children_child_1 in data_children:
            #print('data_children_child', data_children_child)
            data_children_child_1 = data_children_child_1['children']
            for data_children_child in data_children_child_1:
                name = data_children_child['children'][0]['name']
                color = data_children_child['children'][0]['itemStyle']['borderColor']
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

    stu_id = session.get('stu_id')
    query.updateDatabase(stu_id, train_plan)
    query.updateScore(stu_id, scores)

    """功能2："""
    train_plan_str = json.dumps(train_plan)
    train_plan_str = train_plan_str.replace("yellow", "green")
    train_plan = json.loads(train_plan_str)
    return jsonify(train_plan)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)

