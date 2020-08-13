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

def check_error_field(field, list_of_fields):
    if field not in list_of_fields:
        similar_field = similar_name_country(field, list_of_fields)
        raise FieldError(f'The name of data field is not in the list of field. Try one of these {list_of_fields}. Did you mean {similar_field}?')

def check_error_country(df_filtered, country, list_of_countries):
    if df_filtered.empty:
        similar_country = similar_name_country(country, list_of_countries)
        raise EmptyDataFrame(f'The name of country is not in the list of countries. Try to one of these {list_of_countries}. Did you mean {similar_country}?')




