import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd 

img=mpimg.imread('06.jpg')
img_copy = img.copy()
center = 1900
for i in range(4000):
    img_copy[i][center:center+100] = np.array([0,0,0])
imgplot = plt.imshow(img_copy)
st,ed = 1600,3300 # start, end
RGB = np.zeros(((ed-st)+1,3))

for i in range(st,ed+1, 1):
    RGB[i-st] = img[i][center]
x = np.linspace(st,ed,(ed-st)+1)
df = pd.DataFrame(RGB)
filepath = 'raw_data.xlsx'
df.to_excel(filepath, index=False)
# plt.figure()
# plt.plot(x,R,'r',linewidth = 1)
# plt.plot(x,G,'g',linewidth = 1)
# plt.plot(x,B,'b',linewidth = 1)
# plt.show()
# RGB = np.hstack(R,G,B)