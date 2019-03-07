import numpy as np
import cv2
if __name__ == "__main__":
    row = 200
    column = 300
    print u"Generating a spatial matrix(%d*%d)..." % (row, column)
    img = np.zeros((row, column,3), np.uint8)
    pos1 = np.random.randint(200, size = (2000,1))
    pos2 = np.random.randint(300, size = (2000,1))
    for i in range(2000):
        img[pos1[i], pos2[i],[0]] = np.random.randint(0,255)
        img[pos1[i], pos2[i],[1]] = np.random.randint(0,255)
        img[pos1[i], pos2[i],[2]] = np.random.randint(0,255)

cv2.imshow('preview', img)
cv2.waitKey()
cv2.destoryAllWindows()