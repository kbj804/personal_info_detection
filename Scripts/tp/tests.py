import re

txt = "안녕하세요............."
# for i in range(0,txt.count('..')): 
#     txt = txt.replace("..",".")

print(re.sub("\.+", ".",txt))

