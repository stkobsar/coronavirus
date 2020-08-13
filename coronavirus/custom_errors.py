from builtins import Exception
from difflib import SequenceMatcher


class EmptyDataFrame(Exception):
    pass

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def similar_name_country(country, paises):
    #country es uno de los paises intriducidos por el usuario
    #paises es todos los paises

    prob_similar = []
    for pais in paises:
        prob_similar_value = similar(pais, country)
        prob_similar.append(prob_similar_value)

    index_max = prob_similar.index(max(prob_similar))
    country_similar = paises[index_max]

    return country_similar

class FieldError(Exception):
    pass




