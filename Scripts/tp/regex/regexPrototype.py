from Scripts.tp.regex.keyword_extract import KeywordExtract
from Scripts.tp.regex.regexDictionaryManager import regexDictionaryManager
from Scripts.tp.regex.loadFileManager import loadFileManager
from Scripts.tp.nlp.kiwi_morp import kiwi_dictionary_n_fuction
from Scripts.tp.regex.keyword_extract import KeywordExtract

origin_regex = regexDictionaryManager()


# file = loadFileManager("csv_sample.csv")
file = loadFileManager("pdf_sample2.pdf")
# print(file.data[0])
# print(file.path)
# origin_regex.get_all_regex(file.data[0])
# origin_regex.get_all_regex(file.data[1])
# origin_regex.get_all_regex(file.data[2])

# kwd = kiwi_dictionary_n_fuction(r'./tesseract_Project/Scripts/tp/nlp/dic.txt')

ke = KeywordExtract(r'./tesseract_Project/Scripts/tp/nlp/dic.txt')
pages = list(file.data.keys())
ke.keywords.insert(0, "Regex Count")
row = ','.join(ke.keywords)

for page in range(0, len(pages)):
    print(f"############# PAGE: {page+1} #################")
    # regex name, count, regex_ruslt_list
    rn, c, rrl= origin_regex.get_all_regex(file.data[page])
    
    row += '\n' + str(c)


    for i in range(0, len(ke.keywords)-1):
        row += ','
        if ke.keyword_dictionary[i].search(file.data[page]):
            # print(ke.keyword_dictionary[i].search(file.data[page]))
            row += '1'
        else:
            row += '0'

    # print(kwd.get_keyword(file.data[i]))
    # print(kwd.k_morphs(file.data[i]))
    print(f"Regex Name : {rn}")
    print(f"Regex Count : {c}")
    print(f"Regex Result List : {rrl}")

print(row)
origin_regex.extract_csv(row, "result")


# a = regexManager()

# a.add_regex('E-mail2')
# a.add_regex('E-mail')
# a.add_regex('ipAddress')
# a.add_regex('PhoneNumber')

# a.show_dictionary()


# a.get_regex_result(file.data)
