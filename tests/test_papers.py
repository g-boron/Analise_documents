from modules.papers import collect_data, download_pdf
import os


def test_collect_data():
    amount = 1
    keyword = 'test'

    ids = collect_data(amount, keyword)

    assert ids != []


def test_download_pdf():
    if not os.path.exists('./test_pdfs'):
            os.makedirs('./test_pdfs')

    for filename in os.listdir('./test_pdfs'):
                file_path = os.path.join('./test_pdfs', filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

    amount = 1
    keyword = 'test'
    ids = collect_data(amount, keyword)
    dir = './test_pdfs'

    download_pdf(ids, dir)

    assert len(os.listdir(dir)) != 0