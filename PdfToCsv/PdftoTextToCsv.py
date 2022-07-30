import os.path
import csv
import PyPDF2
import tabula
import pandas as pd
import io
import re

# Define a function called "append data to csv"

# from csv import writer
def append_element_of_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', encoding="utf-8") as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

# Dell Desktop : Load your PDF
# with io.open(r"G:\tryPython\Python Test\PdfToCsv\VTN_FCT_2007.pdf", "rb") as f:
# Dell Laptop : Load your PDF
with io.open(r"C:\Users\Dell\Documents\Python Test\PdfToCsv\VTN_FCT_2007.pdf", "rb") as f:
    pagez = list(range(13,36+1))
    # pagez = list(range(38,64+1))
    # pagez = list(range(66,99+1))
    # pagez = list(range(85,99+1))
    # pagez = list(range(97,99+1))
    # pagez = 98
    # pagez = list(range(102,228+1))
    # pagez = list(range(231,286+1))
    # pagez = list(range(288,302+1))
    # pagez = list(range(305,386+1))
    
    #No need encode - majority
    try:
        pdf = tabula.read_pdf(f, pages = pagez)
    except UnicodeDecodeError:
    #Need encode - minority
        pdf = tabula.read_pdf(f, pages = pagez, encoding = "ISO-8859-1")
 
    pdfReader = PyPDF2.PdfFileReader(f) 
    output = []
    for i in pagez:
        pageObj = pdfReader.getPage(i)
        output.append(pageObj.extractText())

Listz = []
patern = r'(?:sè:)+\d+'
patern1 = r'(?:sè:)+\\n\d+'
for i in range(len(output)):
    # innerList = output[i].split("\n")
    innerList = re.findall(patern,output[i])
    if innerList == []:     
        innerList = re.findall(patern1, output[i])
    try:
        Listz.append(innerList[0])
    except IndexError:
        break

with open("Extract_1.csv", "a") as file1:
    # for i in range(len(pagez)):%
    for i, j in enumerate(pagez):
    # for i in pagez:
        append_element_of_list_as_row("Extract_1.csv", Listz[i])
        # Corresponding tables are behind by 2 pages
        try:
            pdf[i+2].to_csv('Extract_1.csv', mode = "a") #, sep = ',', mode='a', index= False,header=False)
        except IndexError:
            break
