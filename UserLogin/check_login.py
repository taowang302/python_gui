import json
import MySQLdb


def set_mysql(host='localhost',port=3306,database='usr',usr='root',passwd=123456):
    conn = MySQLdb.connect(
        host=host,
        port = port,
        user=usr,
        passwd=passwd,
        db =database)
    return  conn.cursor()

def login(cur,information):
    # print name
    # passwd = usr_dic.get(information.get("name"))
    data_nu = cur.execute("select admin_password from webdemo_admin where admin_name='{}'".format(information.get("name")))
    if 0 != data_nu : 
        passwd = cur.fetchone()[0]
        if passwd == information.get("passwd"):
            return json.dumps({'status': "UserLogin success"})
        else:
            #print "{} => {}".format(passwd,type(passwd))
            #print "{} => {}".format(information.get("passwd"),type(information.get("passwd")))
            return json.dumps({'status': "password error"})
    else:
        return json.dumps({'status': "user do not registered"})

def register(cur,information):
    data_nu = cur.execute("insert into webdemo_admin () value () ")
    return json.dumps({'status': "success"})
