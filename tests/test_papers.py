from modules.papers import collect_data


def test_collect_data():
    amount = 1
    keyword = 'test'

    ids = collect_data(amount, keyword)

    assert ids != []