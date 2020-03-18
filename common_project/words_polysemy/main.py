import argparse
import common_project.words_polysemy.common as co
import common_project.words_polysemy.plot_common as pl
import common_project.words_polysemy.common_average as av

#FUNCIONES A DEFINIR
URL = "https://en.m.wikipedia.org/wiki/Most_common_words_in_Spanish"

def analyse_words_polysemy(plot_yes=False, average_yes=False):
    words = co.main(URL)
    freq = pl.plot_words(words, plot_yes)
    average = av.average_freq(freq, average_yes)

def parse_args(parser):
    parser.add_argument('-av', '--average_yes', action="store_true",
                        help='Insert --average_yes if you want to know the average frequencies of the most common words')
    parser.add_argument('-p', '--plot_yes', action="store_true",
                        help='Insert plot_yes if you want to plot an histogram of frequencies')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Most common words in Spanish')
    parse_args(parser)
    args = parser.parse_args()
    analyse_words_polysemy(args.plot_yes, args.average_yes)

    










