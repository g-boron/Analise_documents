import papers
import calculation
import data_analysis
import pandas as pd


if __name__ == '__main__':
    titles, urls, ids = papers.collect_data()
    #papers.download_pdf(ids)
    pdfs, words, chars, chars_wo_spaces = calculation.get_chars_stats()
    finded_words = calculation.count_words('computer')

    df = pd.DataFrame(list(zip(urls, titles, words, chars, chars_wo_spaces, finded_words)), columns = ['Url', 'Title', 'Words', 'Chars', 'Chars without spaces', 'Finded words'])
    print(df)
    print(data_analysis.get_statistics(df, 'Words'))
    print(data_analysis.get_statistics(df, 'Chars'))
    print(data_analysis.get_statistics(df, 'Chars without spaces'))
    print(data_analysis.get_statistics(df, 'Finded words'))
    data_analysis.draw_plot(finded_words, 7)
