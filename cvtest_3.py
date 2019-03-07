# -*- coding:UTF-8 -*-
import numpy as np
import cv2
#  生成负片
filename = "test2.jpg"
if __name__ == '__main__':
    img = cv2.imread(filename)
    sp = img.shape
    print(sp)
    width = sp[1]
    height = sp[0]
    #  生成负片
    b,g,r = cv2.split(img)
    b = 255 - b
    g = 255 - g
    r = 255 - r
    img[:,:,0] = b
    img[:,:,1] = g
    img[:,:,2] = r

    cv2.namedWindow('img')
    cv2.imshow('img',img)
    cv2.waitKey()
    cv2.destoryAllWindows()