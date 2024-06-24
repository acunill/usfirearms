#!/usr/bin/env python
# coding: utf-8
"""Mapes coroplètics

Conté la funció per generar els mapes de l'exercici 6

Funcions:

    * map_choropleth - genera mapes coroplètics amb les dades dels estats.
"""

import io
import pandas as pd
import folium  # leaflet API
from PIL import Image  # Image processing capabilities (Pillow)
# import selenium  # Activate if needed

def map_choropleth(data: pd.DataFrame, variable: str,
                   legend_name: str, output_filepath: str) -> None:
    """Crea un mapa coroplètic i el desa en un arxiu png.

    Genera un mapa coroplètic de la variable d'interés especificada
    sobre un mapa base obtingut de la llibreria folium (leaflet API).

    Args:
      data (pd.DataFrame): Dades per visualitzar en el gràfic.
      variable (str): Variable d'interés a mostrar en el mapa.
      legend_name (str): Nom de la llegenda.
      output_filepath (str): Directori i nom de l'arxiu a exportar el mapa.

    Returns:
      Retorna el mapa generat en un arxiu png dins la ruta especificada.
    """
    # Get basemap of US
    url = (
        "https://raw.githubusercontent.com/python-visualization/" +
        "folium/main/examples/data"
    )
    state_geo = f"{url}/us-states.json"

    # Initialize the map and store it in a m object
    basemap = folium.Map(location=[41, -100], zoom_start=4, font_size="1.5rem")

    # Add data layer to de m object
    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=data,
        columns=["code", variable],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=.1,
        legend_name=legend_name,
    ).add_to(basemap)
    folium.LayerControl().add_to(basemap)

    # Export map as png
    img_data = basemap._to_png(5)  # pylint: disable=W0212
    img = Image.open(io.BytesIO(img_data))
    img.save(output_filepath)
