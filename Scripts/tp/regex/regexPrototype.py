from Scripts.tp.regex.keyword_extract import KeywordExtract
from Scripts.tp.regex.regexDictionaryManager import regexDictionaryManager
from Scripts.tp.regex.loadFileManager import loadFileManager
from Scripts.tp.nlp.kiwi_morp import kiwi_dictionary_n_fuction
from Scripts.tp.regex.keyword_extract import KeywordExtract
import pandas as pd

origin_regex = regexDictionaryManager()


# file = loadFileManager("csv_sample.csv")
file = loadFileManager("pdf_sample2.pdf")
# print(file.data[0])
# print(file.path)
# origin_regex.get_all_regex(file.data[0])
# origin_regex.get_all_regex(file.data[1])
# origin_regex.get_all_regex(file.data[2])

# kwd = kiwi_dictionary_n_fuction(r'./tesseract_Project/Scripts/tp/nlp/dic.txt')

# 사전에서 키워드 추출
ke = KeywordExtract(r'./tesseract_Project/Scripts/tp/nlp/dic.txt')
pages = list(file.data.keys())

# 정규식 검출 수 Column을 Keyword List에 추가
ke.keywords.insert(0, "Regex Count")

data = []

# df = pd.DataFrame(data, columns= ke.keywords)


# CSV파일은 ,으로 구분
row = ','.join(ke.keywords)

# Page별 데이터 로드
for page in range(0, len(pages)):
    print(f"############# PAGE: {page+1} #################")
    
    # regex name, count, regex_ruslt_list
    rn, c, rrl= origin_regex.get_all_regex(file.data[page])

    # 정규식 검출 수 Column 값 추가    
    row += '\n' + str(c)

    row_list=[c]

    # Keyword List에 Regex Count가 추가되어있기 때문에 -1 해줘야 함
    for i in range(0, len(ke.keywords)-1):
        row += ','
        # fileData / search() or findall()
        if ke.keyword_dictionary[i].search(file.data[page]): 
            # print(ke.keyword_dictionary[i].search(file.data[page]))
            row += '1'
            row_list.append(1)
        else:
            row += '0'
            row_list.append(0)
    
    data.append(row_list)
    
    
    # print(list(row.split(',')))

    # print(kwd.get_keyword(file.data[i]))
    # print(kwd.k_morphs(file.data[i]))
    # print(f"Regex Name : {rn}")
    # print(f"Regex Count : {c}")
    # print(f"Regex Result List : {rrl}")

df = pd.DataFrame(data, columns= ke.keywords)
print(df)

print(row)
origin_regex.extract_csv(row, "result")


# a = regexManager()

# a.add_regex('E-mail2')
# a.add_regex('E-mail')
# a.add_regex('ipAddress')
# a.add_regex('PhoneNumber')

# a.show_dictionary()


# a.get_regex_result(file.data)
