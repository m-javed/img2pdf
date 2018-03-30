import glob
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
from PIL import Image
import os


output_filename = 'Result'

extensions = ('*.jpg','*.png','*.gif')

imagelist=[]
for ext in extensions:
    imagelist.extend(glob.glob(ext))

pdf = FPDF()

print(imagelist)
for imagePath in imagelist:
    cover = Image.open(imagePath)
    width, height = cover.size
    if height > width:
        pdf = FPDF(unit = "mm", format = "A4")
        pdf.add_page()
        pdf.image(imagePath, 0, 0, 210, 297)
    elif width > height:
        pdf = FPDF("L", unit = "mm", format = "A4")
        pdf.add_page()
        pdf.image(imagePath, 0, 0, 297, 210)
    pdf.output(imagePath.split('.')[0] + '.pdf', 'F')

merger = PdfFileMerger()

pdfs = [imagepath.split('.')[0] + '.pdf' for imagepath in imagelist]

for pdf in pdfs:
   merger.append(open(pdf, 'rb'))
   os.remove(pdf)

with open(output_filename + '.pdf', 'wb') as fout:
    merger.write(fout)
