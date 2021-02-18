
import argparse
import os
import coronavirus.total_cases as tot
import coronavirus.histograms as hs
import coronavirus.qq_plot as qp
import functionalities.mortality_comparison as mc
import functionalities.plot_maps as mp
from urllib.request import Request, urlopen


(os.path.abspath(__file__))#funcion de os para usar el path absoluto. Sirve para que la fila funcione en todos sitios.
ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#os.path.dirname sirve para ir un dir hacia atras. Se pone 3 veces para ir 3 para atrás.

#CSV_FULL_DATA= "https://covid.ourworldindata.org/data/owid-covid-data.csv"
CSV_FULL_DATA = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"


filedir = os.path.join(ROOT_FOLDER, "/data")
filename = "excess_mortality.csv"
csv_excess_mortality = os.path.join(filedir, filename)


def coronavirus_data(field, countries, incremental, histogram=False, qqplot=False,
                     excessmortality=False, map_cases=False, death_milion=False):
    if countries:
        tot.pl_total_cases(CSV_FULL_DATA, countries, field=field, incremental=incremental)
    if histogram:
        hs.get_histograms(CSV_FULL_DATA)
    if qqplot:
        qp.get_qq_plot(CSV_FULL_DATA)
    if excessmortality:
        mc.plot_mortality_vs_excess(CSV_FULL_DATA, csv_excess_mortality)
    if map_cases:
        mp.map_total_cases(CSV_FULL_DATA)
    if death_milion:
        mp.map_total_deaths_per_million(CSV_FULL_DATA)




def parse_args(parser):
    parser.add_argument('-md', '--death_million', action="store_true", help="death million interactive plot")
    parser.add_argument('-tc', '--map_cases', action="store_true", help="interactive total map cases")
    parser.add_argument('-mt', '--excessmortality', action="store_true", help="excessmortality plot of all variables")
    parser.add_argument('-qq', '--qqplot', action="store_true", help="QQplot of all variables")
    parser.add_argument('-hist', '--histogram', action="store_true", help="Histograms of all variables")
    parser.add_argument('-cts', '--countries', nargs="+", help="List of countries. i.e. --countries spain italy france", default=[])
    parser.add_argument('-fld', '--field', default="total_cases", help="Input column of the csv data to carry out the plot")
    parser.add_argument('-inc', '--incremental', action="store_true", help="Input to carry out a plot of the increment in desired field between days") #action="store_true" manera de poner default false, y si lo pones por cl, pasa a true


if __name__ == "__main__":
    ###########
    parser = argparse.ArgumentParser(description='Coronavirus cases among time: data analysis')
    parse_args(parser)
    args = parser.parse_args()
    ###########
    coronavirus_data(args.field, args.countries, args.incremental, args.histogram, args.qqplot,
                     args.excessmortality, args.map_cases, args.death_million)

