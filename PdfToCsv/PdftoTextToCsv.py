import os.path
import csv
import PyPDF2
import tabula
import pandas as pd
import io

#Load your PDF
with io.open(r"C:\Users\Dell\Documents\Python Test\PdfToCsv\VTN_FCT_2007.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f)
    # pdf = tabula.read_pdf(f, pages = 'all')
    # pdf = tabula.read_pdf(f, pages = 'all')[2]
    pagez = [14,15]
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
    
# print(Listz)
# print(pdf)
# print(type(pdf))
# Save all text to a txt file.



# for i in range(len(pdf)):
#     df = pd.DataFrame(pdf[i])
#     header_row = df.iloc[0]
#     df2 = pd.DataFrame(df.values[1:], columns=header_row)

#     print(df2)



# with open("Extract.csv", "a") as file1:
for i in range(len(pdf)):
    # pdf[i].to_csv("Extract.csv", mode = "a")
    pdf[i].to_csv('Extract.csv', mode = "a") #, sep = ',', mode='a', index= False,header=False)


with open('VTN_FCT.txt', 'w', encoding="utf-8") as f:

    pd.concat(pdf).to_csv(f)
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

