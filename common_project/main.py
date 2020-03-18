import common_project.words_polysemy.main as mn
import common_project.coronavirus.main as mnc
import argparse




def parse_args(parser):
    parser.add_argument('-co', '--coronavirus', action="store_true",
                        help='Insert --coronavirus if you want to know the coronavirus data')
    parser.add_argument('-sp', '--spanish', action="store_true",
                        help='Insert --spanish if you want to know the spanish words data')


if __name__ == "__main__":
    #############ARGPARSE########
    parser = argparse.ArgumentParser(description='software to scrap data from the web. It has two principal features: coronavirus data and spanish words data scraping')
    parse_args(parser)
    mn.parse_args(parser)
    mnc.parse_args(parser)
    args = parser.parse_args()
    ############################

    if args.spanish:
        mn.analyse_words_polysemy(plot_yes=args.plot_yes, average_yes=args.average_yes)

    if args.coronavirus:
        mnc.coronavirus_data(args.country)










