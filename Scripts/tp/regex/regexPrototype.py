from Scripts.tp.regex.regexDictionaryManager import regexManager
from Scripts.tp.regex.loadFileManager import loadFileManager


origin_regex = regexManager()

# 파일을 위 클래스 init에 넣을지 말지 고민좀....
def generate_data(file):
    with open(file, 'r', encoding='UTF8') as f:
        data = f.read()
        return data
            
file = loadFileManager("text.pdf")
print(file.name)
print(file.ext)

# a = regexManager()

# a.add_regex('E-mail2')
# a.add_regex('E-mail')
# a.add_regex('ipAddress')
# a.add_regex('PhoneNumber')

# a.show_dictionary()

# data = generate_data('test2.txt')

# a.get_regex_result(data)
