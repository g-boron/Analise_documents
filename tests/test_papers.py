from modules.papers import collect_data, download_pdf
import os


def test_collect_data():
    amount = 1
    keyword = 'test'

    ids = collect_data(amount, keyword)

    assert ids != []


def test_download_pdf():
    amount = 1
    keyword = 'test'
    ids = collect_data(amount, keyword)
    dir = './test_pdfs'

    download_pdf(ids, dir)

    assert len(os.listdir(dir)) != 0