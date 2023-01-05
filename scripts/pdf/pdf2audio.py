import pyttsx3,PyPDF2

#insert name of pdf file to be converted 
pdfreader = PyPDF2.PdfFileReader(open('e-book.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    
#choose a name for the output file
speaker.save_to_file(clean_text, 'converted.mp3')
voices = engine.getProperty('voices')
speaker.runAndWait()

speaker.stop()
