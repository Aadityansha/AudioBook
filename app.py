# modules
import pyttsx3
import PyPDF2

# configurations of engine
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty(rate, 160)
engine.setProperty('voice', voices[1].id)

# reading PDF page by page
with open('periodic-classification-of-elements.pdf', mode='rb') as book:
    reader = PyPDF2.PdfFileReader(book)
    page_no = 0
    for page in reader.pages:
        page = reader.getPage(page_no)
        engine.say(page.extractText())
        engine.runAndWait()
        page_no = page_no + 1