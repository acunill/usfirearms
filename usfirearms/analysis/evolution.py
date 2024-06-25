#!/usr/bin/env python
# coding: utf-8
"""Anàlisi temporal

Conté les funcions i respostes per realitzar l'anàlisi temporal que es
planteja a l'exercici 4.

Funcions:

    * time_evolution - genera un gràfic d'evolució anual per les dades
    d'entrada.

Variables:
    * response_4dot2 - resposta a l'exercici 4.2
"""

import pandas as pd
import matplotlib.pyplot as plt
import colorbrewer


def time_evolution(data: pd.DataFrame, attrs: list[str],
                   colors: list[str] = None,
                   labels: list[str] = None) -> None:
    """Genera un gràfic amb l'evolució temporal de les variables especificades.

    Args:
      data (pd.DataFrame): Conjunt de dades. Requereix un camp anomenat 'year'.
      attrs (list): Llista de columnes a visualitzar.
      colors (list): Colors de les línies (default: paleta ColorBrewer Accent)
      labels (bool): Legend labels (default: None)

    Returns:
      None
    """
    # Color settings
    if colors is None:
        colors = colorbrewer.Accent[len(attrs)]  # pylint: disable=E1101
        colors = list(map(lambda x: f"#{x[0]:02x}{x[1]:02x}{x[2]:02x}", colors))

    # Aggregate data to annual sums
    agg_data = data.groupby(["year"], as_index=False)[attrs].sum()

    # Plot the data
    fig = plt.figure()
    axis = fig.add_subplot()

    # Add lines
    for i, col in enumerate(attrs):
        axis.plot("year", col, data=agg_data, color=colors[i])

    # Set title and axis labels
    axis.set_title("Evolució temporal dels valors totals anuals")
    axis.set_ylabel("$Registres\\:totals\\:\\times any^{-1}$")

    # Set axis limits
    xlim_min = int(agg_data["year"].min())
    xlim_max = int(agg_data["year"].max())
    xticks = range(xlim_min, xlim_max + 1, 2)
    axis.set(xlim=(xlim_min, xlim_max), xticks=xticks)

    # Show legend
    if labels is None:
        labels = attrs
    plt.legend(labels=labels)

    # Display the plot
    plt.show()


RESPONSE_4DOT2 = (
    "\nS'observa una correlació forta entre el nombre de permisos " +
    "i les peticions d'armes curtes (pistoles) en el període de " +
    "1998 a 2020. En ambdós casos, la tendència ha estat creixent " +
    "fins al 2016, on després disminueix.\n" +
    "Per a les armes llargues, aquesta correlació no és tan " +
    "evident, essent més o menys constant el nombre de peticions " +
    "durant gairebé tot el període.\n" +
    "S'observa, també, que el nombre de peticions d'armes llargues " +
    "és molt major a l'expedició de llicències fins a 2010, on " +
    "s'iguala i torna a créixer fins a 2013. Aquest fet també " +
    "s'observa per a les armes curtes fins a 2006. Sembla, doncs, " +
    "que hi ha un retard en l'expedició de llicències que es comença " +
    "a solucionar per complet a partir de 2014.\n" +
    "L'efecte de la pandèmia de coronavirus (2020) també és " +
    "evident, amb un descens brusc del nombre de permisos i peticions " +
    "d'armes.\n" +
    "Tanmateix, el repunt de 2016 concorda amb el màxim de " +
    "víctimes per tirotejos del 2017 (https://cnnespanol.cnn.com/2024" +
    "/02/15/cultura-armas-estados-unidos-mundo-trax/).\n" +
    "Sense dades postpandèmia, és difícil pronosticar la " +
    "tendència en els pròxims anys.\n"
)
