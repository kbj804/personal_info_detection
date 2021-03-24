from Scripts.tp.personal_information.generateData import GenerateData
from Scripts.tp.personal_information.configs import Configs

class PIDetection(Configs):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        pass

    # File 입력 받아서 키워드 바탕으로 학습에 사용할 Dataframe 생성
    def generate_df(self, file_path):
        g = GenerateData()
        return g.file_to_dataframe(file_path)

