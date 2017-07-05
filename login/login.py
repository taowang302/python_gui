import json
import MySQLdb


def set_mysql(host='localhost',port=3306,database,usr='root',passwd):
    conn = MySQLdb.connect(
        host=host,
        port = port,
        user=usr,
        passwd=passwd,
        db =database,
        )
    return  conn.cursor()

def login(cur,information):
    # print name
    # passwd = usr_dic.get(information.get("name"))
    passwd = cur.execute("select from usr_map where name='{}'".format(information.get("name")))
    if passwd:
        if passwd == information.get("passwd"):
            return json.dumps({'status': "login success"})
        else:
            return json.dumps({'status': "password error"})
    else:
        return json.dumps({'status': "user do not registered"})
