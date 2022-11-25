import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd 
img=mpimg.imread('06.jpg')    
img = img[:,:,::-1]