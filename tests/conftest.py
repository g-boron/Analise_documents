import pytest


def pytest_addoption(parser):
    parser.addoption('--download', action = 'store')
    parser.addoption('--keyword', action = 'store')
    parser.addoption('--stats', action = 'store')
    parser.addoption('--count_words', action = 'store')


@pytest.fixture(scope='session')
def download(request):
    download_value = request.config.option.download
    if download_value is None:
        pytest.skip()
    return download_value


@pytest.fixture(scope='session')
def keyword(request):
    keyword_value = request.config.option.keyword
    if keyword_value is None:
        pytest.skip()
    return keyword_value

    
@pytest.fixture(scope='session')
def stats(request):
    stats_value = request.config.option.stats
    if stats_value is None:
        pytest.skip()
    return stats_value


@pytest.fixture(scope='session')
def count_words(request):
    count_words_value = request.config.option.count_words
    if count_words_value is None:
        pytest.skip()
    return count_words_value