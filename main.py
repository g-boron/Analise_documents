import papers
import calculation
import data_analysis
import sys
import getopt


def main(argv):
    arg_download = ''
    arg_collect = ''
    arg_stats = ''
    arg_count_word = ''
    arg_help = f'{argv[0]} -d / --download <number of papers> -c / --collect <y/n> -s / --stats <y/n> -w / --count_word <word>'

    try:
        opts, args = getopt.getopt(argv[1:], 'hd:c:s:w:', ['help', 'download=', 'collect=', 'stats=', 'count_word='])
    except:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(arg_help)
            sys.exit(2)
        elif opt in ('-d', '--download'):
            arg_download = arg
        elif opt in ('-c', '--collect'):
            arg_collect = arg
        elif opt in ('-s', '--stats'):
            arg_stats = arg
        elif opt in ('-w', '--count_word'):
            arg_count_word = arg

    print('download', arg_download)
    print('collect', arg_collect)
    print('stats', arg_stats)
    print('count_word', arg_count_word)

    #titles, urls, ids = papers.collect_data()
    #papers.download_pdf(ids)
    '''pdfs, words, chars, chars_wo_spaces = calculation.get_chars_stats()
    finded_words = calculation.count_words('computer')

    df = data_analysis.create_dataframe(Url = urls, Title = titles, Words = words, Chars = chars, Chars_without_spaces = chars_wo_spaces, Finded_words = finded_words)
    '''

if __name__ == '__main__':
    main(sys.argv)
