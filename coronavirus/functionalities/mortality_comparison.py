import pandas as pd
import os
import matplotlib.pyplot as plt


def plot_mortality_vs_excess(csv, owid_excess_mortality):
    """
    Description: plots a comparison between official death count and p-score death count
    in a two-ax chart for countries with p-score > 1
    :param owid_data: OWID main coronavirus dataset in a pandas dataframe format,
                        it can be already processed with clean_data()
    :param owid_excess_mortality: OWID excess mortality dataset on coronavirus
                        in a pandas dataframe format
    """
    owid_data = pd.read_csv(csv)
    owid_excess_mortality = pd.read_csv(owid_excess_mortality)

    if owid_data.index.name == "date":
        owid_data = owid_data[["location", "total_deaths_per_million"]].dropna()
    else:
        owid_data = owid_data[["date", "location", "total_deaths_per_million"]].set_index("date").dropna()

    owid_data = owid_data.loc[owid_data.groupby('location').total_deaths_per_million.idxmax()].head(
        len(owid_data["location"].unique()) - 1)

    owid_excess_mortality['date'] = pd.to_datetime(owid_excess_mortality['date'])
    owid_excess_mortality = owid_excess_mortality[["date",
                                                   "location",
                                                   "Excess mortality cumulative P-scores, all ages"]].set_index("date")

    owid_excess_mortality = owid_excess_mortality.dropna().drop_duplicates('location', keep='last')
    owid_excess_mortality = owid_excess_mortality.loc[
        (owid_excess_mortality['Excess mortality cumulative P-scores, all ages'] >= 1)]

    merged_df = owid_excess_mortality.merge(owid_data, on='location')
    merged_df = merged_df.rename(columns={"total_deaths_per_million": "Muertes",
                                          "Excess mortality cumulative P-scores, all ages": "Exceso de mortalidad",
                                          "location": "País"}).set_index('País')
    merged_df = merged_df[["Muertes", "Exceso de mortalidad"]]

    #rcParams['figure.figsize'] = 14, 6
    fig = plt.figure()
    ax = fig.add_subplot()
    ax2 = ax.twinx()
    width = 0.4
    merged_df["Exceso de mortalidad"].plot(kind='bar', color='darkorange', ax=ax, width=width, position=1)
    merged_df["Muertes"].plot(kind='bar', color='royalblue', ax=ax2, width=width, position=0)

    fig.legend(loc="upper right", bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)

    plt.title('Datos a 26 de diciembre de 2020', fontsize=10)
    plt.suptitle('Comparación de mediciones de mortalidad de COVID-19', fontsize=14, y=0.95)
    ax.set_ylim([0, 25])
    ax2.set_ylim([0, 1800])
    ax.tick_params(axis='y', colors='darkorange')
    ax2.tick_params(axis='y', colors='blue')

    ax.set_ylabel("p-score acumulado")
    ax2.set_ylabel("Muertes por millón acumuladas")

    ax.yaxis.label.set_color('darkorange')
    ax2.yaxis.label.set_color('blue')
    plt.savefig("mortality.png")