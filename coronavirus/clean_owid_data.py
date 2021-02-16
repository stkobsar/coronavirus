import pandas as pd

def clean_data(csv):
    """
    Description: Substitutes Nan values in selected columns by
    either zeroes or the previous visible value per country in
    the main OWID coronavirus dataframe
    :param owid_data: OWID main coronavirus dataset in a pandas dataframe format
    :return: OWID main coronavirus dataframe with Nan values corrected
    """

    working_df = pd.read_csv(csv)

    #print(working_df)
    working_df["date"] = pd.to_datetime(working_df["date"])
    #print(working_df)
    working_df = working_df.sort_values(by=['continent', 'location', 'date'])
    working_df = working_df.set_index("date")

    working_df[working_df.columns[working_df.columns.str.startswith(tuple(["new", "weekly"]))]] = working_df[working_df.columns[working_df.columns.str.startswith(tuple(["new", "weekly"]))]].fillna(value=0)

    df_list = []

    for l in working_df.location.unique():
        temporary_df = working_df.loc[working_df['location'] == l]
        temporary_df[temporary_df.columns[temporary_df.columns.str.startswith(tuple(["total"]))]] = temporary_df[temporary_df.columns[temporary_df.columns.str.startswith(tuple(["total"]))]].fillna(method='ffill').fillna(value=0)
        df_list.append(temporary_df)
    result = pd.concat(df_list)

    return(result)