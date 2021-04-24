import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

def correlation(file):
    data = pd.read_csv(file)
    
    # Drop empty columns and columns that only contain zeros
    data = data.dropna(axis=1).loc[:, (data != 0).any(axis=0)]

    corr = data.corr()
    ax = sns.heatmap(
        corr, 
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    )
    plt.show()

correlation('new-jersey-history.csv')
