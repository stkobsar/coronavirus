import pytest
import os
import pandas as pd
import coronavirus.plot_country as pc
import coronavirus.functionalities.increment_days as id

absolute_path_every_machine = os.path.abspath(__file__)
directory_path = os.path.dirname(absolute_path_every_machine)


ID = "full_data.csv"
csv = "https://covid.ourworldindata.org/data/ecdc/{0}".format(ID)
df_coronavirus = pd.read_csv(csv)
condition = df_coronavirus["location"] == "Spain"
df_cond = df_coronavirus[condition]
tail_csv = df_cond.tail(30)

def increment_test(tail_csv):
    field = "total_cases"

    incremental = id.pl_increment_cases(tail_csv, field)




