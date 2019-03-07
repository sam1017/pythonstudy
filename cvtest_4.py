# -*- coding:UTF-8 -*-
import numpy as np
import cv2
#  平铺图片
filename = "test3.jpg"
if __name__ == '__main__':
    img = cv2.imread(filename)
    sp = img.shape
    print(sp)
    width = sp[1]
    height = sp[0]
    #  正常平铺
    #new_width = 5 * width
    #new_height = 2 * height

    #转置后再平铺
    new_width = 5 * height
    new_height = 2 * width

    num_x = 0
    num_y = 0

    new_img = np.zeros((new_height, new_width,3), np.uint8)
    print u"default bmp (%d*%d)" % (width,height)
    print u"new bmp (%d*%d)" % (new_width,new_height)
    for new_y in xrange(0, new_height):
        for new_x in xrange(0, new_width):
            new_img[new_y,new_x,0] = img[num_x, num_y,0]
            new_img[new_y,new_x,1] = img[num_x, num_y,1]
            new_img[new_y,new_x,2] = img[num_x, num_y,2]
            num_x +=1
            if num_x >= height:
                num_x = 0
        num_y += 1
        if num_y >= width:
            num_y = 0

    cv2.namedWindow('img1')
    cv2.imshow('img1',new_img)
    cv2.waitKey()
    cv2.destoryAllWindows()