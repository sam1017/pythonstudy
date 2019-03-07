# -*- coding:UTF-8 -*-
import numpy as np
import cv2
#  图像修改成日落场景
filename = "test2.jpg"
if __name__ == '__main__':
    img = cv2.imread(filename)
    sp = img.shape
    print(sp)
    width = sp[1]
    height = sp[0]
    print ' width: %d \n height %d ' % (width,height)
    for xi in xrange(0,width):
        for xj in xrange(0,height):
            img[xj,xi,0] = int(img[xj,xi,0]*0.7)
            img[xj,xi,1] = int(img[xj,xi,1]*0.7)
            #img[xj,xi,2] = int(img[xj,xi,2]*0.5)
            #if xi%100 == 0:
            #    print(".")

    cv2.namedWindow('img')
    cv2.imshow('img',img)
    cv2.waitKey()
    cv2.destoryAllWindows()