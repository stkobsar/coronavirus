import matplotlib.pyplot as plt

#Funcion que coge la lista de objetos word y haga un plot


def plot_words(words, plot_yes):
    list_freq = []
    for word in words:
        freq = word.frequency
        list_freq.append(freq)
    plt.hist(list_freq)
    if plot_yes:
        plt.savefig("histogram_freq.png") 
    return list_freq 



