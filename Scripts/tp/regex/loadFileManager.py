import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


class loadFileManager:
    # 파일 이름, 확장자 분리
    def __init__(self, path):
        # dir_path = os.getcwd()
        self.path = path
        basename = os.path.basename(self.path)
        self.name, self.ext = os.path.splitext(basename)

    # 확장자 별 데이터 오픈
    # pdf, hwp, ppt, docx, ....

    def read_pdf(self):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        
        # f = open('./out.html', 'wb')
        # device = HTMLConverter(rsrcmgr, f, codec=codec, laparams=laparams)
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        
        with open(self.path, 'rb') as fp:
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            maxpages = 0 #is for all
            caching = True
            pagenos=set()
            
            for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
                interpreter.process_page(page)
            
            str = retstr.getvalue()

            fp.close()
        device.close()
        retstr.close()
        # f.close()
        
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

a = loadFileManager('t.pdf')

print(a.read_pdf())