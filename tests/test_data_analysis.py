from modules.data_analysis import create_dataframe, get_statistics, draw_plot
import pandas as pd
from pandas.testing import assert_frame_equal
from unittest.mock import patch


def test_create_dataframe():
    files = ['f1.txt', 'f2.txt']
    df = create_dataframe(File = files)
    excepted = pd.DataFrame({'File': ['f1.txt', 'f2.txt']})
    assert_frame_equal(df, excepted)


def test_create_dataframe_many():
    files = ['f1.txt', 'f2.txt']
    authors = ['Andrew', 'Tom']
    sizes = [35, 250]
    df = create_dataframe(File = files, Author = authors, Size = sizes)
    excepted = pd.DataFrame({'File': ['f1.txt', 'f2.txt'], 'Author': ['Andrew', 'Tom'], 'Size': [35, 250]})
    assert_frame_equal(df, excepted)


def test_get_statistics():
    df = pd.DataFrame({'col1': [1, 2, 1], 'col2': [4, 5, 6]})
    result = get_statistics(df, 'col2')
    assert result == {'mean': 5, 'min': 4, 'max': 6}


def test_get_statistics_single():
    df = pd.DataFrame({'col1': [1]})
    result = get_statistics(df, 'col1')
    assert result == {'mean': 1, 'min': 1, 'max': 1}


@patch('matplotlib.pyplot.show')
def test_draw_plot(mock_show):
    plot_type = 'plot'
    data = pd.DataFrame({'Test': [1, 2, 3]})
    title = 'Testing'
    xlabel = 'Test x'
    ylabel = 'Test y'
    draw_plot(plot_type, data, title, xlabel, ylabel)


@patch('matplotlib.pyplot.show')
def test_draw_hist(mock_show):
    plot_type = 'hist'
    data = pd.DataFrame({'Test': [1, 2, 3]})
    title = 'Testing'
    xlabel = 'Test x'
    ylabel = 'Test y'
    draw_plot(plot_type, data, title, xlabel, ylabel)