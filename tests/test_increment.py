import pytest
import os
import pandas as pd
import coronavirus.plot_country as pc
import coronavirus.functionalities.increment_days as id

absolute_path_every_machine = os.path.abspath(__file__)
directory_path = os.path.dirname(absolute_path_every_machine)

ID = "full_data.csv"
CSV = "https://covid.ourworldindata.org/data/ecdc/{0}".format(ID)

def get_csv_test(CSV):
    country = "Spain"
    field = "total_cases"
    csv = pc.dataset_clean(country, field, CSV)
    tail_csv = csv.tail(30)
    return tail_csv

tail_csv = get_csv_test(CSV)

def increment_test(tail_csv):
    field = "total_cases"
    incremental = id.pl_increment_cases(tail_csv, field)




