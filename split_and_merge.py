import sys
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)


def split_and_merge(frame):
    (B, G, R) = cv2.split(frame)

    B[B > 120] = 0
    R[R > 0] = 0
    G[G > 0] = 0

    #B[B > 90] = 0
    #R[R < 90] = 0
    #G[G > 90] = 0
    merged = cv2.merge([B, G, R])
    gray = cv2.cvtColor(merged, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))  # Elemento estructural
    gray = cv2.erode(gray, kernel, iterations=1)
    gray = cv2.dilate(gray, kernel, iterations=1)


    return gray



