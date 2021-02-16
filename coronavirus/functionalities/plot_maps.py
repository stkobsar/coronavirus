import pandas as pd
from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts_snapshot.main import make_a_snapshot


def map_total_cases(csv):
    """
    Description: exports an html file with an interactive map showing the latest total cases
    registered per country in the planet
    in a two-ax chart for countries with p-score > 1
    :param owid_data: OWID main coronavirus dataset in a pandas dataframe format,
                        it can be already processed with clean_data()
    :export: HTML file with a pyecharts interactive map
    """

    input_df = pd.read_csv(csv)

    if input_df.index.name == "date":
        input_df = input_df[["location", "total_cases"]].dropna()
    else:
        input_df = input_df[["date", "location", "total_cases"]].set_index("date").dropna()

    map_df = input_df.loc[input_df.groupby('location').total_cases.idxmax()].head(
        len(input_df["location"].unique()) - 1)

    map_df.reset_index(drop=True, inplace=True)

    country = list(map_df["location"])
    totalcases = list(map_df["total_cases"])

    list1 = [[country[i], totalcases[i]] for i in range(len(country))]
    map_1 = Map(init_opts=opts.InitOpts(width="1000px", height="460px"))
    map_1.add("Total Confirmed Cases",
              list1,
              maptype="world",
              is_map_symbol_show=False)
    map_1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    map_1.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=1100000, is_piecewise=True, pieces=[
            {"min": 1000000},
            {"min": 600000, "max": 999999},
            {"min": 200000, "max": 599999},
            {"min": 50000, "max": 119999},
            {"min": 10000, "max": 49999},
            {"max": 9999}, ]),
        title_opts=opts.TitleOpts(
            title='Casos confirmados de COVID-19',
            subtitle="Últimos datos disponibles",
            pos_left="center",
            padding=0,
            item_gap=2,
            title_textstyle_opts=opts.TextStyleOpts(color="darkblue",
                                                    font_weight="bold",
                                                    font_family="Courier New",
                                                    font_size=30),
            subtitle_textstyle_opts=opts.TextStyleOpts(color="grey",
                                                       font_weight="bold",
                                                       font_family="Courier New",
                                                       font_size=13)),
        legend_opts=opts.LegendOpts(is_show=False))

    return map_1.render('map_cases.html')


def map_total_deaths_per_million(csv):
    """
    Author: Jorge Puente
    Description: exports an html file with an interactive map showing the latest total cases
    registered per country in the planet
    in a two-ax chart for countries with p-score > 1
    :param owid_data: OWID main coronavirus dataset in a pandas dataframe format,
                        it can be already processed with clean_data()
    :return: map_cases.html
    """
    input_df = pd.read_csv(csv)
    if input_df.index.name == "date":
        input_df = input_df[["location", "total_deaths_per_million"]].dropna()
    else:
        input_df = input_df[["date", "location", "total_deaths_per_million"]].set_index("date").dropna()

    map_df = input_df.loc[input_df.groupby('location').total_deaths_per_million.idxmax()].head(
        len(input_df["location"].unique()) - 1)

    map_df.reset_index(drop=True, inplace=True)

    country = list(map_df["location"])
    totaldeaths = list(map_df["total_deaths_per_million"])

    list1 = [[country[i], totaldeaths[i]] for i in range(len(country))]
    map_1 = Map(init_opts=opts.InitOpts(width="1000px", height="460px"))
    map_1.add("Muertes por millón de habitantes",
              list1,
              maptype="world",
              is_map_symbol_show=False)
    map_1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    map_1.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=1100000, is_piecewise=True, pieces=[
            {"min": 1000},
            {"min": 800, "max": 999},
            {"min": 600, "max": 799},
            {"min": 400, "max": 599},
            {"min": 200, "max": 399},
            {"max": 199}, ]),
        title_opts=opts.TitleOpts(
            title='Muertes por millón de habitantes',
            subtitle="Datos recogidos hasta el 26 de Diciembre de 2020",
            pos_left="center",
            padding=0,
            item_gap=2,
            title_textstyle_opts=opts.TextStyleOpts(color="darkblue",
                                                    font_weight="bold",
                                                    font_family="Courier New",
                                                    font_size=30),
            subtitle_textstyle_opts=opts.TextStyleOpts(color="grey",
                                                       font_weight="bold",
                                                       font_family="Courier New",
                                                       font_size=13)),
        legend_opts=opts.LegendOpts(is_show=False))
    return map_1.render('map_deaths_per_million.html')
