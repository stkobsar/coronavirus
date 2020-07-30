import


def pl_increment_cases(csv, field="total_users"):

    df_coronavirus = pd.read_csv(csv)
    condition = df_coronavirus["location"].str.lower() == country.lower()  # str.lower() retrieve en minuscula. Esto permite que le usuario pase spain como quiera
    df_filtered = df_coronavirus[condition]
    df_filtered_na = df_filtered.fillna(0)

    increment_list = []
    list_cases = df_filtered_na[field].values
    for idx, case in enumerate(list_cases):
        list_cases_val = list_cases[idx+1]
        increment =   - case
        increment_list.append(increment)


    list_date = range(len(list_cases))

    plt.scatter(list_date, list_cases)
    output = "cases_date_{}.png".format(country)
    if savefig:
        plt.savefig(output)
    else:
        pass

    return output