import requests
from bs4 import BeautifulSoup
import pandas as pd


def main(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all("table", class_="wikitable sortable")[0]
    rows = table.find_all("tr")

    word_list=[]
    for row in rows:
        tds=row.find_all("td")
        try:
            palabra = tds[1].text.strip("\n") #asi se salta la primera linea de la tabla que son los títulos (th)
            frec = tds[2].text.strip("\n")
        except IndexError:
            continue
        frec = frec.replace(",", "") #esta funcion sirve para remplazar la coma de los numeros por nada
        frec = float(frec)
        word = Word(palabra, frec)
        word_list.append(word)    
    return word_list


class Word():

    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency




if __name__ == "__main__":
    url = "https://en.m.wikipedia.org/wiki/Most_common_words_in_Spanish"
    words = main(url)
