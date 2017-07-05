from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json
from   UserLogin.check_login import *
from RunShell import RunCommand
from OP_RETURN.OP_RETURN import *
import sys

def btc_opreturn(information):
    print "start action"
    send_address = information.get("address").decode("utf-8").rstrip("\n")
    send_amount = information.get("amount").decode("utf-8").rstrip("\n")
    metadata =  information.get("metadata").decode("utf-8").rstrip("\n")
    if_testnet = int(information.get("if_testnet"))
    if if_testnet:
        try:
            result = OP_RETURN_send(send_address, float(send_amount), metadata, if_testnet)
        except:
            info = sys.exc_info()
            print info[0],":",info[1]
            return json.dumps({"status":"fail","reason":'{}'.format(sys.exc_info()[1])})
        else:
            print result
            if 'error' in result:
                return json.dumps({"status":"fail","information":result})  
            else:
                return json.dumps({"status":"sucess","information":result})  
    else:
        pass


def check_login(information):
    coon = set_mysql(host='localhost', port=3306, database='webdemo', usr='root', passwd='jbi123456')
    return login(coon, information)

method_dic = {'login': check_login,
              "run_shell_command": RunCommand.run_shell_command,
              "op_return":btc_opreturn}

class TodoHandler(BaseHTTPRequestHandler):
    """A simple TODO server
    which can display and manage todos for you.
    """

    # Global instance to store todos. You should use a database in reality.
    # def __init__(self):
    #     self.TODOS = ["this is a test"]
    #     self.method_dic = {'getname':self.getname}
    TODOS = ["this is a test"]


    def do_GET(self):
        # return all todos

        if self.path != '/':
            self.send_error(404, "File not found.")
            return

        # Just dump data to json, and return it
        message = json.dumps(self.TODOS)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(self.gen_msg('get_name'))

    def do_POST(self):
        """Add a new todo

        Only json data is supported, otherwise send a 415 response back.
        Append new todo to class variable, and it will be displayed
        in following get request
        """
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        if ctype == 'application/json':
            length = int(self.headers['content-length'])
            post_values = json.loads(self.rfile.read(length))
            # self.TODOS.append(post_values)
        else:
            self.send_error(415, "Only json data is supported.")
            return
        #print '--------'
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(self.gen_msg(post_values))


    def gen_msg(self,post_body):
        method = post_body.get("method")
        information = post_body.get("information")
        #print method_dic.get(method)(information)
        return method_dic.get(method)(information)

if __name__ == '__main__':
    # Start a simple server, and loop forever
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('', 8888), TodoHandler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()
