from PIL import Image
import cv2
import numpy as np

def resizeimg(img, width, name):
    basewidth = width
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    #img.save(name+'.png')
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    return img


'''
frame_original = frame = resizeimg(Image.open('p.PNG'), 500, '1r')
cv2.waitKey(0)
cv2.destroyAllWindows()
'''