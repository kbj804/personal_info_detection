#-*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

dotImage = cv2.imread('receipt1.jpg')
holeImage = cv2.imread('receipt1.jpg')
orig = cv2.imread('receipt1.jpg')


kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

"""
# erosion
각 Pixel에 structuring element를 적용하여 하나라도 0이 있으면 대상 pixel을 제거
원본의 각 pixel에 적용하여 겹치는 부분이 하나라도 있으면 그 중심 pixel을 제거함

# cv2.erode(src, kernel, dst, anchor, iterations, borderType, borderValue)

Parameters:	
src – the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
kernel – structuring element. cv2.getStructuringElemet() 함수로 만들 수 있음.
anchor – structuring element의 중심. default (-1,-1)로 중심점.
iterations – erosion 적용 반복 횟수
"""

erosion = cv2.erode(dotImage,kernel,iterations = 1)

"""
# Dilation
대상을 확장한 후 작은 구멍을 채우는 방법. Pixel에 대해서 OR연산을 수행하여 겹치는부분에 대해 이미지 확장
경계가 부드러워지고, 구멍이 메꿔지는 효과

# cv2.dilation(src, kernel, dst, anchor, iterations, borderType, borderValue)

Parameters:	
src – the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
kernel – structuring element. cv2.getStructuringElemet() 함수로 만들 수 있음.
anchor – structuring element의 중심. default (-1,-1)로 중심점.
iterations – dilation 적용 반복 횟수
"""
dilation = cv2.dilate(holeImage,kernel,iterations = 1)

"""
Opening과 Closing은 Erosion과 Dilation의 조합 결과 입니다. 차이는 어느 것을 먼저 적용을 하는 차이 입니다.
Opeing : Erosion적용 후 Dilation 적용. 작은 Object나 돌기 제거에 적합
Closing : Dilation적용 후 Erosion 적용. 전체적인 윤곽 파악에 적합

# cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst

Parameters:	
src – Source image. The number of channels can be arbitrary. The depth should be one of CV_8U, CV_16U, CV_16S, CV_32F` or ``CV_64F.
op –
Type of a morphological operation that can be one of the following:

MORPH_OPEN - an opening operation
MORPH_CLOSE - a closing operation
MORPH_GRADIENT - a morphological gradient. Dilation과 erosion의 차이.
MORPH_TOPHAT - “top hat”. Opeining과 원본 이미지의 차이
MORPH_BLACKHAT - “black hat”. Closing과 원본 이미지의 차이
kernel – structuring element. cv2.getStructuringElemet() 함수로 만들 수 있음.
anchor – structuring element의 중심. default (-1,-1)로 중심점.
iterations – erosion and dilation 적용 횟수
borderType – Pixel extrapolation method. See borderInterpolate for details.
borderValue – Border value in case of a constant border. The default value has a special meaning.
"""
opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(holeImage, cv2.MORPH_CLOSE,kernel)

gradient = cv2.morphologyEx(orig, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(orig, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(orig, cv2.MORPH_BLACKHAT, kernel)

images =[dotImage, erosion, opening, holeImage, dilation, closing, gradient, tophat, blackhat]
titles =['Dot Image','Erosion','Opening','Hole Image', 'Dilation','Closing', 'Gradient', 'Tophat','Blackhot']

for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()