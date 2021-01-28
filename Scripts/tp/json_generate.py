#-*- coding: utf-8 -*-

# Import libraries 
import pytesseract
import json
import re
import sys
import os
from PIL import Image
from pdf2image import convert_from_path
from collections import OrderedDict
from nlp.kiwi_morp import kiwi_dictionary_n_fuction
# print(os.path.abspath(os.path.dirname(__file__)))

def pdf2img(pages):
    # init image_counter
    image_counter = 1

    for page in pages:
        filename = "page_"+str(image_counter)+".jpg"
      
        # Save the image of the page in system 
        page.save(filename, 'JPEG') 
    
        # Increment the counter to update filename 
        image_counter = image_counter + 1
        
    return generate_json(image_counter)

# json structure  
def generate_json(image_counter):
    page_list = []
    for i in range(1, image_counter):
        json_data = OrderedDict()
        filename = "page_"+str(i)+".jpg"

        text = str(((pytesseract.image_to_string(Image.open(filename), config=config))))
        text, morp, keyword = preprocess_data(text)

        json_data['file'] = file_name
        json_data['file_path'] = file_path
        json_data['file_type'] = file_type
        json_data['language'] = "kor"
        json_data['page'] = str(i)
        
        json_data['data'] = {'text': text,
                                'morp': morp,
                                'keyword': keyword
                                }
        json_data['classification'] = "분류 예제"

        print(json_data)
        page_list.append(json_data)
    
    return page_list

def preprocess_data(readData):
    text = re.sub('[-=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\[\]\<\>`\'…》]', '', readData)
    text = re.sub(r"\n+", "", text)
    text = re.sub("\ +", " ", text)

    morp = kiwi_f.get_token_str(text)
    keyword = get_keyword(text)

    return text, morp, keyword

# get keyword
def get_keyword(text):
    nn_list = kiwi_f.get_nn_list(text)

    # reduce duplication keyword(nn)
    k_set = set(nn_list)
    keyword = list(k_set)
    return keyword

if __name__ == "__main__":
    # OCR config
    poppler_path = r'D:\Project\tesseract\tesseract_Project\Lib\site-packages\poppler-20.12.1\bin' # for pdf2image Library
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract' # tesseract.exe path
    config = ('-l kor --oem 1 --psm 4') # tesseract configs value
    
    # etc config
    img_path = 'tesseract_Project/Scripts/tp/'
    file_type = 'pdf'
    file_name = "병합"
    file_path = img_path + file_name + "." + file_type
    
    kiwi_f = kiwi_dictionary_n_fuction(img_path+'nlp/dic.txt')

    pages = convert_from_path(file_path , 500, poppler_path = poppler_path)
    jsondata = pdf2img(pages)

    with open(file_name + ".json", 'w', encoding='utf-8') as make_file:
        json.dump(jsondata, make_file, ensure_ascii=False, indent='\t')
 
    # print(preprocess_data("   tkv tk    fkfkf   fkfk  fkfk \n\n\nsdsd"))
