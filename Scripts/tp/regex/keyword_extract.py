
import re

class KeywordExtract:
    def __init__(self, keyword_path) -> None:
        # 
        self.keywords=['Regex Count']
        with open(keyword_path, mode="r", encoding='UTF8') as kwd_file:
            for kwd in kwd_file:
                # preprocessing for reducing tail string
                index = kwd.find('\t')
                word = kwd[:index]

                self.keywords.append(word)

        self.keyword_dictionary = {}
        for i, kwd in enumerate(self.keywords):
            self.keyword_dictionary[i] = re.compile(kwd)


# a = KeywordExtract(r"./tesseract_Project/Scripts/tp/nlp/dic.txt")
# print(a.keywords)
# print(a.keyword_dictionary)
# text = "jdgajdsngj sdfsadkljn kfgoodf sd f njlksdfn agter  sdalfafter sdnfj good"

# 사용 예제
# for i in range(0, len(list(a.keyword_dictionary.keys()))):
#     print(a.keyword_dictionary[i].search(text))


import h2o
from h2o.automl import H2OAutoML

h2o.init()




df = h2o.import_file("origin.txt")

train, test = df.split_frame(ratios = [.8], seed = 1234)

x = train.columns
y = "y"
x.remove(y)

train[y] = train[y].asfactor()
test[y] = test[y].asfactor()

aml = H2OAutoML(max_models=3, seed=1)
aml.train(x=x, y=y, training_frame=train)

lb = aml.leaderboard
lb.head(rows=lb.nrows)

preds = aml.predict(test)
test[y].cbind(preds)


# Save Model
model_path = h2o.save_model(model=aml.leader, path="/model", force=True)
print(model_path)

# Load Model
saved_model = h2o.load_model(model_path)

# Prodiction
preds = saved_model.predict(test)
test[y].cbind(preds)