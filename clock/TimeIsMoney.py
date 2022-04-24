import time
import pandas as pd
from inputimeout import inputimeout, TimeoutOccurred
import ascii_magic
import os
import webbrowser

path = 'Time.csv'
clear = lambda: os.system('clear')
flag = True
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def animation(s):
    cnt = 0
    while cnt<=80:
        tmp = ""
        for i in s:
            try:
                inputimeout(prompt='', timeout=0.1)
                return True
            except TimeoutOccurred:
                cls()
                tmp += i
                print(tmp,'\n')
                path = "portal/potal-"+str(cnt%80)+".jpg"
                my_art = ascii_magic.from_image_file(path)
                ascii_magic.to_terminal(my_art)
                print("input sth to END")
                time.sleep(0.1)
                cnt +=1
            
    return False
def animation2(s):
    cnt = 0
    while cnt<=80:
        tmp = ""
        for i in s:
            try:
                inputimeout(prompt='', timeout=0.1)
                return True
            except TimeoutOccurred:
                cls()
                tmp += i
                print(tmp,'\n')
                path = "study/"+str(cnt%10)+".jpg"
                my_art = ascii_magic.from_image_file(path)
                ascii_magic.to_terminal(my_art)
                print("input sth to END")
                time.sleep(0.1)
                cnt +=1
            
    return False

def Relax_Time():
    Start = time.time()
    time.sleep(1)
    while True:
        if animation("...Relaxing..."):
            cls()
            End = time.time()
            print("Start Time:",time.ctime(Start))
            print("End Time:",time.ctime(End))
            print("Cost Time:",End-Start)
            break
    data = pd.read_csv(path,index_col=0)
    data['Accumulation'][0] = round(float(data['Accumulation'][0])+ End-Start,0)
    data.to_csv(path)
    print(data)
    print("You are great!!. Keep this habit!!")
    return 
def Study_Time():
    Start = time.time()
    time.sleep(1)
    while True:
        if animation2("...Studying..."):
            cls()
            End = time.time()
            break
    data = pd.read_csv(path,index_col=0)
    data['Accumulation'][1] = round(float(data['Accumulation'][1])+ End-Start,0)
    data.to_csv(path)
    cls()
    print("Cost Time:",End-Start)
    print(data)
    print("You are great!!. Keep this habit!!")
    return 

def initialize():
    data = pd.read_csv(path,index_col=0)
    data['Accumulation'][1] = 0
    data['Accumulation'][0] = 0
    data.to_csv(path)
    print(data)
    print("Success!!")
    return

while True:
    string = input("What time is it?\n\
1: Study\n\
2: Relax \n\
3: Initialize \n\
4: Exit\n")
    case = int(string)
    if case == 1:
        Study_Time()
    elif case == 2:
        Relax_Time()
    elif case == 3:
        initialize()
    elif case == 4:
        print("Bye~Bye~")
        break
    else:
        print("你在打什麼？")
    print("\n",'\n')

# 之後要做的是針對日期分出不同的時間表。