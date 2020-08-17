
def pl_increment_cases(df_filtered, field):

    increment_list = []
    list_cases = df_filtered[field].values
    for idx, case in enumerate(list_cases):

        try:
            list_cases_val = list_cases[idx+1]
        except IndexError:
            continue
        increment = list_cases_val - case
        increment_list.append(increment)

    return increment_list