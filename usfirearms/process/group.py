#!/usr/bin/env python
# coding: utf-8
"""Agrupament de dades

Conté les funcions d'agrupament de les dades referents a l'exercici 3.

Funcions:

    * groupby_state_and_year - agrupa les dades numèriques per estat i any.
    * print_biggest_guns - mostra l'estat i l'any amb major nombre de peticions
    d'armes.
    * print_bigguest_hanguns - crida a la funció print_biggest_guns per a
    armes curtes.
    * print_bigguest_longguns - crida a la funció print_biggest_guns per a
    armes llargues.
"""

import pandas as pd


def groupby_state_and_year(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula els valors acumulats totals per estat i any.

    Calcula la suma acumulativa de les variables numèriques per estat
    i any (suma total per any).
    Elimina el format geràrquic de l'índex.

    Args:
      data (pd.DataFrame): Dades amb els registres d'armes mensuals.

    Returns:
      pd.DataFrame: DataFrame resultant amb les dades agrupades
    """
    output = data.groupby(["state", "year"], as_index=False).sum()
    return output


def print_biggest_guns(data: pd.DataFrame, gun_type: str) -> None:
    """Indica el nom de l'estat i l'any amb més registres d'armes.

    Args:
      data (pd.DataFrame): Datafrane amb les sumes totals per estat i any.
      gun_type (str): Tipus d'armes ("handgun", "longgun").

    Returns:
      None
    """
    # Max guns record
    max_guns = data[gun_type].max()

    # Subset state and year with max number of guns
    res = data.loc[data[gun_type] == max_guns, ["state", "year"]]
    res = res.iloc[0]

    # Print message with the result
    gun_type_txt = {"handgun": "curtes", "longgun": "llargues"}
    msg = ("\nEl major nombre de peticions d'armes {} s'ha registrat " +
           "l'any {} a l'estat de {}, amb un total de {} armes.\n")
    print(msg.format(gun_type_txt[gun_type], res["year"], res["state"],
                     int(max_guns)))


def print_biggest_handguns(data: pd.DataFrame) -> None:
    """Indica el nom de l'estat i l'any amb més registres d'armes manuals.

    Args:
      data (pd.DataFrame): Dataframe amb les sumes totals per estat i any.

    Returns:
      None
    """
    print_biggest_guns(data, "handgun")


def print_biggest_longguns(data: pd.DataFrame) -> None:
    """Indica el nom de l'estat i l'any amb més registres d'armes llargues.

    Args:
      data (pd.DataFrame): Dataframe amb les sumes totals per estat i any.

    Returns:
      None
    """
    print_biggest_guns(data, "longgun")
