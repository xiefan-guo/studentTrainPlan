# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import  SQLAlchemy

# 创建flask对象
app = Flask(__name__)
# flash 消息闪现 --> 需要加密 secret_key 加密消息的混淆
app.secret_key = 'gsolvit'

# 数据库设计
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.01/studentTrainPlan"

# 配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
# 跟踪数据库修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 获取SQLAlchemy实例对象，接下来就可以使用对象调用数据
db = SQLAlchemy(app)

# 数据库模型
class student(db.Model):
    # 定义表名
    __tablename__ = 'student'

    # 定义字段
    name = db.Column(db.String(255))





@app.route('/', methods=['GET','POST'])
def index():
    url_str = 'baidu.com'
    if request.method == 'POST':
        # 获取用户信息
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 判断填写完整
        # flash 消息闪现 --> 需要加密 secret_key 加密消息的混淆
        if not all([username, password, password2]):
            flash('参数不完整')
        elif password2 != password:
            flash('密码不一致')
        else:
            return 'success'

    return render_template('index.html', url_str=url_str)


if __name__ == '__main__':
    app.run()
