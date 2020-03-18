import matplotlib.pyplot as plt
import pandas as pd

def pl_country_cases(country, csv, savefig=True):
    df_coronavirus = pd.read_csv(csv)
    condition = df_coronavirus["location"].str.lower() == country.lower() #str.lower() retrieve en minuscula. Esto permite que le usuario pase spain como quiera
    df_filtered = df_coronavirus[condition]
    df_filtered_na = df_filtered.fillna(0)
    list_cases = df_filtered_na["new_cases"].values
    list_date = df_filtered_na["date"].values
    plt.scatter(list_date, list_cases)
    output = "cases_date_{}.png".format(country)
    if savefig:
        plt.savefig(output)
    else:
        pass

    return output