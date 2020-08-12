import pandas as pd
import coronavirus.plot_country as pl
import matplotlib.pyplot as plt


def pl_total_cases(csv, countries_user, field):
    for country in countries_user:
        plot_output = pl.pl_country_cases(country, csv, field, savefig=False)

    plt.legend(countries_user)


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


    output = f"{field_custom}_{curr_date_custom}_{countries_user_outputname}.png"


    plt.savefig(output)
