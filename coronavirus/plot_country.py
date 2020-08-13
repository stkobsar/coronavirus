import matplotlib.pyplot as plt
import pandas as pd
import coronavirus.custom_errors as ce

def pl_country_cases(country, csv, field, savefig=True):
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
    list_of_fields = []
    for col_name in df_filtered.columns:
        list_of_fields.append(col_name)



    if field not in list_of_fields:
        similar_field = ce.similar_name_country(field, list_of_fields)
        raise ce.FieldError(f'The name of data field is not in the list of field. Try one of these {list_of_fields}. Did you mean {similar_field}?')



    if df_filtered.empty:
        similar_country = ce.similar_name_country(country, list_of_countries)
        raise ce.EmptyDataFrame(f'The name of country is not in the list of countries. Try to one of these {list_of_countries}. Did you mean {similar_country}?')


    df_filtered_na = df_filtered.fillna(0)
    list_cases = df_filtered_na[field].values
    list_dates = range(len(list_cases))

    ### Plot ###

    curr_date = str(pd.to_datetime('today').date())
    curr_date_custom = curr_date.replace('-', '')
    field_custom = field.replace('_', '')
    field_title = field.replace('_', ' ')

    plt.scatter(list_dates, list_cases)
    plt.xlabel("Days since COVID-19 start spreading")
    plt.ylabel(f"COVID-19 official cases of {field_title}")
    plt.title(f"COVID-19 data of {field_title} in {country}")

    ############

    curr_date = str(pd.to_datetime('today').date())
    curr_date_custom = curr_date.replace('-', '')
    field_custom = field.replace('_', '')

    output = f"{field_custom}_{curr_date_custom}_{country}.png"

    if savefig:
        plt.savefig(output)
    else:
        pass

    return output