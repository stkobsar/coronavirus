import argparse
import os
import coronavirus.plot_country as pl
import coronavirus.total_cases as tot

(os.path.abspath(__file__))#funcion de os para usar el path absoluto. Sirve para que la fila funcione en todos sitios.
ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#os.path.dirname sirve para ir un dir hacia atras. Se pone 3 veces para ir 3 para atrás.
print(ROOT_FOLDER)
#CSV = os.path.join(ROOT_FOLDER, "data/full_data.csv")

ID = "full_data.csv"
CSV = "https://covid.ourworldindata.org/data/ecdc/{0}".format(ID)



def coronavirus_data(country, field, countries):
    if country:
        plot_country_cases = pl.pl_country_cases(country, CSV, field=field)
    if countries:
        plot_total_cases = tot.pl_total_cases(CSV, countries)
    else:
        pass



def parse_args(parser):
    parser.add_argument('-ct', '--country', default=False, type=str,
                        help='Insert --country if you want to know the evolution of cases in that country. i.e --country Spain')
    parser.add_argument('-cts', '--countries', nargs="+", help="List of countries. i.e. --countries spain italy france", default=[])
    parser.add_argument('-col', '--column', default="total_cases", help="Input column of the csv to carry out the plot")

if __name__ == "__main__":
    ###########
    parser = argparse.ArgumentParser(description='Coronavirus cases among time analysis')
    parse_args(parser)
    args = parser.parse_args()
    ###########
    coronavirus_data(args.country, args.column, args.countries)

