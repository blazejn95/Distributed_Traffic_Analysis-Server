import socket
import os
import subprocess
import time
subprocess.Popen("python init.py", shell=True)
time.sleep(1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.31"  # modify or make it input
port = 1235

s.connect((host, port))
s.send(b'Hello server!')
data = None
startFlag = True
ending = 'endofdata'
while(1):
    CLIoutput = subprocess.check_output("ls")
    if ("data1" in CLIoutput) and startFlag == True:
        print("sending data0")
        startFlag = False

        f = open("data0", "rb")
        l = f.read(1024)
        while(l):
            holder = s.send(l)
            l = f.read(1024)
        time.sleep(1)
        s.send(ending)
        f.close()
        print('Successfully sent the file')
        os.remove("data0")
        CLIoutput = subprocess.check_output("ls")
    if ("data0" in CLIoutput) and startFlag == False:
        print("sending data1")
        startFlag = True

        f = open("data1", "rb")
        l = f.read(1024)
        while(l):
            holder = s.send(l)
            l = f.read(1024)
        time.sleep(1)
        s.send(ending)
        f.close()
        print('Successfully sent the file')
        os.remove("data1")
s.close()
print('connection closed')
