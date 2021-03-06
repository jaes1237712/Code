import itertools
from re import X
import threading
import time
import sys
from numpy import diff
import pandas as pd
from inputimeout import inputimeout, TimeoutOccurred
import ascii_magic
import os
import cursor
cursor.hide()


path = 'Time.csv'
flag = True
def cls():
    print("\033[%d;%dH" % (0, 0))
def clear():
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

def Trivial_Time():
    clear()
    Start = time.time()
    time.sleep(0.2)
    while True:
        if animation("...Trivial...Trivial...Trivial...Trivial...Trivial...Trivial...Trivial"):
            clear()
            End = time.time()
            break
    differ = round((End-Start)/60,2)
    data = pd.read_csv(path,index_col=0)
    data['Accumulation'][2] = round(float(data['Accumulation'][2])+ differ,0)
    data.to_csv(path)
    clear()
    print("Cost Time:",differ)
    print(data)
    for i in range(5):
        print("Make trivial time as small as possible, ok?")
    return
def Relax_Time():
    clear()
    Start = time.time()
    time.sleep(0.2)
    while True:
        if animation("...Relaxing...Relaxing...Relaxing...Relaxing...Relaxing...Relaxing...Relaxing..."):
            clear()
            End = time.time()
            break
    differ = round((End-Start)/60,2)
    data = pd.read_csv(path,index_col=0)
    data['Accumulation'][0] = round(float(data['Accumulation'][0])+ differ,0)
    data.to_csv(path)
    clear()
    print("Cost Time:",differ)
    print(data)
    if(data["Accumulation"][0]+data["Accumulation"][2]<data["Accumulation"][1]/2):
        for i in range(5):
            print("You are great!!. Keep this figure!!")
        print("The differ:",2*data["Accumulation"][1]-data["Accumulation"][0]-data["Accumulation"][2])
    else:
        for i in range(5):
            print("Shame on you. You should study then play!")
        print("The differ:",2*data["Accumulation"][1]-data["Accumulation"][0]-data["Accumulation"][2])
    return 
def Study_Time():
    clear()
    Start = time.time()
    time.sleep(1)
    while True:
        if animation2("...Studying...Studying...Studying...Studying...Studying...Studying...Studying..."):
            clear()
            End = time.time()
            break
    differ = round((End-Start)/60,2)
    data = pd.read_csv(path,index_col=0)
    data['Accumulation'][1] = round(float(data['Accumulation'][1])+ differ,0)
    data.to_csv(path)
    clear()
    print("Cost Time:",differ)
    print(data)
    if(data["Accumulation"][0]+data["Accumulation"][2]<data["Accumulation"][1]/2):
        for i in range(5):
            print("You are great!!. Keep this figure!!")
        print("The differ:",2*data["Accumulation"][1]-data["Accumulation"][0]-data["Accumulation"][2])
    else:
        for i in range(5):
            print("Not enough!!")
        print("The differ:",2*data["Accumulation"][1]-data["Accumulation"][0]-data["Accumulation"][2])
    return 

while True:
    string = input("What time is it?\n\
1: Relax\n\
2: Study \n\
3: Trivial\n\
4: Exit\n")
    try:
        case = int(string)
        if case == 1:
            Relax_Time()
        elif case == 2:
            Study_Time()
        elif case == 3:
            string = input("Are u sure? (Y/n)")
            if string == "Y":
                Trivial_Time()
        elif case == 4:
            print("Bye~Bye~")
            break
        else:
            print("??????????????????")
    except:
        print("??????????????????")
    print("\n")
# ?????????????????????????????????????????????????????????