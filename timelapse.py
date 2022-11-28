import PyPDF2
import os
from PIL import Image
from PyPDF2 import PdfReader

# if os.path.exists('C:\\Users\\sseve\\Pictures\\20221128-full-color-ice-chart.pdf'):
#   print("The file exist")
# else:
#   print("The file does not exist")

print("Select starting date: ")

# reader = PdfReader("example.pdf")
reader = PdfReader('C:\\Users\\sseve\\Pictures\\New folder\\20221128-full-color-ice-chart.pdf')

page = reader.pages[0]
print("Select ending date: ")

count = 0

# with open('C:\\Users\\sseve\\Pictures\\New folder\\20221128-full-color-ice-chart.pdf', 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#     print(f'Number of Pages in PDF File is {pdf_reader.getNumPages()}')

for image_file_object in page.images:
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)
        count += 1

print(page.extract_text(0))
print(count)

    #     # extracting images from the 1st page
    # page0 = pdf_reader.getPage(0)

    # if '/XObject' in page0['/Resources']:
    #     xObject = page0['/Resources']['/XObject'].getObject()

    #     for obj in xObject:
    #         if xObject[obj]['/Subtype'] == '/Image':
    #             size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
    #             data = xObject[obj].getData()
    #             if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
    #                 mode = "RGB"
    #             else:
    #                 mode = "P"

    #             if '/Filter' in xObject[obj]:
    #                 if xObject[obj]['/Filter'] == '/FlateDecode':
    #                     img = Image.frombytes(mode, size, data)
    #                     img.save(obj[1:] + ".png")
    #                 elif xObject[obj]['/Filter'] == '/DCTDecode':
    #                     img = open(obj[1:] + ".jpg", "wb")
    #                     img.write(data)
    #                     img.close()
    #                 elif xObject[obj]['/Filter'] == '/JPXDecode':
    #                     img = open(obj[1:] + ".jp2", "wb")
    #                     img.write(data)
    #                     img.close()
    #                 elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
    #                     img = open(obj[1:] + ".tiff", "wb")
    #                     img.write(data)
    #                     img.close()
    #             else:
    #                 img = Image.frombytes(mode, size, data)
    #                 img.save(obj[1:] + ".png")
    # else:
    #     print("No image found.")
    
    # # print(f'PDF Metadata is {pdf_reader.documentInfo}')
    # # print(f'PDF File Author is {pdf_reader.documentInfo["/Author"]}')
    # # print(f'PDF File Creator is {pdf_reader.documentInfo["/Creator"]}')

