import pandas as pd
from matplotlib import pyplot as plt


def get_statistics(df, name):
    return {
        'mean': df[name].mean(),
        'min': df[name].min(),
        'max': df[name].max()
        }


def create_dataframe(**kwargs):
    z = list(zip(*kwargs.values()))
    return pd.DataFrame(z, columns=kwargs.keys())


def draw_plot(plot_type, data, title, xlabel, ylabel):
    if plot_type == 'hist':
        plt.hist(data, bins=5)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
    elif plot_type == 'plot':
        plt.Figure()
        data.plot()
        plt.legend(loc='best')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()


def save_dataframe(format, df, file_name):
    if format == 'json':
        df.to_json(f'{file_name}.json')
    elif format == 'csv':
        df.to_csv(f'{file_name}.csv', index=False, sep=';')
    else:
        raise Exception('Invalid format!')
