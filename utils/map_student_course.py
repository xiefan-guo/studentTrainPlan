from query import query


def get_map_student():
    map_student = {}
    sql = "SELECT NAME, STU_NO FROM STUDENT WHERE STU_NO<>'admin'"
    result = query(sql)
    map_student_id = 0
    for cur in result:
        values = list(cur)
        map_student[map_student_id] = values
        map_student_id = map_student_id + 1

    map_course = {}
    sql="SELECT CO_NAME FROM EDUCATION_PLAN"
    result = query(sql)
    map_course_id = 0
    for cur in result:
        map_course[map_course_id] = cur[0]
        map_course_id = map_course_id + 1

    return map_student, map_course


def get_matrix():
    map_student, map_course = get_map_student()
    matrix = []
    for i in range(30):
        matrix.append([])
    for i in range(30):
        stu_no = map_student[i][1]
        #print(stu_no)
        for j in range(118):
            #print(map_course[j])
            sql="SELECT CO_NO FROM EDUCATION_PLAN WHERE CO_NAME='%s'" % map_course[j]
            stu_id = query(sql)
            stu_id=stu_id[0][0]
            #print(stu_id)
            sql="SELECT COMMENT FROM CHOOSE WHERE STU_NO='%s' AND CO_NO='%s'" % (stu_no, stu_id)
            score=query(sql)
            if len(score)==0:
                score=0
            else:
                score=score[0][0]
                score=int(score)
            #print(score)
            matrix[i].append(score)

    return matrix

