import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
config = ('-l kor --oem 1 --psm 4')


img = cv2.imread('doc1.jpg')

# th2 = cv2.adaptiveThreshold(
#                             img, 
#                             maxValue=255,
#                             adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                             thresholdType=cv2.THRESH_BINARY,
#                             blockSize=11,
#                             C=2
#                             )
# th2 = cv2.medianBlur(th2, 3)

# img = th2


def boxes(img):
    d = pytesseract.image_to_data(img, output_type=Output.DICT, config=config)    
    n_boxes = len(d['text'])
    for i in range(n_boxes):
    # if int(d['conf'][i]) > 60:
        # print(d['conf'][i], d['text'][i])
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)  
    return img
        
    
# d = pytesseract.image_to_data(img, output_type=Output.DICT, config=config)

# print(d.keys())
# dict_keys(['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text'])

print(pytesseract.image_to_string(img, config=config))
# n_boxes = len(d['text'])
# for i in range(n_boxes):
    # if int(d['conf'][i]) > 60:
        # print(d['conf'][i], d['text'][i])
        # (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)


cv2.imshow('img', boxes(img))
cv2.waitKey(0)