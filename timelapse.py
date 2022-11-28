# import module
import os
import tempfile
from pdf2image import convert_from_path
from PyPDF2 import PdfFileWriter, PdfFileReader

path="/home/safka/timelapse-sea-ice-fmi/"
output_folder_path="/home/safka/timelapse-sea-ice-fmi/output/"
pdfname=path+"peedeeaff.pdf"
inputpdf = PdfFileReader(open(pdfname,"rb"))
maxPages = inputpdf.numPages
print("Number of pages in PDF="+str(maxPages))
i = 1
for page in range(1, maxPages, 10):
    pil_images = convert_from_path(pdfname, dpi=200, first_page=page,
                                                     last_page=min(page + 10 - 1, maxPages), fmt= 'jpg',
                                                     thread_count=1, userpw=None,
                                                     use_cropbox=False, strict=False)
    for image in pil_images:
        image.save(output_folder_path+'output' + str(i) + '.jpg', 'JPEG')
        i = i + 1
