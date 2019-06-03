from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from pathlib import Path
import requests


def convert_pdf_to_txt(path,name):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    
    File_object = open(name,"w+", encoding='utf8', errors='ignore')
    File_object.write(text)
    File_object.close()
    print("Download Complete")

    fp.close()
    device.close()
    retstr.close()
    return text.lower().split()

def save_pdf(path,name):
    filename = Path('Pdfs/temp.pdf')
    
    response = requests.get(path)
    print("Downloading PDF")
    try:
        filename.write_bytes(response.content)
        return convert_pdf_to_txt('Pdfs/temp.pdf',name)

    except:
        print("PDF does not exist")

    return {}
        