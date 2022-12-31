from modules.calculation import get_chars_stats, count_words


def test_get_char_stats():
    pdfs, words, chars, chars_wo_spaces = get_chars_stats('./test_pdfs')

    assert pdfs == ['test_file.pdf']
    assert words == [3]
    assert chars == [15]
    assert chars_wo_spaces == [11]


def test_count_words():
    amount = count_words('file', './test_pdfs')

    assert amount == [1]