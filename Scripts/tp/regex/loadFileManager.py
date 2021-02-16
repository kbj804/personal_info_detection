import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


class loadFileManager:
    # 파일 이름, 확장자 분리
    def __init__(self, path) -> None:
        # dir_path = os.getcwd()
        basename = os.path.basename(path)
        self.name, self.ext = os.path.splitext(basename)

    # 확장자 별 데이터 오픈
    # pdf, hwp, ppt, docx, ....

    def read_pdf(self, path):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        
        f = open('./out.html', 'wb')
        device = HTMLConverter(rsrcmgr, f, codec=codec, laparams=laparams)
        # device = TextConverter(rsrcmgr, f, codec=codec, laparams=laparams)
        fp = open(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0 #is for all
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        fp.close()
        device.close()
        str = retstr.getvalue()
        retstr.close()
        f.close()
        
        return str

    def read_hwp():
        pass

    def read_ppt():
        pass

    def read_docx():
        pass

    def read_exel():
        pass

    read_function = {
        'pdf': read_pdf,
        'hwp': read_hwp,
        'ppt': read_ppt,
        'docx': read_docx,
        'exel': read_exel

    }