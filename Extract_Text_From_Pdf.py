import PyPDF2
a = PyPDF2.PdfFileReader('CV.pdf')
print(a.documentInfo)
print(a.getNumPages())
str = ""
for i in range(1,1):
    str += a.getPage(i).extractText()
with open("Final_Output.txt", "w", encoding='utf-8') as f:
    f.write(str)