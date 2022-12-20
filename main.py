import papers
import calculation


if __name__ == '__main__':
    titles, urls, ids = papers.collect_data()
    papers.download_pdf(ids)
    pdfs, words, chars, chars_wo_spaces = calculation.get_chars_stats()
    words = calculation.count_words('introduction')
