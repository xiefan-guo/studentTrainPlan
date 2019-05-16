import pymysql
from config import config

def query(sql):
    """
    功能; 使用sql语句查询数据库中学生选课信息.
    参数: sql(string)
    """
    db = pymysql.connect('localhost', 'root', config['MYSQL_PASSWORD'], config['DATABASE_NAME'], charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()

        #print('query success')

        # print('query success')
    except:
        # print('query loss')
        db.rollback()
    cur.close()
    db.close()
    return result


def update(sql):
    """
    功能; 使用sql语句更新数据库中学生选课信息。
    参数: sql(string)
    """
    db = pymysql.connect('localhost', 'root', config['MYSQL_PASSWORD'], config['DATABASE_NAME'], charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
        #print('update success')
        # print('update success')
    except:
        # print('update loss')
        db.rollback()
    cur.close()
    db.close()

def getPlanTreeJson(stu_id):
    """
    功能: 传入学生stu_id,然后利用stu_id从数据库查询得到该学生选课信息，再转换为计划树所需的json格式
    :param stu_id: 唯一标识学生的id号
    :return: 学生选课计划树Json数据
    """
    print(stu_id)
    sql = "select FINISHED_CO from EDU_STU_PLAN WHERE STU_NO='%s'" % stu_id
    result = query(sql)
    print(result)
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

    score = [0.0] * 15

    add_time_list = []
    for j in range(44):
        add_time_list.append([])

    sql="SELECT CO_NO,COMMENT FROM CHOOSE WHERE STU_NO='%s'" % stu_id
    course2score=query(sql)
    co2score = {}
    for cur in course2score:
        co2score[cur[0]] = cur[1]

    #print(co2score)

    for co in finished_co:
        course_add = {}
        aid_str = str(aid)
        sql = "select CLASSIFICATION, START_TIME, CO_NAME, IS_MUST, CREDITS, CO_NO from education_plan WHERE CO_100='%s'" % aid_str
        co_name = query(sql)
        #print('数据库查询结果')
        #print(co_name)
        aid = aid + 1
        add_is_list = []

        add_curse = {}
        add_is = {}

        add_score = float(co_name[0][4])

        if co == '0':
            #print(co_name)
            add_curse['name'] = co_name[0][2]
            add_curse['itemStyle'] = {'borderColor': 'red'}
            add_curse['value'] = add_score
            add_curse['score'] = int(co2score[co_name[0][5]])

            if co_name[0][3] == 1:
                add_is['name'] = '必修'
            else:
                add_is['name'] = '选修'

            add_is_list.append(add_curse)
            add_is['children'] = add_is_list
            # add_time['name'] = str(co_name[0][1])
            # add_time_list.append(add_is)
            # add_time['children'] = add_time_list
        else:
            add_curse['name'] = co_name[0][2]
            add_curse['itemStyle'] = {'borderColor': 'green'}
            add_curse['value'] = add_score
            add_curse['score'] = int(co2score[co_name[0][5]])

            if co_name[0][3] == 1:
                add_is['name'] = '必修'
            else:
                add_is['name'] = '选修'

            add_is_list.append(add_curse)
            add_is['children'] = add_is_list
            # add_time['name'] = str(co_name[0][1])
            # add_time_list.append(add_is)
            # add_time['children'] = add_time_list

        str_co_time = str(co_name[0][1])
        if co_name[0][0] == '思想政治理论':
            if str_co_time[3] == '6':
                add_time_list[0].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[1].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[2].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[3].append(add_is)
        if co_name[0][0] == '外语':
            if str_co_time[3] == '6':
                add_time_list[4].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[5].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[6].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[7].append(add_is)
        if co_name[0][0] == '文化素质教育必修':
            if str_co_time[3] == '6':
                add_time_list[8].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[9].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[10].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[11].append(add_is)
        if co_name[0][0] == '体育':
            if str_co_time[3] == '6':
                add_time_list[12].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[13].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[14].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[15].append(add_is)
        if co_name[0][0] == '军事':
            if str_co_time[3] == '6':
                add_time_list[16].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[17].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[18].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[19].append(add_is)
        if co_name[0][0] == '健康教育':
            if str_co_time[3] == '6':
                add_time_list[20].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[21].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[22].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[23].append(add_is)
        if co_name[0][0] == '数学':
            if str_co_time[3] == '6':
                add_time_list[24].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[25].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[26].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[27].append(add_is)
        if co_name[0][0] == '物理':
            if str_co_time[3] == '6':
                add_time_list[28].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[29].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[30].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[31].append(add_is)
        if co_name[0][0] == '计算机':
            if str_co_time[3] == '6':
                add_time_list[32].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[33].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[34].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[35].append(add_is)
        if co_name[0][0] == '学科基础':
            if str_co_time[3] == '6':
                add_time_list[36].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[37].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[38].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[39].append(add_is)
        if co_name[0][0] == '专业选修':
            if str_co_time[3] == '6':
                add_time_list[40].append(add_is)
            if str_co_time[3] == '7':
                add_time_list[41].append(add_is)
            if str_co_time[3] == '8':
                add_time_list[42].append(add_is)
            if str_co_time[3] == '9':
                add_time_list[43].append(add_is)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[0]
    children1_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[1]
    children1_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[2]
    children1_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[3]
    children1_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[4]
    children2_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[5]
    children2_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[6]
    children2_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[7]
    children2_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[8]
    children3_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[9]
    children3_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[10]
    children3_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[11]
    children3_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[12]
    children4_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[13]
    children4_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[14]
    children4_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[15]
    children4_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[16]
    children5_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[17]
    children5_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[18]
    children5_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[19]
    children5_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[20]
    children6_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[21]
    children6_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[22]
    children6_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[23]
    children6_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[24]
    children7_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[25]
    children7_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[26]
    children7_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[27]
    children7_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[28]
    children8_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[29]
    children8_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[30]
    children8_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[31]
    children8_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[32]
    children9_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[33]
    children9_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[34]
    children9_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[35]
    children9_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[36]
    children10_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[37]
    children10_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[38]
    children10_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[39]
    children10_list.append(add_time)

    add_time = {}
    add_time['name'] = '2016'
    add_time['children'] = add_time_list[40]
    children11_list.append(add_time)
    add_time = {}
    add_time['name'] = '2017'
    add_time['children'] = add_time_list[41]
    children11_list.append(add_time)
    add_time = {}
    add_time['name'] = '2018'
    add_time['children'] = add_time_list[42]
    children11_list.append(add_time)
    add_time = {}
    add_time['name'] = '2019'
    add_time['children'] = add_time_list[43]
    children11_list.append(add_time)

    children1['value'] = 16
    children2['value'] = 8
    children3['value'] = 5.5
    children4['value'] = 4
    children5['value'] = 5
    children6['value'] = 0.5
    children7['value'] = 21.5
    children8['value'] = 9
    children9['value'] = 4.0
    children10['value'] = 24.5
    children11['value'] = 21.5

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
    return data

def updateDatabase(stu_id, train_plan):
    """
    功能: 用户在“培养计划”界面点击“提交”按钮后，使用最新“计划树”信息更新数据库
    :param stu_id: 唯一标识学生的id
    :param train_plan: “培养计划”界面“计划树”数据的json格式
    :return: 无
    """
    data = train_plan['children']
    array_finish = [0]*120
    # print(array_finish)
    for data_children in data:
        data_children = data_children['children']
        print(data_children)
        for data_children_child_1 in data_children:
            # print('data_children_child', data_children_child)
            data_children_child_1 = data_children_child_1['children']
            for data_children_child in data_children_child_1:
                name = data_children_child['children'][0]['name']
                color = data_children_child['children'][0]['itemStyle']['borderColor']
                #print(name, color)
                sql = "select CO_100 from education_plan WHERE CO_NAME='%s'" % name
                co_100 = query(sql)
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
    sql = "UPDATE edu_stu_plan SET FINISHED_CO='%s' WHERE STU_NO='%s'" % (finish_co,stu_id)
    update(sql)


def updateScore(stu_id, scores):
    sql="SELECT CO_NO, CO_NAME FROM EDUCATION_PLAN";
    name2no = {}
    result = query(sql)
    for cur in result:
        name2no[cur[1]] = cur[0]

    for cur in scores:
        sql="UPDATE CHOOSE SET COMMENT='%d' WHERE STU_NO='%s' AND CO_NO='%s'" % (scores[cur], stu_id, name2no[cur])
        #print(sql)
        update(sql)