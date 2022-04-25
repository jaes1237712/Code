import itertools
import threading
import time
import sys
from numpy import diff
import pandas as pd
from inputimeout import inputimeout, TimeoutOccurred
import ascii_magic
import os


path = 'Time.csv'
clear = lambda: os.system('clear')
flag = True
def cls():
    print("\033[H\033[J", end="")

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
                sys.stdout.flush()
                time.sleep(2/144)
                cnt +=1   
    return False
def animation2(s):
    cnt = 0
    while cnt<=80:
        tmp = ""
        for i in s:
            try:
                inputimeout(prompt='', timeout=0.2)
                return True
            except TimeoutOccurred:
                cls()
                tmp += i
                print(tmp,'\n')
                path = "study/"+str(cnt%10)+".jpg"
                my_art = ascii_magic.from_image_file(path)
                ascii_magic.to_terminal(my_art)
                print("input sth to END")
                time.sleep(4/144)
                cnt +=1
            
    return False

def Relax_Time():
    Start = time.time()
    time.sleep(0.2)
    while True:
        if animation("...Relaxing...Relaxing...Relaxing...Relaxing...Relaxing...Relaxing...Relaxing..."):
            cls()
            End = time.time()
            break
    differ = round((End-Start)/60,2)
    data = pd.read_csv(path,index_col=0)
    data['Accumulation'][0] = round(float(data['Accumulation'][0])+ differ,0)
    data.to_csv(path)
    cls()
    print("Cost Time:",differ)
    print(data)
    if(data["Accumulation"][0]<data["Accumulation"][1]):
        for i in range(5):
            print("You are great!!. Keep this figure!!")
        print("The differ:",data["Accumulation"][1]-data["Accumulation"][0])
    else:
        for i in range(5):
            print("Shame on you. You should study then play!")
        print("The differ:",data["Accumulation"][1]-data["Accumulation"][0])
    return 
def Study_Time():
    Start = time.time()
    time.sleep(1)
    while True:
        if animation2("...Studying...Studying...Studying...Studying...Studying...Studying...Studying..."):
            cls()
            End = time.time()
            break
    differ = round((End-Start)/60,2)
    data = pd.read_csv(path,index_col=0)
    data['Accumulation'][1] = round(float(data['Accumulation'][1])+ differ,0)
    data.to_csv(path)
    cls()
    print("Cost Time:",differ)
    print(data)
    if(data["Accumulation"][0]<data["Accumulation"][1]):
        for i in range(5):
            print("You are great!!. Keep this figure!!")
        print("The differ:",data["Accumulation"][1]-data["Accumulation"][0])
    else:
        for i in range(5):
            print("加油，補足差距！")
        print("The differ:",data["Accumulation"][1]-data["Accumulation"][0])
    return 

while True:
    string = input("What time is it?\n\
1: Relax\n\
2: Study \n\
3: Exit\n")
    try:
        case = int(string)
        if case == 1:
            Relax_Time()
        elif case == 2:
            Study_Time()
        elif case == 3:
            print("Bye~Bye~")
            break
        else:
            print("你在打什麼？")
    except:
        print("你在打什麼？")
    print("\n")
# 之後要做的是針對日期分出不同的時間表。