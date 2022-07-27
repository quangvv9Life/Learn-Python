import os.path
import csv
import PyPDF2
import tabula
import pandas as pd
import io


with io.open(r"C:\Users\Dell\Documents\Python Test\PdfToCsv\VTN_FCT_2007.pdf", "rb") as f:

    pagez = [14,15]
    pdfReader = PyPDF2.PdfFileReader(f) 
    result = pdfReader.index('\n')
print(result)