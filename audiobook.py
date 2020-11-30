import pyttsx3
import PyPDF2
book=open('the_phoenix_project.pdf','rb')
readPDF=PyPDF2.PdfFileReader(book)

#to get the number of pages
num_pages=readPDF.numPages
print(num_pages)

speaker=pyttsx3.init()
for num in range(8,num_pages):
    page=readPDF.getPage(8)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
