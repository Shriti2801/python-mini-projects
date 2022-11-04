import PyPDF2
file = open("C:/Users/shrit/Downloads/Python+Syntax+Cheat+Sheet+Booklet.pdf",'rb')
fileReader = PyPDF2.PdfFileReader(file)
page = fileReader.getPage(1)
print(page.extractText())


