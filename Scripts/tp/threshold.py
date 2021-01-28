import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img_path = 'tesseract_Project/Scripts/tp/pic/'

img = cv2.imread(img_path + 'receipt1.jpg', 0)
# img = cv2.medianBlur(img,5)

ret, thresh1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO_INV)


thresh6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,2)
thresh7 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,2)

ret2, thresh8 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img,(5,5),0)

ret3, thresh9 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# images = [img,th1,th2,th3]

# for i in range(4):
# 	plt.subplot(2, 2, i+1),plt.imshow(images[i],'gray')
# 	plt.title(titles[i])
# 	plt.xticks([]),plt.yticks([])

# plt.show()

# Tozero, Gaussian 이 깔끔하게 추출 됨
# 두개 뽑아서 Morphological Transformations 해보자
titles = ['Binary','Binary_inv','Trunc','Tozero','Tozero_inv','Mean_B','Gaussian_B','B_O','blur','B_O2']
thresh = [thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7, thresh8, blur, thresh9 ]
for i in range(10):
	cv2.imshow(titles[i], thresh[i])
	cv2.waitKey(0)