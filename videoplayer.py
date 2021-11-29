from io import StringIO

from PIL import Image
import cv2
import numpy as np
from skin_edit import skindetect
from split_and_merge import split_and_merge
from resize import resizeimg
from comb import grab

# sorted_hsv_basic
# hsv_basic
# data_hsv
# data_rgb
# split_and_merge
type = 'data_hsv'  # Tipo de Segmentación
cap = cv2.VideoCapture('Referencia1F.mp4')  # Video para segmentar
data = cv2.imread('data1.png')  # Tipo de fragmento guia de parte del video
grab_cut = True  # Generar GrabCut o visualizar segmentación previa

skinmask = ()

x = 0
while True:
    x += 1
    print('Frame:', x)
    # Display the resulting frame
    ret, frame = cap.read()
    if ret:
        PIL_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).astype('uint8'), 'RGB')
        frame = resizeimg(PIL_image, 500, '1r')

        if type == 'split_and_merge':
            skinmask = split_and_merge(frame)
        else:
            skinmask = skindetect(frame, type, data)

        if grab_cut:
            final = grab(frame, skinmask, type)
        else:
            final = cv2.bitwise_and(frame, frame, mask=skinmask)

        cv2.imshow('final', final)

        # cv2.imwrite("D:/Escritorio/Skin/Resultados/HSV1/"+str(x)+".png", final)

    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
