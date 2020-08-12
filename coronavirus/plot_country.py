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
    condition = df_coronavirus["location"].str.lower() == country.lower() #str.lower() retrieve en minuscula. Esto permite que le usuario pase spain como quiera
    df_filtered = df_coronavirus[condition]

    list_of_countries = df_coronavirus["location"].unique()

    if df_filtered.empty:
        similar_country = ce.similar_name_country(country, list_of_countries)
        raise ce.EmptyDataFrame(f'The name of country is not in the list of countries. Try to one of these {list_of_countries}. Did you mean {similar_country}?')

    df_filtered_na = df_filtered.fillna(0)
    list_cases = df_filtered_na[field].values
    list_dates = range(len(list_cases))

    ### Plot ###

    plt.scatter(list_dates, list_cases)
    plt.xlabel("Days since covid started")
    plt.ylabel("COVID official cases")
    plt.title("Analysis of coronavirus data in a single country")

    curr_date = pd.to_datetime('today').date()
    output = f"cases_{curr_date}_{country}.png"

    if savefig:
        plt.savefig(output)
    else:
        pass

    return output