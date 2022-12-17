import PyPDF2
import os


def get_chars_stats():
    files = os.listdir('./pdfs')
    list_of_words = []
    list_of_chars = []
    list_of_chars_wo_spaces = []

    for file in files:
        with open(f'./pdfs/{file}', 'rb') as pdf_file:
            ReadPDF = PyPDF2.PdfFileReader(pdf_file, strict=False)
            pages = ReadPDF.numPages

            total_words = 0
            total_chars = 0
            total_chars_wo_spaces = 0

            for page in range(pages):
                pageObj = ReadPDF.getPage(page)
                data = pageObj.extract_text()
                
                total_words += len(data.split())
                total_chars += len(list(data))
                wo_spaces = data.replace(' ', '')
                total_chars_wo_spaces += len(list(wo_spaces))

            list_of_words.append(total_words)
            list_of_chars.append(total_chars)
            list_of_chars_wo_spaces.append(total_chars_wo_spaces)
    
    return files, list_of_words, list_of_chars, list_of_chars_wo_spaces
