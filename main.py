import papers
import calculation
import data_analysis
import pandas as pd


if __name__ == '__main__':
    titles, urls, ids = papers.collect_data()
    #papers.download_pdf(ids)
    pdfs, words, chars, chars_wo_spaces = calculation.get_chars_stats()
    finded_words = calculation.count_words('computer')

    df = data_analysis.create_dataframe(Url = urls, Title = titles, Words = words, Chars = chars, Chars_without_spaces = chars_wo_spaces, Finded_words = finded_words)
    print(df)
    #b = df[['Chars', 'Chars without spaces']]
    #data_analysis.draw_plot('bar', b, 'Chars with and without spaces', 'Amount of papers', 'Amounts of chars')
