'''
pip install pdfminer.six
pip install 'olefile'  or '-U olefile'
pip install python-pptx
pip install python-docx
'''
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import olefile
from pptx import Presentation
from docx import Document

class loadFileManager:
    # 파일 이름, 확장자 분리
    def __init__(self, path):
        # dir_path = os.getcwd()
        self.path = path
        basename = os.path.basename(self.path)
        self.name, self.dotext = os.path.splitext(basename)
        self.ext = self.dotext.replace(".",'',1)

        self.data = ''

        # 읽을 수 있는 파일인지 검사하고 읽을 수 있으면 data입력
        if self.check_ext():
            self.data = self.read_file()

        else:
            print("여기론 안와")
            pass
    
    # 확장자에 맞는 read 함수로 매핑
    def read_file(self):
        result = self.read_function[self.ext](self)
        return result 

    # 읽을 수 있는 확장자인가 검사
    def check_ext(self):
        try:
            if self.read_function[self.ext]:
                return True
            else:
                print("@ # @ # {} For Debugging... @ # @ #".format(self.ext))
                return False

        except Exception as e:
            print("####ERROR#### {0} dose not exist in ext Dictionary".format(e))

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

    def read_hwp(self):
        f = olefile.OleFileIO(self.path)
        encoded_text = f.openstream('PrvText').read()
        decoded_text = encoded_text.decode('UTF-16')
        
        return decoded_text

    def read_pptx(self):
        pptxdoc = Presentation(self.path)
        fullText = []
        for slide in pptxdoc.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    fullText.append(paragraph.text)
                    
        return '\n'.join(fullText)

    def read_docx(self):
        # with open(self.path, 'rb') as f:
        #     source_stream = StringIO(f.read())
        document = Document(self.path)
        fullText = []
        for para in document.paragraphs:
            fullText.append(para.text)
        # source_stream.close()

        return '\n'.join(fullText)

    def read_exel():
        pass

    def read_txt(self):
        with open(self.path, 'r', encoding='UTF8') as f:
            data = f.read()
            return data
    
    def read_html(self):
        pass

    read_function = {
        'pdf': read_pdf,
        'hwp': read_hwp,
        'pptx': read_pptx,
        'docx': read_docx,
        'exel': read_exel,
        'txt': read_txt,
        'html': read_html
    }
    
    

# a = loadFileManager('hwp_sample.hwp')
# print(a.data)
