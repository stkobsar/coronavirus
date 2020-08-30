import pandas as pd

def relative_population(absolute_values):
    CSV_POPULATION = "https://covid.ourworldindata.org/data/ecdc/locations.csv"

    population_df = pd.read_csv(CSV_POPULATION)
    population_list = population_df["population"].unique()
     ### Dividir valores de las listas entre si y meterlo en una nueva lista, que será list_cases para plotar.

    #CSV_POPULATION --> population
    #relative_values = num_cases / population
    #return realtive_values


CSV_POPULATION = "https://covid.ourworldindata.org/data/ecdc/locations.csv"

relative_population(CSV_POPULATION)