import pandas as pd
import math



def relative_population(list_cases):
    CSV_POPULATION = "https://covid.ourworldindata.org/data/ecdc/locations.csv"
    population_df = pd.read_csv(CSV_POPULATION)

    population_list = population_df["population"].unique()
    pop_abs = [1 if math.isnan(x) else x for x in population_list]

    #print(list_cases)
    #pop_rel = [x / y for x, y in zip(list_cases, pop_abs)]
    #print(pop_rel)
