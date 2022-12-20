import PyPDF2
import os
import re
import logging


def set_logs():
    logger = logging.getLogger('PyPDF2')
    logger.setLevel(logging.ERROR)


def get_chars_stats():
    set_logs()
    print()
    print('Getting statistics..')

    files = os.listdir('./pdfs')
    list_of_words = []
    list_of_chars = []
    list_of_chars_wo_spaces = []

    for idx, file in enumerate(files, 1):
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
            print(f'File {idx}')
    
    return files, list_of_words, list_of_chars, list_of_chars_wo_spaces


def count_words(word):
    set_logs()
    print()
    print('Counting words..')

    files = os.listdir('./pdfs')
    counted_words = []

    for idx, file in enumerate(files, 1):
        with open(f'./pdfs/{file}', 'rb') as pdf_file:
            ReadPDF = PyPDF2.PdfFileReader(pdf_file, strict=False)
            pages = ReadPDF.numPages

            words_count = 0

            for page in range(pages):
                pageObj = ReadPDF.getPage(page)
                data = pageObj.extract_text()
                words_count += sum(1 for match in re.findall(rf'\b{word}\b', data, flags=re.I))

            counted_words.append(words_count)
        
        print(f'File: {idx}')
    
    return counted_words
