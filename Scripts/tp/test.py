import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Path 주의!

# print(cv2.version)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
config = ('-l kor+eng --oem 2 --psm 4')

img = cv2.imread('receipt.png')

# cv2.imshow('image', img)
# cv2.waitKey(0)
# print(pytesseract.image_to_string(img, config=config))


canny = cv2.Canny(img,30,70)

laplacian = cv2.Laplacian(img,cv2.CV_8U)
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Origianl', 'Laplacian', 'Sobel X', 'Sobel Y','Canny']

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title([titles[i]])
    plt.xticks([]),plt.yticks([])

plt.show()


# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# 블러처리로 노이즈 제거
# gray = cv2.medianBlur(gray, 10)

# print(pytesseract.image_to_string(gray, config=config))

# cv2.imshow('gray', gray)
# cv2.waitKey(0)


# print(" =============== 음영 처리 ================== ")
# img_gray=cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('gray', img_gray)

# print(pytesseract.image_to_string(img_gray, config=config))
# cv2.waitKey()

