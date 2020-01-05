#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket,time,subprocess,pyttsx3
target_ip = "127.0.0.1"     
target_port = 1233

#Now we are creating UDP socket -- this is  all sender & receiver both    ipv4 ,UDP

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#this is sender side
while True:
    msg = input("please enter ur msg: ")
#we have to encode string to byte like obj in python3 only

    newmsg = msg.encode('ascii')
    print(newmsg)

    s.sendto(newmsg,(target_ip,target_port))
    
    client_data = s.recvfrom(100)
    print(client_data)
    #  now  converting to audio msg
    audio1=pyttsx3.init()
    audio1.say(client_data[0].decode('ascii'))
    audio1.runAndWait()
    time.sleep(1)


# In[ ]:





# In[ ]:




