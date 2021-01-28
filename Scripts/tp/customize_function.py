def boxes(img):
    d = pytesseract.image_to_data(img, output_type=Output.DICT, config=config)    
    n_boxes = len(d['text'])
    for i in range(n_boxes):
    # if int(d['conf'][i]) > 60:
        # print(d['conf'][i], d['text'][i])
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)  
    return img