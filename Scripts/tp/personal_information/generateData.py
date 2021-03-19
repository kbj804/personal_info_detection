from Scripts.tp.regex.keyword_extract import KeywordExtract
from Scripts.tp.regex.regexDictionaryManager import regexDictionaryManager
from Scripts.tp.regex.loadFileManager import loadFileManager
from Scripts.tp.regex.keyword_extract import KeywordExtract
import pandas as pd


class GenerateData:
    def __init__(self) -> None:
        self.origin_regex_dic = regexDictionaryManager()
        self.default_model_df = pd.read_csv(r'./regex_result/model.csv', encoding='UTF-8')
        self.kwd = KeywordExtract(r'./tesseract_Project/Scripts/tp/nlp/dic.txt')


    def update_model_df(self, df_data):
        # print(self.default_model_df)
        # print(df_data)
        c_df = pd.concat([self.default_model_df, df_data]).reset_index(drop=True)
        c_df.to_csv(r'./regex_result/model.csv', sep=',', na_rep='NaN', encoding='UTF-8', index=False)
        return c_df


    # need generate file path
    def generate_df(self, file_path):
        file = loadFileManager(file_path)
        pages = list(file.data.keys())

        data =[]

        for page in range(0, len(pages)):
            # regex name, count, regex_ruslt_list
            _, c, _= self.origin_regex_dic.get_all_regex(file.data[page])

            row_list = [c]

            # Keyword List에 Regex Count가 추가되어있기 때문에 인덱스 1부터시작 해줘야 함
            for i in range(1, len(self.kwd.keywords)):
                # fileData / search() or findall()
                if self.kwd.keyword_dictionary[i].search(file.data[page]): 
                    # print(ke.keyword_dictionary[i].search(file.data[page]))
                    row_list.append(1)
                else:
                    row_list.append(0)
            
            data.append(row_list)
        
        df = pd.DataFrame(data, columns=self.kwd.keywords)
        return df

g = GenerateData()
a = g.generate_df("pdf_sample2.pdf")
b = g.update_model_df(a)
print(b)

