import numpy as np
from skinranges import typeskins

import cv2


def skindetect(img, type, data):
    converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # RGB->HSV
    ranges = typeskins(type, data)

    skinMask = np.zeros(img.shape[:2], np.uint8)

    # Filtro de color en rgb
    if type == 'data_rgb':
        x, y, z = img.shape
        for i in range(x):
            for j in range(y):
                r, g, b = img[i, j]
                aux = [r, g, b]
                if aux in ranges:
                    skinMask[i, j] = 255
        # Ediciones de elemento estructural erosion/dilatacion
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))  # Elemento estructural
        skinMask = cv2.dilate(skinMask, kernel, iterations=1)


    # Filtro de color en hsv
    else:
        for i in range(len(ranges) - 1):
            skinMask = skinMask + cv2.inRange(converted, ranges[i], ranges[i + 1])
        # Ediciones de elemento estructural erosion/dilatacion
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))  # Elemento estructural
        skinMask = cv2.erode(skinMask, kernel, iterations=1)
        skinMask = cv2.dilate(skinMask, kernel, iterations=1)
        if type == 'data_hsv':
            skinMask[skinMask == 0] = 1
            skinMask[skinMask > 1] = 0
            skinMask[skinMask == 1] = 255



    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)  # Edit por desenfoque
    skin = cv2.bitwise_and(img, img, mask=skinMask)

    return skinMask

'''
# Ejemplo
frame = cv2.imread('1r.png')
data = cv2.imread('data1.png')
type = 'data_rgb'

skindetect(frame, type, data)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''