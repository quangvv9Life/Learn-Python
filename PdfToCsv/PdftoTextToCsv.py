import os.path
import csv
import PyPDF2
import tabula
import pandas as pd
import io

# Define a function called "append data to csv"

# from csv import writer
def append_element_of_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', encoding="utf-8") as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

#Load your PDF
with io.open(r"C:\Users\Dell\Documents\Python Test\PdfToCsv\VTN_FCT_2007.pdf", "rb") as f:
    # pagez = list(range(13,36+1))
    # pagez = list(range(38,64+1))
    # pagez = list(range(66,99+1))
    # pagez = list(range(85,99+1))
    pagez = list(range(97,99+1))
    pdf = tabula.read_pdf(f, pages = pagez)
    pdfReader = PyPDF2.PdfFileReader(f) 
    output = []
    for i in pagez:
        pageObj = pdfReader.getPage(i)
        output.append(pageObj.extractText())

Listz = []
for i in range(len(output)):
    innerList = output[i].split("\n")
    Listz.append(innerList[0])

with open("Extract.csv", "a") as file1:
    # for i in range(len(pagez)):%
    for i, j in enumerate(pagez):
    # for i in pagez:
        append_element_of_list_as_row("Extract.csv", Listz[i])
        # Corresponding tables are behind by 2 pages
        try:
            pdf[i+2].to_csv('Extract.csv', mode = "a") #, sep = ',', mode='a', index= False,header=False)
        except AttributeError:
            break
            
        
        

# print(Listz)
# print(pdf)
# print(type(Listz))
# print(type(pdf))
# Save all text to a txt file.

# for i in range(len(pdf)):
#     df = pd.DataFrame(pdf[i])
#     header_row = df.iloc[0]
#     df2 = pd.DataFrame(df.values[1:], columns=header_row)

#     print(df2)
# append_element_of_list_as_row("Extract.csv", Listz)

# with open('VTN_FCT.txt', 'w', encoding="utf-8") as f:

#     pd.concat(pdf).to_csv(f)
    # f.write("\n\n".join(pdf))
    # dfAsString = pdf.to_string(header=False, index=False)
    # f.write(dfAsString)

# save_path = "C:\\Users\\Dell\\Documents\\Python Test\\PdfToCsv\\"

# completeName_in = os.path.join(save_path, 'crimestory' + '.txt')
# completeName_out = os.path.join(save_path, 'crimestoryycsv' + '.csv')

# file1 = open(completeName_in)
# In_text = csv.reader(file1, delimiter=',')

# file2 = open(completeName_out, 'w')
# out_csv = csv.writer(file2)

# file3 = out_csv.writerows(In_text)

# file1.close()
# file2.close()

