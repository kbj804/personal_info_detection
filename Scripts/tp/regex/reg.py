import re
import time
# import os
# print(os.path.abspath(os.path.dirname(__file__)))
from regularExpression_configs import RegexConfigs

class regexDictionaryManagerClass:
    def __init__(self):
        # new regex Dictionary
        self.dictionary={}
        
        self.origin_regex = RegexConfigs()
        self.origin_Dictionary = self.origin_regex.preComfile_dic
    
    # 키값 있는지 없는지 검사
    def check_key(self, key):
        try:
            if self.origin_Dictionary[key]:    # else시 에러
            # if key in self.origin_Dictionary:    # return값 boolean 
                value = self.origin_Dictionary.get(key)    # return값 value
                return value
            else:
                print("{} dose not exist in Regualr-Dictionary".format(key))
        
        except Exception as e:
            print("####ERROR####{0} \n {1} dose not exist in Regualr-Dictionary".format(e ,key))
    
    
    def add_regex(self, key):
        v = self.check_key(key)
        if v == None:
            pass
        else:
            self.dictionary.setdefault(key, v)

    def show_dictionary(self):
        print(self.dictionary)

a = regexDictionaryManagerClass()
a.add_regex('E-mail2')
a.add_regex('E-mail')
a.add_regex('ipAddress')

b = regexDictionaryManagerClass()
b.add_regex('sadff')

a.show_dictionary()