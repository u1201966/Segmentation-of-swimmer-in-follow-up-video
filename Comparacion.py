import sys
import cv2
import numpy as np
from PIL import Image
np.set_printoptions(threshold=sys.maxsize)

porcentaje_completitud = 0
porcentaje_aislamiento = 0
frames = 80
for i in range(frames):
    direction = "HSV1"
    original = cv2.imread("Resultados/Completness/"+str(i+1)+".png")
    segmentation = cv2.imread("Resultados/"+direction+"/"+str(i+1)+".png")

    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    segmentation = cv2.cvtColor(segmentation, cv2.COLOR_BGR2GRAY)

    original[original == 255] = 0
    original[original > 0] = 255



    segmentation[segmentation > 0] = 255
    completitud = np.zeros(original.shape, np.uint8)

    aislamiento = np.zeros(original.shape, np.uint8)
    not_orig = np.zeros(original.shape, np.uint8)
    not_orig[original == 255] = 0
    not_orig[original == 0] = 255





    completitud[np.logical_and(segmentation == original, original == 255)] = 255
    aislamiento[np.logical_and(segmentation == not_orig, segmentation == 255)] = 255

    ''
    cv2.imshow('a', original)
    cv2.waitKey(10)
    cv2.imshow('a', completitud)
    cv2.waitKey(20)
    cv2.imshow('a', aislamiento)
    cv2.waitKey(20)
    ''
    comp = 1-(abs(np.count_nonzero(completitud == 255)-np.count_nonzero(original == 255))/np.count_nonzero(original == 255))
    porcentaje_completitud = porcentaje_completitud+comp

    aisl = 1 - (np.count_nonzero(aislamiento == 255) / np.count_nonzero(not_orig == 255))
    porcentaje_aislamiento = porcentaje_aislamiento+aisl

porcentaje_completitud = 100*porcentaje_completitud/frames
print('Completitud:', porcentaje_completitud)
porcentaje_aislamiento = 100*porcentaje_aislamiento/frames
print('Aislamiento:', porcentaje_aislamiento)
print('Promedio:', (porcentaje_aislamiento+porcentaje_completitud)/2)

cv2.waitKey(1)
cv2.destroyAllWindows()