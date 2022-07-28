import os.path
import csv
# import pdftotext
import tabula
import pandas as pd

#Load your PDF
with open(r"C:\Users\Dell\Documents\Python Test\PdfToCsv\VTN_FCT_2007.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f)
    # pdf = tabula.read_pdf(f, pages = 'all')
    # pdf = tabula.read_pdf(f, pages = 'all')[2].
    pdf = tabula.read_pdf(f, pages = 'all')[14]

# print(pdf)
# print(type(pdf))
# Save all text to a txt file.
with open('VTN_FCT.txt', 'w', encoding="utf-8") as f:

    pd.concat(pdf).to_csv(f)
    # f.write("\n\n".join(pdf))
    # dfAsString = pdf.to_string(header=False, index=False)
    # f.write(dfAsString)

save_path = "C:\\Users\\Dell\\Documents\\Python Test\\PdfToCsv\\"

completeName_in = os.path.join(save_path, 'crimestory' + '.txt')
completeName_out = os.path.join(save_path, 'crimestoryycsv' + '.csv')

file1 = open(completeName_in)
In_text = csv.reader(file1, delimiter=',')

file2 = open(completeName_out, 'w')
out_csv = csv.writer(file2)

file3 = out_csv.writerows(In_text)

file1.close()
file2.close()