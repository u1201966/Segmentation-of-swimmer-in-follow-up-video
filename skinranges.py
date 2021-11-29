import numpy as np
import cv2


def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v


def typeskins(type, data):
    u8 = "uint8"

    if type == 'sorted_hsv_basic':

        A = (
            [0, 10, 60],
            [0, 30, 60],
            [20, 150, 255],
            [108, 23, 82],
            [179, 255, 255]
        )

        H = ()

        for i in range(len(A)):
            r, g, b = A[i]
            h, s, v = rgb_to_hsv(r, g, b)
            H = H + ([str(int(h)), r, g, b],)

        H1 = sorted(H, reverse=True)
        ret = ()
        for i in range(len(A)):
            x, r, g, b = H1[i]
            ret = ret + (np.array([r, g, b], dtype=u8),)

        return ret

    elif type == 'hsv_basic':
        A = (
            [0, 10, 60],
            [0, 30, 60],
            [20, 150, 255],
            [108, 23, 82],
            [179, 255, 255]
        )

        ret = ()
        for i in range(len(A)):
            ret = ret + (np.array(A[i], dtype=u8),)

        return ret

    elif type == 'data_hsv':
        d = ()
        H = ()
        x, y, z = data.shape
        for i in range(x):
            for j in range(y):
                r, g, b = data[i, j]
                aux = [r, g, b]
                if not aux in d:
                    h, s, v = rgb_to_hsv(r, g, b)
                    d = d + ([r, g, b],)
                    H = H + ([str(int(h)), r, g, b],)

        H1 = sorted(H, reverse=True)
        H1=H
        ret = ()
        for i in range(len(H1)):
            x, r, g, b = H1[i]
            ret = ret + (np.array([r, g, b], dtype=u8),)

        return ret

    elif type == 'data_rgb':
        ret = ()
        x, y, z = data.shape
        for i in range(x):
            for j in range(y):
                r, g, b = data[i, j]
                aux = [r, g, b]
                if not aux in ret:
                    ret = ret + ([r, g, b],)

        ret = sorted(ret)
        return ret

    return 0




'''
data = cv2.imread('data1.png')
typeskins('data_hsv', data)
'''