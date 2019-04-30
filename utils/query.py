import pymysql


def query(sql):
    db = pymysql.connect('localhost', 'root', config['MYSQL_PASSWORD'], config['DATABASE_NAME'], charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()
    except:
        db.rollback()
    cur.close()
    db.close()
    return result
