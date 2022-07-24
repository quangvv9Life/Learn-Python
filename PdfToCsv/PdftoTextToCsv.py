import os.path
import csv
import pdftotext
#Load your PDF
with open("VTN_FCT_2007.pdf", "rb") as f:
   pdf = pdftotext.PDF(f)

# Save all text to a txt file.
with open('crimestory.txt', 'w') as f:
    f.write("\n\n".join(pdf))

save_path = "/home/mayureshk/PycharmProjects/NLP/"

completeName_in = os.path.join(save_path, 'crimestory' + '.txt')
completeName_out = os.path.join(save_path, 'crimestoryycsv' + '.csv')

file1 = open(completeName_in)
In_text = csv.reader(file1, delimiter=',')

file2 = open(completeName_out, 'w')
out_csv = csv.writer(file2)

file3 = out_csv.writerows(In_text)

file1.close()
file2.close()