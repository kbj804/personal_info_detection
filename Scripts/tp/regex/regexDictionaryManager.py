import re
import time

# import os
# print(os.path.abspath(os.path.dirname(__file__)))
from Scripts.tp.regex.regularExpression_configs import RegexConfigs

class regexDictionaryManagerClass:
    def __init__(self):
        # new regex Dictionary
        self.dictionary={}
        
        origin_regex = RegexConfigs()
        self.origin_Dictionary = origin_regex.preComfile_dic
    
    # 키값 있는지 없는지 검사
    def check_key(self, key):
        try:
            if self.origin_Dictionary[key]:    # else시 에러
            # if key in self.origin_Dictionary:    # return값 boolean 
                value = self.origin_Dictionary.get(key)    # return값 value
                return value
            else:
                print("@ # @ # {} For Debugging... @ # @ #".format(key))
        
        except Exception as e:
            print("####ERROR#### {0} dose not exist in Regualr-Dictionary".format(e))
    
    # Dictionary에 정규표현식 추가
    def add_regex(self, key):
        v = self.check_key(key)
        if v == None:
            pass
        else:
            self.dictionary.setdefault(key, v)
            print("Success Add Regular Expression Dictionary")

    def show_dictionary(self):
        keys = list(self.dictionary.keys())
        print("key list = {}".format(keys))
        print(self.dictionary)

    def extract_csv(self, data, filename):
        with open("./regex_result/" + filename + '.csv', "w") as file:
            file.write(filename + '\n' + data)
            file.close()

    # 문자
    def get_regex_result(self, data):
        keys = list(self.dictionary.keys())

        for i in range(0, len(keys)):
            result = ''
            for regex in self.dictionary[keys[i]].findall(data):
                result += str(regex[0]) + '\n'
            
            self.extract_csv(result, keys[i])
            print("{} is Success Extract".format(keys[i]))
            
    def generate_data(self, file):
        with open(file, 'r', encoding='UTF8') as f:
            data = f.read()
            return data
            

a = regexDictionaryManagerClass()
a.add_regex('E-mail2')
a.add_regex('E-mail')
a.add_regex('ipAddress')
a.add_regex('PhoneNumber')
a.show_dictionary()

data = a.generate_data('test2.txt')

a.get_regex_result(data)
