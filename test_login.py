from UserLogin.check_login import *
import json

information=json.loads(["{'method':'login','information':{'name':'tom','passwd':'123456'}}"])

conn = check_login.set_mysql(host='localhost',port=3306,database="webdemo",usr='root',passwd="jbi123456")
print check_login.login(conn, information)
