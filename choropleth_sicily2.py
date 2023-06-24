import json
import pandas as pd
import plotly.express as px

with open('data/limits_R_19_municipalities.geojson', encoding='utf-8') as response:
    polygons = json.load(response)

url = 'https://raw.githubusercontent.com/Gangelo99/Sismicita-Sicilia/main/data/dataset_choropleth_2.csv'
df = pd.read_csv(url, index_col=0, dtype={"comune": str})

max_ag_value = df['ag'].max()
min_ag_value = df['ag'].min()

print(max_ag_value)
fig = px.choropleth_mapbox(
    df,
    geojson=polygons,
    locations='comune',
    featureidkey='properties.name',
    color="ag",
    # color_continuous_scale="Viridis",
    mapbox_style="carto-positron",
    zoom=6,
    center={'lat': 37.50000,'lon': 15.090278},
    range_color=(min_ag_value, max_ag_value),
    labels={"Classificazione sismica Sicilia"},
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_geos(fitbounds="locations", visible=True)
fig.show()