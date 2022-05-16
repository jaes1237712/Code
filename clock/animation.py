import itertools
import threading
import time
import sys
import pandas as pd
from inputimeout import inputimeout, TimeoutOccurred
import ascii_magic
import os
def cls():
    print("\033[H\033[J", end="")
def animation(s):
    cnt = 0
    while cnt<=80:
        tmp = ""
        for i in s:
            if done:
                break
            else:
                tmp += i
                print(tmp,'\n')
                path = "portal/potal-"+str(cnt%80)+".jpg"
                my_art = ascii_magic.from_image_file(path)
                ascii_magic.to_terminal(my_art)
                print("input sth to END")
                sys.stdout.flush()
                time.sleep(0.1)
                cnt +=1   

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animation())
t.start()

#long process here
time.sleep(10)
done = True