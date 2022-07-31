import os.path
import csv
import PyPDF2
import tabula
import pandas as pd
import io
import re
import openpyxl

# Define a function called "append data to csv"

# from csv import writer
def append_element_of_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', encoding="utf-8") as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def append_element_of_list_as_row_not_iterable(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', encoding="utf-8") as write_obj:
        # Create a writer object from csv module
        # csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        write_obj.write(list_of_elem)

# Dell Desktop : Load your PDF
with io.open(r"G:\tryPython\Python Test\PdfToCsv\VTN_FCT_2007.pdf", "rb") as f:
# Dell Laptop : Load your PDF
# with io.open(r"C:\Users\Dell\Documents\Python Test\PdfToCsv\VTN_FCT_2007.pdf", "rb") as f:
    # pagez = list(range(13,36+1))
    # pagez = list(range(38,64+1))
    # pagez = list(range(66,99+1))
    # pagez = list(range(102,228+1))
    # pagez = list(range(230,286+1))
    # pagez = list(range(288,302+1))
    # pagez = list(range(304,386+1))
    # pagez = list(range(388,447+1))
    # pagez = list(range(449,460+1))
    # pagez =  list(range(462,471+1)) 
    pagez = list(range(473,494+1)) 
    # pagez = list(range(496,523+1))   
    # pagez = list(range(525,548+1)) 
    # pagez =  list(range(550,566+1))

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
patern1 = r'(?:sè:)+\n\d+'
for i in range(len(output)):
    # innerList = output[i].split("\n")
    innerList = re.findall(patern,output[i])
    if innerList != []:    
        try:
            Listz.append(innerList[0])
        except IndexError:
            break
    elif innerList == []:  
        innerList = re.findall(patern1, output[i])
        try:
            Listz.append(innerList[0])
        except IndexError:
            break

# headers = [  "Nutrients", "Unit", "Value", "Source", "Placeholder", "Nutrients", "Unit", "Value", "Source", "Ingre_code" ]
with open("Extract_1.csv", "a") as file1:
    # for i in range(len(pagez)):
    for i, j in enumerate(pagez):
    # for i in pagez:
        # Handle index out of range error :
        try:
            append_element_of_list_as_row_not_iterable("Extract_1.csv", Listz[i])
        except IndexError:
            break
        # Handle index out of range error :
        try:
        # Corresponding tables are behind by x pages
            # pdf[i+2].to_csv('Extract_1.csv', mode = "a", columns = headers) #, sep = ',', mode='a', index= False,header=False)
        # For pagez = list(range(13,36+1)) and pagez = list(range(38,64+1))
            # pdf[i+2].to_csv('Extract_1.csv', mode = "a")
        # For pagez = 66-99, 288-302, 
            # pdf[i].to_csv('Extract_1.csv', mode = "a")
        # For pagez = 102-228, 230-286, 305-386, 449-460
# -            pdf[i+1].to_csv('Extract_1.csv', mode = "a")
        # For pagez = 462-471, 473-494, 496-523, 525-548
            pdf[i+2].to_csv('Extract_1.csv', mode = "a")
        except IndexError:
            break
# Open the output file and filter column A - ingre's code to check
# wb = openpyxl.load_workbook('Extract_1.csv')
# ws1 = wb.active

# ws1.auto_filter.ref = 'A:A'
# ws1.auto_filter.add_filter_column(0, ['sÃ¨'])