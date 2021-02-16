import os

class loadFileManager:
    def __init__(self, path) -> None:
        # dir_path = os.getcwd()
        basename = os.path.basename(path)
        self.name, self.ext = os.path.splitext(basename)
