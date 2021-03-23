'''
pip install requests
pip install tabulate
pip install "colorama>=0.3.8"
pip install future
pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o

'''
#%%
import h2o
from h2o.automl import H2OAutoML
from h2o.h2o import load_model
import pandas as pd

class H2oClass:
    def __init__(self):
        # Start H2O Server
        h2o.init()
        self.train=[]
        self.test=[]
        
        self.x = None
        self.y = None

        self.aml = None
        self.preds = None

        self.model_path = None

    def load_data(self, path):
        df = pd.read_csv(path, sep=',')
        hf = h2o.H2OFrame(df)
        return hf

    def split_data(self, data):
        self.train, self.test = data.split_frame(ratios = [.8], seed = 1234)

        self.x = self.train.columns
        self.y = "y"
        self.x.remove(self.y)

        # For binary classification, "y" should be a factor
        self.train[self.y] = self.train[self.y].asfactor()
        self.test[self.y] = self.test[self.y].asfactor()

    def train_model(self):
        # Setting parameter
        self.aml = H2OAutoML(max_models=3
                        , seed=1
                    )

        # Train Model
        self.aml.train(x= self.x, y=self.y, training_frame=self.train)

        # Select Model in autoML
        lb = self.aml.leaderboard
        lb.head(rows=lb.nrows)

    def save_model(self):
        self.model_path = h2o.save_model(model=self.aml.leader, path=r"/model", force=True)

    def load_model(self, model_path):
        return h2o.load_model(model_path)

    def predict(self, data):
        # self.preds = self.aml.predict(data)
        self.preds = self.aml.leader.predict(data)

        # self.test[self.y].cbind(self.preds)
#%%  
h = H2oClass()

#%%
data = h.load_data("h2o_sample.csv")

#%%
h.split_data(data)

#%%
h.train_model()

#%%
h.save_model()

#%%
h.predict(h.test)

#%%
h.test[h.y].cbind(h.preds)
# %%
t = h.test
# predict(data) 에 다른 데이터 생성해서 넣어서 테스트 해보면 됨 

#%%
# t = t.drop(21)
h.predict(t)
# t

#%%
h.preds

#%%
pre = h.load_data(r"D:\\Project\\tesseract\\regex_result\\model2.csv")

#%%
h.predict(pre) 
h.preds

#%%
model = h.load_model(r"D:\\model\\GBM_1_AutoML_20210323_104837")

#%%
ppp = model.predict(pre)
ppp