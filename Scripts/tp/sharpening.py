#-*-coding:utf-8 -*-
import cv2
import numpy as np
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
config = ('-l kor --oem 1 --psm 4')

img_path = 'tesseract_Project/Scripts/tp/pic/'
img = cv2.imread(img_path + 'receipt1.jpg', cv2.CV_16UC1)

sharpening_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpening_2 = np.array([[-1, -1, -1, -1, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, 2, 9, 2, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, -1, -1, -1, -1]]) / 9.0

dst = cv2.filter2D(img, -1, sharpening_1)

ret, thresh4 = cv2.threshold(dst, 127,255, cv2.THRESH_TOZERO)

def boxes(img):
    d = pytesseract.image_to_data(img, output_type=Output.DICT, config=config)    
    n_boxes = len(d['text'])
    for i in range(n_boxes):
    # if int(d['conf'][i]) > 60:
        # print(d['conf'][i], d['text'][i])
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)  
    return img


cv2.imshow('dst', dst)
print(pytesseract.image_to_string(dst, config=config))
cv2.waitKey()

cv2.imshow('Sharpening_tozero', thresh4)
print(pytesseract.image_to_string(thresh4, config=config))
cv2.waitKey()

cv2.imshow('boxes', boxes(thresh4))
cv2.waitKey()

# cv2.imshow('Sharpening1', boxes(dst))
# cv2.waitKey()

# dst = cv2.filter2D(img, -1, sharpening_2)
# cv2.imshow('Sharpening2', dst)
# cv2.waitKey()