import numpy as np
from matplotlib import pylab
import matplotlib.pyplot as plt
from pylab import *
import scipy.stats as stats
import os
import pandas as pd

def get_qq_plot(csv):
    """
    Author: Stefanie Kobsar
    Description: Preprocessing of outlier values
    :param csv: Resulting csv from scrapping
    :return: void
    """

    df_coronavirus = pd.read_csv(csv)

    analysis = "analysis_qqplots"

    if not os.path.exists(analysis):
        os.mkdir(analysis)

    df = df_coronavirus

    for col in df.columns:
        try:
            fig, ax = plt.subplots()
            valores = pd.to_numeric(df[col])
            stats.probplot(valores, dist="norm", plot=ax)
            plt.savefig(os.path.join(analysis, f"{col}_qqplots.png"))
        except ValueError:
            print('Not able to return qqplot')
