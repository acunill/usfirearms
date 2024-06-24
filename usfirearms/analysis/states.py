#!/usr/bin/env python
# coding: utf-8
"""Anàlisi dels estats

Conté les funcions i respostes per realitzar l'anàlisi per estats que es
planteja a l'exercici 5.

Funcions:

    * groupby_state - agrupa les dades numèriques per estats
    * clean_states - elimina estats sense dades de població
    * merge_datasets - afegeix les dades de població al conjunt original
    * calculate_relative_values - calcula les variables d'armes relatives a
    la població de cada estat.
    * remove_outlier - elimina un valor extrem de l'estat de Kentucky
"""

import pandas as pd


def groupby_state(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula els valors acumulats totals per estat.

    Calcula la suma acumulativa de les variables numèriques per
    estat (suma total per estat).
    Afegeix la variable d'agrupament com a columna i elimina l'any.

    Args:
      data (pd.DataFrame): Dades agrupades per estat i any.

    Returns:
      pd.DataFrame: DataFrame resultant amb les dades agrupades
      estat.
    """
    output = data.groupby(["state"], as_index=False).sum()
    output.drop(columns=["year"], inplace=True)

    # Checkings
    print("Show the first 5 rows of the state data:\n")
    print(output.iloc[0:5])
    return output


def clean_states(data: pd.DataFrame) -> pd.DataFrame:
    """Elimina una llista preestablerta d'estats.

    Args:
      data (pd.DataFrame): Dades agrupades per estat.

    Returns:
      pd.DataFrame: DataFrame resultant amb les files dels estats eliminades.
    """
    # List of states to remove
    states_to_rm = ["Guam", "Mariana Islands", "Puerto Rico", "Virgin Islands"]

    # Check if the states exist in the dataframe
    states_to_rm = [x for x in states_to_rm if x in set(data["state"])]
    if states_to_rm:
        print(f"\nEstats eliminats ({len(states_to_rm)}):\n\n{states_to_rm}")

        # Remove states
        rows_to_rm = data["state"].isin(states_to_rm)
        data = data[~rows_to_rm].reset_index(drop=True)

    # Show list of states and number
    list_of_states = sorted(set(data["state"]))
    print(f"\nLlista d'estats final (total = {len(list_of_states)})" +
          f":\n\n{list_of_states}\n")
    return data


def merge_datasets(left: pd.DataFrame, right: pd.DataFrame) -> pd.DataFrame:
    """Combina les dades d'armes per estat amb la info de cada estat.

    Combina el dataframe obtingut amb la funció groupy_state i les dades
    de població per cada estat.

    Args:
      left (pd.DataFrame):  Dades agrupades per estat.
      right (pd.DataFrame): Nova informació dels estats.

    Returns:
      pd.DataFrame: DataFrame resultant de la combinació.
    """
    output = pd.merge(left, right, on="state", how="left")

    # Show first 5 records
    print("\nDisplay the first 5 records:\n")
    print(output.iloc[0:5])
    return output


def calculate_relative_values(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula els valors relatius a la població.

    Calcula els valors relatius a la població de cada estat
    per les variables referents als permisos i peticions d'armes.
    Afegeix les columnes resultants al conjunt de dades original.

    Args:
      data (pd.DataFrame): Dades d'armes i població per estat.

    Returns:
      pd.DataFrame: DataFrame amb les columnes de percentatge.
    """
    # Create a temporary dataset with the variables
    tmp = data[["permit", "handgun", "longgun", "pop_2014"]]

    # Calculate percentatges
    perc = (
        tmp.apply(lambda row: 100 * row / row["pop_2014"],
                  axis="columns", result_type="expand")
        .drop(columns="pop_2014")
        .add_suffix("_perc")
    )

    # Join percentatge columns to the original dataset
    return pd.concat([data, perc], axis="columns")


def remove_outlier(data: pd.DataFrame) -> pd.DataFrame:
    """Modifica un valor extrem a les dades.

    Canvia un valor extrem de la columna permit_perc per la
    mitjana de tots els valors de la mateixa columna.

    Args:
      data (pd.DataFrame): Dades agrupades per estat. Requereix la
      columna permit_perc.

    Returns:
      pd.DataFrame: Dades sense el valor extrem.
    """
    # State with an outlier
    state = "Kentucky"

    # Calculate actual mean
    permit_mean = data["permit_perc"].mean()
    print(f"\nMitjana de permisos (%): {permit_mean:.2f}%\n")

    # Show all records of the state with the outlier
    print(data[data["state"] == state].round(2))

    # Impute outlier by variable mean (inplace)
    idx = data.index[data["state"] == state]
    data.loc[idx, "permit_perc"] = permit_mean

    # Show new variable mean
    new_permit_mean = data["permit_perc"].mean()
    print("\nMitjana de permisos actualitzada (%): " +
          f"{new_permit_mean:.2f}%\n")

    # Process description
    print(
        ("El valor ha canviat en {} punts. El què hem fet és " +
         "eliminar el valor extrem que condicionava la mitjana " +
         "de la variable 'permit_perc'. Posteriorment, hem " +
         "imputat aquest valor perdut per la mitjana de tots " +
         "els valors de la variable. És una manera de no " +
         "perdre tots els registres (columnes) d'aquest estat.")
        .format(round(abs(new_permit_mean - permit_mean), 1))
    )
    return data
