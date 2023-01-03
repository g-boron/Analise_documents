import main
import pytest


def test_options(download, keyword, stats, count_words):
    assert download == '1'
    assert keyword == 'test'
    assert stats == 'y'
    assert count_words == 'testing'