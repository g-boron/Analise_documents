import pandas as pd
from matplotlib import pyplot as plt


def get_statistics(df, name):
    return {
        'mean': df[name].mean(),
        'min': df[name].min(),
        'max': df[name].max()
        }


def draw_plot(data, amount):
    plt.hist(data, bins=amount)
    plt.show()