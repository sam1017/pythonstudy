# -*- coding:UTF-8 -*-
import numpy as np
import cv2
filename1 = "test3.jpg"
filename2 = "test4.jpg"
if __name__ == '__main__':
    img1 = cv2.imread(filename1)
    sp = img1.shape
    print(sp)
    width = sp[1]
    height = sp[0]

    #  融合图片
    #img2 = cv2.imread(filename2)
    #if width == img2.shape[1] and height == img2.shape[0]:
    #    for img_y in xrange(0, height):
    #        for img_x in xrange(0,width):
    #            img2[img_y,img_x,0] = int(img2[img_y,img_x,0]*0.5 + img1[img_y,img_x,0]*0.5)
    #            img2[img_y,img_x,1] = int(img2[img_y,img_x,1]*0.5 + img1[img_y,img_x,1]*0.5)
    #            img2[img_y,img_x,2] = int(img2[img_y,img_x,2]*0.5 + img1[img_y,img_x,2]*0.5)
    #cv2.namedWindow('img2')
    #cv2.imshow('img2',img2)

    #生成镜像图片
    for img_y in xrange(0,height):
        for img_x in xrange(width/2, width):
            img1[img_y,img_x,:] = img1[img_y,width - img_x,:]
    cv2.namedWindow('img')
    cv2.imshow('img',img1)
    cv2.waitKey()
    cv2.destoryAllWindows()