#!/usr/bin/env python
# coding: utf-8
"""Processament de dades

Conté les funcions de preprocessament de les dades referents a
l'exercici 2.

Funcions:

    * breakdown_date - separa l'any i el mes de la columna month en
    dues columnes diferents.
    * erase_month - esborra la columna month del dataframe resultant.
"""

import pandas as pd


def breakdown_date(data: pd.DataFrame) -> pd.DataFrame:
    """Crea les columnes amb l'any i el mes.

    Separa l'any i el mes de la columna 'month' en dues columnes
    anomenades 'year' per l'any i la mateixa columna 'month' pel mes.
    Ambdues es converteixen a tipus enter.

    Args:
      data (pd.DataFrame): Dades carregades amb les columnes d'interès.

    Returns:
      pd.DataFrame: DataFrame amb l'any i el mes en dues columnes diferents.
    """
    # Avoid modify in place
    data = data.copy()

    # Split year-month into two diferent columns
    data[["year", "month"]] = data["month"].str.split("-", n=1, expand=True)

    # Convert string type to integer type
    data = data.astype({"year": "int", "month": "int"})
    return data


def erase_month(data: pd.DataFrame) -> pd.DataFrame:
    """Elimina la columna 'month'.

    Args:
      data (pd.DataFrame): Dades amb la columna month.

    Returns:
      pd.DataFrame: DataFrame sense la columna 'month'.
    """
    # Drop column month (does not modify original data)
    data = data.drop(columns=["month"], inplace=False)

    # Checkings
    print("\nDrop column month.\n")
    print("Show the first 5 rows and selected columns:\n")
    print(data.iloc[0:5])
    return data
