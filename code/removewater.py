#coding=utf-8
#图片修复

# from cv2 import cv2 
import cv2
import numpy as np

imageName= "frame33"
path = "D:\img\\1\\"+imageName+".png"
pathNew = "D:\img\\1\\"+imageName+"_1.png"

img = cv2.imread(path)
hight, width, depth = img.shape[0:3]

print(img.ndim)

bright_image = img.copy() 

# 203,6  235,6
# 203,28 235,28

#对像素blue/green/red值整体
for row in range(8,28): 
    for column in range(205,234):
        bright_image[row, column, 0] = 204
        bright_image[row, column, 1] = 153
        bright_image[row, column, 2] = 51

#填充 内容
img2 = cv2.putText(bright_image, 'Yuan Dynasty', (151,15), cv2.LINE_4,  0.6, (0,0,255), 1)

img2 = cv2.putText(bright_image, 'sslbitcoin.com', (301,255), cv2.LINE_4,  0.5, (0,0,255), 1)
# cv2.imshow(winname='show black image',mat=bright_image)
cv2.imwrite(pathNew, bright_image)
cv2.waitKey()
cv2.destroyAllWindows()
