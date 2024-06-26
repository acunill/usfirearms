#!/usr/bin/env python
# coding: utf-8
"""Script principal de la PAC4

Proporciona les respostes a les preguntes de la PAC4 de l'assignatura
de Programació per a la Ciència de Dades del Màster en Ciència de
Dades de la UOC.

Data de creació: 24/06/2024
Autor: Àngel Cunill Camprubí

Requereix de llibreries externes especificades a l'arxiu requirements.txt
que han d'estar instal·lades a l'entorn Python on s'executa l'script.

L'arxiu es pot executar directament com a programa principal o es pot
importar com a mòdul amb els objectes i funcions següents

    * ARMS_FILE - ruta i nom de l'arxiu CSV principal a analitzar.
    * POP_FILE - ruta i nom de l'arxiu CSV amb dades auxiliars de població.
    * main - funció principal de l'script
"""

# Load libraries and modules
from usfirearms import load_data
from usfirearms.process import process, group
from usfirearms.analysis import states, evolution
from usfirearms.map import choropleth

# Filepath and name of the USA arms file (input file)
ARMS_FILE = "data/nics-firearm-background-checks.csv"

# Filepath and name of the USA population file (auxiliary data)
POP_FILE = "data/us-state-populations.csv"


# Entry function
def main():
    """Funció que executa l'anàlisi complet"""
    # EXERCISE 1 ---
    print("\nEXERCICI 1 -----------------------------------\n")
    # 1.1 Load data
    arms = load_data.read_csv(ARMS_FILE)
    # 1.2 Select columns of interest
    arms = load_data.clean_csv(arms)
    # 1.3 Standardize column names
    arms = load_data.rename_col(arms)
    print("\nNOTA: L'anunciat diu que la funció 'rename_col' s'ha " +
         "d'implementar al conjunt de dades que conté totes les columnes. " +
         "No li he trobat el sentit ja que sempre treballarem amb el " +
         "subconjunt de dades seleccionat i, per tant, he trobat més lògic " +
         "homogeneitzar les columnes del conjunt seleccionat.")

    # EXERCISE 2 ---
    print("\nEXERCICI 2 -----------------------------------\n")
    # 2.1 Create year field with month column
    arms = process.breakdown_date(arms)
    # 2.2 Remove month column
    arms = process.erase_month(arms)

    # EXERCISE 3 ---
    print("\nEXERCICI 3 -----------------------------------\n")
    # 3.1 Group data by state and year
    arms_state_year = group.groupby_state_and_year(arms)
    # 3.2 State and year with the max hand gun record
    group.print_biggest_handguns(arms_state_year)
    # 3.3 State and year with the max long gun record
    group.print_biggest_longguns(arms_state_year)

    # EXERCISE 4 ---
    print("\nEXERCICI 4 -----------------------------------\n")
    # 4.1 Plot annual evolution
    evolution.time_evolution(
        data=arms_state_year,
        attrs=["permit", "handgun", "longgun"],
        labels=["Permit", "Hand Gun", "Long Gun"]
    )
    # 4.2 Print comments
    print(evolution.RESPONSE_4DOT2)

    # EXERCISE 5 ---
    print("\nEXERCICI 5 -----------------------------------\n")
    # 5.1 Group data by state
    arms_state = states.groupby_state(arms_state_year)
    # 5.2 Clean some states
    arms_state = states.clean_states(arms_state)
    # 5.3 Merge arms data with population data
    pop_df = load_data.read_csv(POP_FILE, verbose=False)
    arms_state_pop = states.merge_datasets(arms_state, pop_df)
    # 5.4 Calculate relative values to the population
    arms_state_pop = states.calculate_relative_values(arms_state_pop)
    # 5.5 Fix an outlier of Kentucky state
    arms_state_pop = states.remove_outlier(arms_state_pop)

    # EXERCISE 6 ---
    print("\nEXERCICI 6 -----------------------------------\n")
    # Make choropleth maps for each percentage variable
    try:
        choropleth.map_choropleth(
            data=arms_state_pop,
            variable="permit_perc",
            legend_name="Permisos Revisats (%)",
            output_filepath="outputs/permit.png"
        )
        choropleth.map_choropleth(
            data=arms_state_pop,
            variable="handgun_perc",
            legend_name="Peticions d'Armes Curtes (%)",
            output_filepath="outputs/handgun.png"
        )
        choropleth.map_choropleth(
            data=arms_state_pop,
            variable="longgun_perc",
            legend_name="Peticions d'Armes Llargues (%)",
            output_filepath="outputs/longgun.png"
        )
    except Exception as error:  # pylint: disable=W0703
        print(error)
    else:
        print("Choropleths successfully mapped at outputs folder.\n")


# Run as a program
if __name__ == '__main__':
    main()
