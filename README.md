# Programació per a la Ciència de Dades - PAC4

Autor: Àngel Cunill Camprubi (acc30)  
Data: 24 de juny de 2024

## ¿Què conté el repositori?

Aquest repositori conté la solució a la PAC4 de l'assignatura Programació per a
la Ciència de Dades del Màster en Ciència de Dades de la UOC.

L'objectiu és realitzar un projecte de ciència de dades amb totes les seves
parts. Per fer-ho, es proposa estudiar el comportament de la població dels 
Estats Units pel que fa a l’ús d’armes de foc. S'utilitza un conjunt de dades 
obtingut de la base de dades de [Kaggle](https://www.kaggle.com/datasets/pedropereira94/nics-firearm-backgroundchecks),
que conté informació (per data i estat) de la verificació d’antecedents
de gent que es vol treure el permís d’armes.

L'arxiu està inclòs en el projecte i conté, entre d'altres, les següents 
columnes d'interès:

* `month`: any i mes del registre
* `state`: estat
* `permit`: permisos (verificació d’antecedents)  
* `handgun`: peticions d’armes curtes (pistoles)  
* `long_gun`: peticions d’armes llargues

S'utilitza també dades poblacionals obtingudes d'un repositori 
[GitHub Gist](https://gist.githubusercontent.com/bradoyler/0fd473541083cfa9ea6b5da57b08461c/raw/fa5f59ff1ce7ad9ff792e223b9ac05c564b7c0fe/populations.csv)
, que també està inclòs en el projecte. Aquest conjunt presenta la població 
(2014) dels diferents estats ubicats als Estats Units amb les columnes següents:

* `code`: codi de dues lletres que identifica els estats
* `state`: nom de l’estat sense abreujar
* `pop_2014`: nombre d’habitants a l’any 2014

### Estructura principal del projecte

* `data` - dades necessàries per fer l'anàlisi
  * `nics-firearm-background-checks.csv` - arxiu de dades sobre armes de foc als EUA
  * `us-state-populations.csv` - arxiu de dades de població del EUA
* `usfirearms` - mòduls per realitzar les anàlisis
  * `load_data.py` - funcions de l'Exercici 1
  * `process`
    * `process.py` - funcions de l'Exercici 2
    * `group.py` - funcions de l'Exercici 3
  * `analysis`
    * `evolution.py` - funcions de l'Exercici 4
    * `states.py` - funcions de l'Exercici 5
  * `map`
    * `choropleth` - funció de l'Exercici 6
* `outputs` - carpeta de sortida de resultats
* `tests` - tests sobre les funcions
* `main.py` - programa principal
* `LICENCE` - llicència del projecte
* `README.md` - arxiu README
* `requirements.txt` - arxiu de requeriments de llibreries

## ¿Com executar el programa?

Per executar l'anàlisi des de la línia de comandes cal seguir els següents 
passos:

1. `git clone https://github.com/acunill/usfirearms.git`
2. `cd ./usfirearms`
3. `pip install -r requirements.txt`
4. `python3 ./main.py`

Tot el projecte està desenvolupat en Python 3.10.0.
Si s'obtenen els arxius del projecte de forma local (p. ex, un arxiu ZIP), es 
pot saltar el pas 1. És recomanable instal·lar les llibreries en un entorn 
virtual, que s'hauria de crear després del pas 2.

## Sortides

El programa retorna els resultats de l'anàlisi (respostes als punts de la PAC) 
per la consola i genera 3 mapes en format PNG que es desen a la carpeta
`outputs`.

## Notes

Per manca de temps, els tests sobre el codi es troben en desenvolupament.
Només n'he creat un per rebre el comentari del professor, perquè m'indiqui si
vaig en la bona direcció.
