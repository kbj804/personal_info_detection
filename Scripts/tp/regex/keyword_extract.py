
import re

class KeywordExtract:
    def __init__(self, keyword_path) -> None:
        self.keywords=[]
        with open(keyword_path, mode="r", encoding='UTF8') as kwd_file:
            for kwd in kwd_file:
                self.keywords.append(kwd.rstrip('\n'))
                print(kwd)


        # kwds = ["good", "after", "noon", "full"]
        

        # self.keyword_dictionary = {}
        # for i, kwd in enumerate(kwds):
        #     self.keyword_dictionary[i] = re.compile(kwd)


a = KeywordExtract(r"./tesseract_Project/Scripts/tp/nlp/keyword.txt")
print(a.keywords)

# text = "jdgajdsngj sdfsadkljn kfgoodf sd f njlksdfn agter  sdalfafter sdnfj good"

# for i in range(0, len(list(a.keyword_dictionary.keys()))):
#     print(a.keyword_dictionary[i].search(text))