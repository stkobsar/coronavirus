import pandas as pd
import common_project.coronavirus.plot_country as pl
import matplotlib.pyplot as plt


def pl_total_cases(csv, countries_user):
    for country in countries_user:
        plot_output = pl.pl_country_cases(country, csv, savefig=False)
    plt.legend(countries_user)
    output = "cases_date_{}.png".format("_".join(countries_user))
    plt.xlabel("Days since covid started")
    plt.ylabel("COVID official cases")
    plt.savefig(output)
