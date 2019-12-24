#!/usr/bin/python3
#to accept input from user

import subprocess
import webbrowser
import time
print("enter your choice")
choice = input()
#input function will accepts the value in string

#print("enter",choice)

if choice == '1':
    #opening default browser
    print("Wait kar bhai!!!!")
    time.sleep(4)
    
    print(webbrowser.open_new_tab('now.html'))
    """Opening a specificed browser
    print(webbrowser.open_new_tab('https://www.google.com'))"""

elif choice == '2':
    print("Opening Browser to Check internet Status: ")
    print(webbrowser.open_new_tab('https://www.google.com/search?q=fast.com'))


elif choice=='3':
    output=subprocess.getstatusoutput('ping  8.8.8.8')
    if output[0]==0:
        print("your internet is working ")
    else:
        print("not working")


elif choice == '4' :
    print("current date",subprocess.getoutput('date /t') )
    print("current time",subprocess.getoutput('time /t')  )

elif choice == '7':
    dir_name=input("Please enter name of directory:")
    dir_output=subprocess.getstatusoutput("mkdir "+dir_name)
    if dir_output[0] == 0:
        print("your directory "+dir_name,"Successfully created")
    else:
        print("Please choose another directory name")

elif choice == '10':
    msg=input("please enter what to search in google:- ")
    time.sleep(2)
    
    webbrowser.open_new_tab('https://www.google.com/search?q='+msg)
    
    
else:
    print("wrong option")
    
