import fitz
import io
import os, shutil
import zipfile
from . import settings
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def makezipfile(dir_name):
    # filePaths = retrieve_file_paths(dir_name)
    filess = os.listdir(dir_name)
    # writing files to a zipfile
    zip_file = zipfile.ZipFile(dir_name + '.zip', 'w')
    with zip_file:
        # writing each file one by one
        for file in filess:
            zip_file.write(dir_name + '/' + file)
        
    # print(dir_name + '.zip file is created successfully!')

def delete_spec(del_path):
    test = os.listdir(del_path)

    for item in test:
        if item.endswith(".pdf"):
            os.remove(os.path.join(del_path, item))
        if item.endswith(".zip"):
            os.remove(os.path.join(del_path, item))
    
def delete_all(del_path):
    for filename in os.listdir(del_path):
        file_path = os.path.join(del_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def pdf2image(in_path,out_path):
    doc = fitz.open(in_path)
    for pg in range(doc.pageCount):
        page = doc[pg]
        rotate = int(0)
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)   
        pm = page.getPixmap(matrix=trans, alpha=False)
        pm.writePNG(out_path + '/page_%s.png' % pg)

def pdf2text(in_path, out_path):
    '''Convert pdf content from a file path to text

    :path the file path
    '''
    with open(in_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle, codec='utf-8', laparams=LAParams())
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
 
            text = fake_file_handle.getvalue()
            with open(out_path +'/file.txt',"a+") as f:
                f.write(text + "\n")
 
            # close open handles
            converter.close()
            fake_file_handle.close() 

# def pdftodocx(in_path,out_path): 
#     docx_file = out_path + '/file.docx'
#     pages=[]
#     pdf = Reader(in_path)
#     docx = Writer()

#     # parsing arguments
#     pdf_len = len(pdf)
#     if pages: 
#         pdf_pages = [pdf[int(x)] for x in pages]
#     else:
#         end = pdf_len-1
#         pdf_pages = pdf[int(0):int(end)]

#     # process page by page
#     for page in pdf_pages:
#         # print(f"Processing {page.number}/{pdf_len-1}...")
#         # parse layout
#         layout = pdf.parse(page)        
#         # create docx
#         docx.make_page(layout)

#     # save docx, close pdf
#     docx.save(docx_file)
#     pdf.close()