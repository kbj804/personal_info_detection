"""
Canny Edge Detection
가장 유명한 Edge Detection방법입니다. 여러 단계의 Algorithm을 통해서 경계를 찾아 냅니다.

Noise Reduction
이미지의 Noise를 제거합니다. 이때 5x5의 Gaussian filter를 이용합니다.

Edge Gradient Detection
이미지에서 Gradient의 방향과 강도를 확인합니다. 경계값에서는 주변과 색이 다르기 때문에 미분값이 급속도로 변하게 됩니다. 이를 통해 경계값 후보군을 선별합니다.

Non-maximum Suppression
이미지의 pixel을 Full scan하여 Edge가 아닌 pixel은 제거합니다.

Hysteresis Thresholding
이제 지금까지 Edge로 판단된 pixel이 진짜 edge인지 판별하는 작업을 합니다. 
max val과 minVal(임계값)을 설정하여 maxVal 이상은 강한 Edge, min과 max사이는 약한 edge로 설정합니다. 
이제 약한 edge가 진짜 edge인지 확인하기 위해서 강한 edge와 연결이 되어 있으면 edge로 판단하고, 그러지 않으면 제거합니다.
이와 같은 일련의 작업을 통해서 경계값만을 남겨두고 제거합니다.


Laplacian 함수
이미지의 가로와 세로에 대한 Gradient를 2차 미분한 값입니다. Sobel filter에 미분의 정도가 더해진 것과 비슷합니다.
(dx와 dy가 2인 경우) blob(주위의 pixel과 확연한 picel차이를 나타내는 덩어리)검출에 많이 사용됩니다.

Sobel & Scharr Filter
Gaussian smoothing과 미분을 이용한 방법입니다. 그래서 노이즈가 있는 이미지에 적용하면 좋습니다. X축과 Y축을 미분하는 방법으로 경계값을 계산합니다.
직선을 미분하면 상수, 곡선을 미분하면 또 다른 방정식이 나오는 성질을 이용하여 edge에 대한 선을 그려주는 기능을 합니다. 
X축 미분은 수평선(수직선이 남음), Y축 미분은 수직선(수평선이 남음)을 미분하여 경계가 사라지는 효과가 있습니다. 
미분시 소실되는 표본의 정보가 많을 수 있어 aperture_size 값을 이용하여 소실되는 정도를 조절할 수 있습니다.
만약 ksize가 -1이면 3x3 Scharr filter가 적용이 되어 Sobel의 3x3보다 좀 더 나은 결과를 보여 줍니다.

"""

import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
config = ('-l kor --oem 1 --psm 4')

img = cv2.imread('4.png')
canny = cv2.Canny(img, 30, 70)
laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img, cv2.CV_8U,1,0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U,0,1, ksize=3)

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Origianl', 'Laplacian', 'Sobel X', 'Sobel Y','Canny']

# for i in range(5):
#     plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title([titles[i]])
#     plt.xticks([]),plt.yticks([])
#     print(pytesseract.image_to_string(images[i], config=config))
# plt.show()

for i in range(5):
	cv2.imshow('img', images[i])
	cv2.waitKey(0)
# print(pytesseract.image_to_string(images[0], config=config))
# cv2.waitKey(0)