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
from Scripts.tp.personal_information.configs import Configs
import pandas as pd

class H2oClass(Configs):
    def __init__(self):
        super().__init__()
        # Start H2O Server
        h2o.init()
        self.train=[]
        self.test=[]
        
        self.x = None
        self.y = None

        self.model = None
        self.preds = None

        self.md_path = None

    def load_csv_to_hf(self, path):
        df = pd.read_csv(path, sep=',')
        hf = h2o.H2OFrame(df)
        return hf

    def df_to_hf(self, df):
        hf = h2o.H2OFrame(df)
        return hf

    def split_data(self, h_data):
        self.train, self.test = h_data.split_frame(ratios = [.8], seed = 1234)

        self.x = self.train.columns
        self.y = "y"
        self.x.remove(self.y)

        # For binary classification, "y" should be a factor
        self.train[self.y] = self.train[self.y].asfactor()
        self.test[self.y] = self.test[self.y].asfactor()

    def train_model(self):
        # Setting parameter
        aml = H2OAutoML(max_models=3
                        , seed=1
                    )

        # Train Model
        aml.train(x= self.x, y=self.y, training_frame=self.train)
        
        # aml.leaderboard
        # Select Model in autoML
        return aml.leader
        # self.model.head(rows=self.model.nrows)

    def save_md(self, model):
        self.md_path = h2o.save_model(model=model, path=self.model_path, force=True)

    def load_md(self, model_path):
        return h2o.load_model(model_path)

    # 이거 없이 그냥 model.predict(hdf) 사용해도 됨
    def predict(self, data):
        # self.preds = self.aml.predict(data)
        self.preds = self.model.predict(data)

        # self.test[self.y].cbind(self.preds)
'''#%%  
h = H2oClass()

#%%
data = h.load_csv_to_hf("h2o_sample.csv")
data
#%%
h.split_data(data)

#%%
ml = h.train_model()
ml

#%%
ml.leader
#%%
h.save_md(ml)

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
ppp'''