"""3.   OCR Engine Mode (oem): Tesseract 4에는 2 개의 OCR 엔진이 있습니다. 

1) 레거시 Tesseract 엔진

 2) LSTM 엔진: --oem 옵션을 사용하여 선택 할 수 있는 네 가지 작동 모드는 다음과 같습니다.
    0    Legacy engine only.
    1    Neural nets LSTM engine only.
    2    Legacy + LSTM engines.
    3    Default, based on what is available.
     
Page segmentation modes(–psm):
    0 - Orientation and script detection (OSD) only.
    1 - Automatic page segmentation with OSD.
    2 - Automatic page segmentation, but no OSD, or OCR.
    3 - Fully automatic page segmentation, but no OSD. (Default)
    4 - Assume a single column of text of variable sizes.
    5 - Assume a single uniform block of vertically aligned text.
    6 - Assume a single uniform block of text.
    7 - Treat the image as a single text line.
    8 - Treat the image as a single word.
    9 - Treat the image as a single word in a circle.
    10 - Treat the image as a single character.
    11 - Sparse text. Find as much text as possible in no particular order.
    12 - Sparse text with OSD.
    13 - Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.
    
    """