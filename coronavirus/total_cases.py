import pandas as pd
import os
import coronavirus.plot_country as pl
import matplotlib.pyplot as plt


def pl_total_cases(csv, countries_user, field, incremental, relative):
    for country in countries_user:
        plot_output = pl.pl_country_cases(country, csv, field, incremental=incremental, relative=relative)

    #Overwrite previous axis and title name!
    plt.legend(countries_user)
    curr_date = str(pd.to_datetime('today').date())
    curr_date_custom = curr_date.replace('-', '')
    field_custom = field.replace('_', '')
    field_title = field.replace('_', ' ')
    countries_user_outputname = "_".join(countries_user)
    countries_plot_title = " ".join(countries_user)

    plt.xlabel("Days since COVID-19 start spreading")
    plt.ylabel(f"COVID-19 official cases of {field_title}")
    plt.title(f"COVID-19 data of {field_title} in {countries_plot_title}")

    dir = create_dir_default(curr_date_custom)
    output = f"{field_custom}_{curr_date_custom}_{countries_user_outputname}.png"
    output = os.path.join(dir, output)
    plt.savefig(output)


def create_dir_default(date):
    dir_name = f"{date}_results"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    return dir_name
