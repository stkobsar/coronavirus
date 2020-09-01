import argparse
import os
import coronavirus.plot_country as pl
import coronavirus.total_cases as tot
import coronavirus.functionalities.increment_days as id
import coronavirus.custom_errors as ce

(os.path.abspath(__file__))#funcion de os para usar el path absoluto. Sirve para que la fila funcione en todos sitios.
ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#os.path.dirname sirve para ir un dir hacia atras. Se pone 3 veces para ir 3 para atrás.

CSV_FULL_DATA = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"


def coronavirus_data(field, countries, incremental, relative):
    plot_total_cases = tot.pl_total_cases(CSV_FULL_DATA, countries, field=field, incremental=incremental, relative=relative)


def parse_args(parser):
    parser.add_argument('-cts', '--countries', nargs="+", help="List of countries. i.e. --countries spain italy france", default=[])
    parser.add_argument('-fld', '--field', default="total_cases", help="Input column of the csv data to carry out the plot")
    parser.add_argument('-inc', '--incremental', action="store_true", help="Input to carry out a plot of the increment in desired field between days") #action="store_true" manera de poner default false, y si lo pones por cl, pasa a true
    parser.add_argument('-rel', '--relative', action="store_true", help="Input to carry out a plot of the cases relative to population") #action="store_true" manera de poner default false, y si lo pones por cl, pasa a true


if __name__ == "__main__":
    ###########
    parser = argparse.ArgumentParser(description='Coronavirus cases among time: data analysis')
    parse_args(parser)
    args = parser.parse_args()
    ###########
    coronavirus_data(args.field, args.countries, args.incremental, args.relative)

