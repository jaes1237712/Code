from time import sleep
import ascii_magic
import time




while True:
  for i in range(80):
      path = "portal/potal-"+str(i)+".jpg"
      my_art = ascii_magic.from_image_file(path)
      ascii_magic.to_terminal(my_art)
      time.sleep(0.1)
      
      
