import tabula
import pandas

PDFfilename2 = "VTN_FCT_2007.pdf"

df = tabula.read_pdf(PDFfilename2, pages = 'all')[0:10]

# tabula.io.convert_into("VTN_FCT_2007.pdf","VTN_FCT_2007.csv", output_format=  "csv", pages = 'all')



# df = PDFfilename2.encode('utf-8')

# print(tabula.read_pdf(df))
# print(type(df))
# tabula.convert_into(df, "VTN_FCT_EN.csv", output_format=  "csv", pages = 'all')

df.to_csv(r'C:\Users\Dell\Documents\12_MyfitnessPal\VTN_FCT_EN.csv', encoding='utf-8')