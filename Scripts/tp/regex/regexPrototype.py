from Scripts.tp.regex.regexDictionaryManager import regexDictionaryManager
from Scripts.tp.regex.loadFileManager import loadFileManager
from Scripts.tp.nlp.kiwi_morp import kiwi_dictionary_n_fuction

origin_regex = regexDictionaryManager()


# file = loadFileManager("csv_sample.csv")
file = loadFileManager("pdf_sample2.pdf")
# print(file.data[0])
# print(file.path)
# origin_regex.get_all_regex(file.data[0])
# origin_regex.get_all_regex(file.data[1])
# origin_regex.get_all_regex(file.data[2])

kwd = kiwi_dictionary_n_fuction(r'./tesseract_Project/Scripts/tp/nlp/dic.txt')

keys = list(file.data.keys())
for i in range(0, len(keys)):
    print(f"############# PAGE: {i+1} #################")
    # regex name, count, regex_ruslt_list
    rn, c, rrl= origin_regex.get_all_regex(file.data[i])
    print(kwd.get_keyword(file.data[i]))
    # print(kwd.k_morphs(file.data[i]))
    print(rn)
    print(c)
    print(rrl)




# a = regexManager()

# a.add_regex('E-mail2')
# a.add_regex('E-mail')
# a.add_regex('ipAddress')
# a.add_regex('PhoneNumber')

# a.show_dictionary()


# a.get_regex_result(file.data)
