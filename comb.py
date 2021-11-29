import sys
from skin_edit import skindetect
from split_and_merge import split_and_merge
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)


def grab(frame, mask, type):
    frame_original = frame
    skin_mask = mask
    #cv2.imshow('Skin mask detection', skin_mask)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)


    mask[mask >= 1] = 1  # 3FG
    mask[mask == 0] = 2  # 2BG


    # """
    mask2, bgdModel, fgdModel = cv2.grabCut(frame, mask, None, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_MASK)
    mask2 = np.where((mask2 == 2) | (mask2 == 0), 0, 1).astype('uint8')
    frame = frame * mask2[:, :, np.newaxis]

    mask[mask == 1] = 1
    mask[mask >= 2] = 0

    #cv2.imshow(type, cv2.bitwise_and(frame, frame, mask=mask))

    return frame

# Version mascara prediseñada
'''
cv2.imshow('Original image', frame_original)
cv2.imshow('Final mask grabCut', mask2)
cv2.imshow('Final', frame)
'''


# Version generación de mascaras
'''
frame = cv2.imread('1r.png')
data1 = cv2.imread('data1.png')
data2 = cv2.imread('data2.png')
# type skinmask
# sorted_hsv_basic
# hsv_basic
# data_hsv
# data_rgb
# split_and_merge

type1 = 'data_rgb'
type2 = 'data_rgb'

mask1 = skinmask1 = skindetect(frame, type1, data1)
mask2=skinmask2 = skindetect(frame, type2, data2)
newmask = cv2.bitwise_and(frame, frame, mask=mask1+mask2)
mask1=split_merge_mask = split_and_merge(newmask)


#Version de mascaras sumadas
mask1=0
mask1 = skinmask1 = skindetect(frame, 'data_rgb', data1)
cv2.imshow('1',cv2.bitwise_and(frame, frame, mask=mask1))
mask1 = mask1 + skindetect(frame, 'data_rgb', data2)
cv2.imshow('2',cv2.bitwise_and(frame, frame, mask=mask1))
mask1 = mask1 + skindetect(frame, 'data_hsv', data1)
cv2.imshow('3',cv2.bitwise_and(frame, frame, mask=mask1))
mask1 = mask1 + skindetect(frame, 'sorted_hsv_basic', data1)
cv2.imshow('4',cv2.bitwise_and(frame, frame, mask=mask1))
mask1 = mask1 + skindetect(frame, 'hsv_basic', data1)
cv2.imshow('5',cv2.bitwise_and(frame, frame, mask=mask1))
mask1 = mask1 + split_and_merge(frame)
cv2.imshow('6',cv2.bitwise_and(frame, frame, mask=mask1))


cv2.imshow("+Grabcut",grab(frame, mask1, 'data_hsv'))

cv2.imshow("Grabcut",grab(frame, skinmask1, type1)+grab(frame, mask2, type2))

cv2.waitKey(0)
cv2.destroyAllWindows()
'''