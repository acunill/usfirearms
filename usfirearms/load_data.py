#!/usr/bin/env python
# coding: utf-8
"""Mòdul de càrrega de dades

Conté les funcions per carregar i preparar les dades d'interès per al seu
posterior processament i anàlisi, referents a l'exercici 1.

Funcions:

    * read_csv - carrega les dades des del fitxer CSV.
    * clean_csv - selecciona les columnes d'interés per les anàlisis.
    * rename_col - reanomena la columna long_gun per longun.
"""

import os
import pandas as pd


def read_csv(file_path: str, verbose: bool = True) -> pd.DataFrame:
    """Carrega un fitxer CSV com a DataFrame.

    Carrega un fitxer de dades CSV com a DataFrame de Pandas.
    Mostra els 5 primers registres i 4 columnes.
    Mostra la seva estructura.

    Args:
      file_path (str): Ruta i nom de l'arxiu de dades.
      verbose (bool):  Mostra comprovacions per pantalla (default: True)

    Returns:
      pd.DataFrame: Dataframe amb les dades carregades.
    """
    # Load data
    print(f"Loading '{os.path.basename(file_path)}'")
    data = pd.read_csv(file_path)

    # Check results
    if verbose:
        # Show first 5 records and n columns
        print("\nDisplay the first 5 records and " +
              f"{max([len(data.columns), 4])} columns:\n")
        print(data.iloc[0:5, 0:4])  # pylint: disable=E1101

        # Show data structure
        print("\nData structure:\n")
        print(data.info())  # pylint: disable=E1101
    return data


def clean_csv(data: pd.DataFrame) -> pd.DataFrame:
    """Selecciona les columnes desitjades del DataFrame.

    Args:
      data (pd.DataFrame): Dataframe amb les dades d'armes.

    Returns:
      pd.DataFrame: Dataframe amb les columnes seleccionades.
    """
    # Columns of interest
    cols = ["month", "state", "permit", "handgun", "long_gun"]

    # Select columns and print final column names
    data = data.loc[:, cols]
    print(f"\nSelected columns: {list(data.columns)}\n")
    return data


def rename_col(data: pd.DataFrame) -> pd.DataFrame:
    """Modifica el nom de la columna 'long_gun' a 'longgun'.

    Args:
      data (pd.DataFrame): Dades en format dataframe.

    Returns:
      pd.DataFrame: DataFrame amb la columna modificada.
    """
    # Column to change
    colnames = {"long_gun": "longgun"}

    # Check if columns exists and rename in a copy
    if set(colnames.keys()).issubset(data.columns):
        data = data.rename(columns=colnames, inplace=False)

    # Show new column names to the stdout
    print(f"\nNew column names: {list(data.columns)}\n")
    print((
        "\nNOTA: L'anunciat diu que s'ha d'implementar al conjunt de dades " +
        "que conté totes les columnes. No li he trobat el sentit ja que " +
        "sempre treballarem amb el subconjunt de dades seleccionat i, per " +
        "tant, he trobat més lògic homogeneitzar les columnes del conjunt " +
        "seleccionat.\n"
    ))
    return data
