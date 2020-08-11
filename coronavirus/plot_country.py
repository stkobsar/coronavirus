import matplotlib.pyplot as plt
import pandas as pd
import coronavirus.custom_errors as ce

def pl_country_cases(country, csv, field="total_cases", savefig=True):
    """
    Description: Plot country cases by days since pandemic started
    :param country: country entered by the user
    :param csv: csv with the data
    :param field: the field in dataset
    :param savefig: Save plot created trough data
    :return: output plot
    """
    df_coronavirus = pd.read_csv(csv)
    paises = df_coronavirus["location"].unique()


    condition = df_coronavirus["location"].str.lower() == country.lower() #str.lower() retrieve en minuscula. Esto permite que le usuario pase spain como quiera
    df_filtered = df_coronavirus[condition]

    if df_filtered.empty:
        similar_country = ce.similar_name_country(country, paises)
        raise ce.EmptyDataFrame(f'The name of country is not in the list of countries. Try to one of these {paises}. Did you mean {similar_country}?')

    df_filtered_na = df_filtered.fillna(0)
    list_cases = df_filtered_na[field].values
    list_date = range(len(list_cases))
    #list_date = df_filtered_na["date"].values
    plt.scatter(list_date, list_cases)
    output = "cases_date_{}.png".format(country)
    if savefig:
        plt.savefig(output)
    else:
        pass

    return output