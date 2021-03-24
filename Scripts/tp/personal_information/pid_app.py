#%%
from Scripts.tp.personal_information.generateData import GenerateData
from Scripts.tp.personal_information.configs import Configs
from Scripts.tp.ml.h2o_helper import H2oClass

class PIDetection(Configs):
    def __init__(self) -> None:
        super().__init__()
        self.h = None

    # h2o init
    def run(self):
        self.h = H2oClass()

    # File 입력 받아서 키워드 바탕으로 학습에 사용할 Dataframe 생성
    def generate_df(self, file_path):
        g = GenerateData()
        return g.file_to_dataframe(file_path)

    # Dataframe to CSV File
    def dataframe_to_csv(self, df, filename):
        df.to_csv(self.train_folder_path + filename + '.csv', sep=',', index=False)

    # 일단 보류
    def update_csv(self, csv_path, up_df):
        pass
    
    # 학습하고 저장까지
    def train_hf(self, csv_path):
        if self.h is None:
            # h2o init Error
            raise ModuleNotFoundError

        else:
            hf = self.h.load_csv_to_hf(csv_path)
            
            # self.train, test, x, y
            self.h.split_data(hf)

            # leader model
            lm = self.h.train_model()

            self.h.save_md(lm)
    
    def load_recent_model(self, md):
        if self.h is None:
            # h2o init Error
            raise ModuleNotFoundError
        else:
            return self.h.load_md(md)


# 데이터 만드는거 구현해야함


a = PIDetection()
a.run()
# a.train_hf(r'D:\\Project\\tesseract\\tesseract_Project\\Scripts\\tp\\ml\\train\\h2o_sample.csv')
model = a.load_recent_model(a.using_model)
preds = model.predict()
