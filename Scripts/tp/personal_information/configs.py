class Configs:
    def __init__(self) -> None:
        # Folder path
        self.sample_folder_path = r'D:\\Project\\tesseract\\sample\\'
        self.train_folder_path = r'D:\\Project\\tesseract\\tesseract_Project\\Scripts\\tp\\ml\\train\\'

        # File path
        self.keyword_path = r'D:\\Project\\tesseract\\tesseract_Project\Scripts\\tp\\nlp\\dic.txt'
        self.default_csv_model_path = r'D:\\Project\\tesseract\\tesseract_Project\\Scripts\\tp\\ml\\train\\model.csv'

        # Save h2o model
        self.model_path = r'D:\\Project\\tesseract\\model'

        self.using_model = self.model_path + '/GBM_1_AutoML_20210324_171907'