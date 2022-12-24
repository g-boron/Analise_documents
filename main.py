import papers
import calculation
import data_analysis
import sys
import getopt


def main(argv):
    arg_download = ''
    arg_keyword = ''
    arg_stats = ''
    arg_count_word = ''
    arg_help = f'{argv[0]} -d | --download <number of papers> -k | --keyword <keyword> -s | --stats <y/n> -w | --count_words <word>'

    try:
        opts, args = getopt.getopt(argv[1:], 'hd:k:s:w:', ['help', 'download=', 'keyword=', 'stats=', 'count_word='])
    except:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(arg_help)
            sys.exit(2)
        elif opt in ('-k', '--keyword'):
            arg_keyword = arg
        elif opt in ('-d', '--download'):
            arg_download = arg
        elif opt in ('-s', '--stats'):
            arg_stats = arg
        elif opt in ('-w', '--count_word'):
            arg_count_word = arg

    if arg_download != '' and arg_keyword != '' and arg_download.isnumeric() and int(arg_download) > 0:
        ids = papers.collect_data(arg_download, arg_keyword)
        papers.download_pdf(ids)

    if arg_stats == 'y':
        pdfs, words, chars, chars_wo_spaces = calculation.get_chars_stats()
        df = data_analysis.create_dataframe(File = pdfs, Words = words, Chars = chars, Chars_without_spaces = chars_wo_spaces)
        with open('keyword.txt', 'r') as f:
            content = f.read()
            finded_words = calculation.count_words(content)
            df['Finded_keywords'] = finded_words
            print(df)
    

    if arg_count_word != '':
        finded_words = calculation.count_words(arg_count_word)
        try:
            df = df.drop('Finded_keywords', axis=1)
            df['Finded_words'] = finded_words
            print(df)
        except:
            df = data_analysis.create_dataframe(Finded_words = finded_words)
            print(df)

    if arg_stats == 'y' or arg_count_word != '':
        print('\nDo you want to visualize data? (y/n)')
        
        while True:
            answer = input('-> ')

            if answer == 'y':
                columns = []

                for i, c in enumerate(df.columns):
                    print(f'{i}: {c}')

                print(f'Choose columns 1 - {len(df.columns)-1} (-1 to exit, OK to accept):')
                while True:
                    column = input('-> ')
                    if column == '-1':
                        break
                    elif column.isdigit() and int(column) >=1 and int(column) < len(df.columns):
                        if int(column) not in columns:
                            columns.append(int(column))
                    elif column == 'OK':
                        print("OK")
                        break
                    print(columns)

                temp = []

                for c in columns:
                    temp.append(df.columns[c])

                new = df[temp]
                data_analysis.draw_plot('plot', new, 'tytul', 'x', 'y')
                break
            elif answer == 'n':
                print('No')
                break

if __name__ == '__main__':
    main(sys.argv)
