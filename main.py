from modules.papers import collect_data, download_pdf
from modules.calculation import get_chars_stats, count_words
from modules.data_analysis import get_statistics, create_dataframe, draw_plot
import sys
import getopt
import shutil
import os


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
        option = input('Delete existing files? (y/n) -> ')
        if option == 'y':
            folder = './pdfs'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

        ids = collect_data(arg_download, arg_keyword)
        download_pdf(ids)

    if arg_stats == 'y':
        pdfs, words, chars, chars_wo_spaces = get_chars_stats('./pdfs')
        df = create_dataframe(File = pdfs, Words = words, Chars = chars, Chars_without_spaces = chars_wo_spaces)
        with open('keyword.txt', 'r') as f:
            content = f.read()
            finded_words = count_words(content, './pdfs')
            df['Finded_keywords'] = finded_words
            print(df)
    

    if arg_count_word != '':
        finded_words = count_words(arg_count_word, './pdfs')
        try:
            df['Finded_words'] = finded_words
            print(df)
        except:
            pdfs, words, chars, chars_wo_spaces = get_chars_stats('./pdfs')
            df = create_dataframe(File = pdfs, Finded_words = finded_words)
            print(df)

    if arg_stats == 'y' or arg_count_word != '':
        print('\nDo you want to visualize data (0) or get statistics (1)?')
        
        answer = input('-> ')

        if answer == '0':
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
                    temp = []

                    for c in columns:
                        temp.append(df.columns[c])

                    new = df[temp]

                    plot_type = input('Which plot do you want to draw? (plot / hist) -> ')
                    title = input('Set title -> ')
                    xlabel = input('Set xlabel -> ')
                    ylabel = input('Set ylabel -> ')
                    draw_plot(plot_type, new, title, xlabel, ylabel)
                    break

                print(columns)
        elif answer == '1':
            for i, c in enumerate(df.columns):
                print(f'{i}: {c}')

            print(f'Choose columns 1 - {len(df.columns)-1} (-1 to exit):')
            while True:
                column = input('-> ')
                if column == '-1':
                    break
                elif column.isdigit() and int(column) >=1 and int(column) < len(df.columns):
                    print(get_statistics(df, df.columns[int(column)]))


if __name__ == '__main__':
    main(sys.argv)
