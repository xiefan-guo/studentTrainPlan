import pymysql
from config import config


def query(sql):
    db = pymysql.connect('localhost', 'root', config['MYSQL_PASSWORD'], config['DATABASE_NAME'], charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()
        print('query success')
    except:
        print('query loss')
        db.rollback()
    cur.close()
    db.close()
    return result


def update(sql):
    db = pymysql.connect('localhost', 'root', config['MYSQL_PASSWORD'], config['DATABASE_NAME'], charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
        print('update success')
    except:
        print('update loss')
        db.rollback()
    cur.close()
    db.close()

