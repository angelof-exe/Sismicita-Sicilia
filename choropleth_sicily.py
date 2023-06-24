import json
import pandas as pd
import plotly.express as px

with open('data/limits_R_19_municipalities.geojson', encoding='utf-8') as response:
    polygons = json.load(response)

url = 'https://raw.githubusercontent.com/Gangelo99/Sismicita-Sicilia/main/dataset_choropleth.csv'
df = pd.read_csv(url, index_col=0, dtype={"comune": str})
df['classificazione'] = df['classificazione'].astype(str)

fig = px.choropleth_mapbox(
    df,
    geojson=polygons,
    locations='comune',
    featureidkey='properties.name',
    color="classificazione",
    # color_continuous_scale="Viridis",
    # color_discrete_sequence=4,
    color_discrete_map={'4': 'Green',
                        '3': 'Yellow',
                        '2': 'Orange',
                        '1': 'red'},
    mapbox_style="carto-positron",
    zoom=6,
    center={'lat': 37.50000,'lon': 15.090278},
    range_color=(1, 4),
    labels={"Classificazione sismica sicilia"},
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_geos(fitbounds="locations", visible=True)
fig.show()