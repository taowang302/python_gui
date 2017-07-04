import json
import subprocess

def run_shell_command(information):
    #command_list = unicode(information.get("command"),"utf-8").split(" ")
    #print type(information.get("command"))
    command_list = information.get("command").encode("utf-8").split(" ")
    print command_list
    try:
        subprocess.Popen(command_list)
    except Exception as e:
        #print e
        return json.dumps({'status': "run fail" , "reason":unicode(e)})
    else:
        # print "sucess"
        return json.dumps({'status': "success"})