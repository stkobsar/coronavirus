import matplotlib.pyplot as plt
import pandas as pd
import os


def get_histograms(csv):
    """
    Author: Stefanie Kobsar
    Description: Preprocessing of outlier values
    :param csv: Resulting csv from scrapping
    :return: void
    """

    df_coronavirus = pd.read_csv(csv)
    description = df_coronavirus.describe()

    analysis = "analysis_histograms"

    if not os.path.exists(analysis):
        os.mkdir(analysis)
    description.to_csv(os.path.join(analysis, "description_data.csv"))

    df_types_variable = df_coronavirus.dtypes
    df_types_variable.to_csv(os.path.join(analysis, "type_of_variables.csv"))

    number_of_nans = df_coronavirus.isna().sum()
    number_of_nans.to_csv(os.path.join(analysis, "number_of_nans.csv"))

    ####All histograms#####

    df = df_coronavirus

    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
            df.hist(column=col)
            plt.savefig(os.path.join(analysis, f"{col}.png"))
        except ValueError:
            print('This column can not be represented as an histogram')

