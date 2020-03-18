import argparse
import os
import common_project.coronavirus.plot_country as pl
import common_project.coronavirus.total_cases as tot

print(os.path.abspath(__file__))#funcion de os para usar el path absoluto. Sirve para que la fila funcione en todos sitios.
ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#os.path.dirname sirve para ir un dir hacia atras. Se pone 3 veces para ir 3 para atrás.
CSV = os.path.join(ROOT_FOLDER, "data/full_data.csv")
print(CSV)

def coronavirus_data(country):
    if country:
        plot_country_cases = pl.pl_country_cases(country, CSV)

def parse_args(parser):
    parser.add_argument('-ct', '--country', default=False, type=str,
                        help='Insert --country if you want to know the evolution of cases in that country. i.e --country Spain')
    parser.add_argument('-cts', '--countries', nargs="+", help="List of countries. i.e. --countries spain italy france", default=[])
if __name__ == "__main__":
    ###########
    parser = argparse.ArgumentParser(description='Coronavirus cases among time analysis')
    parse_args(parser)
    args = parser.parse_args()
    ###########

    coronavirus_data(args.country)

    if args.countries:
        plot_total_cases = tot.pl_total_cases(CSV, args.countries)
    else:
        pass
    #hist_total = hist_total_cases(CSV)

