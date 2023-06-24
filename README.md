# Sicily Seismicity Data Analysis
This project use the dataset taken from the Open Data of Sicily (https://dati.regione.sicilia.it/catalogo/78fe53fc-6cbb-4811-8a9e-aa31923a03f2). This dataset needs to create histograms.

## Requirements
Install the python packages present in the `requirements.txt` file

    pip3 install -r requirements.txt

## Histograms
- ### histogram_1.py - Municipalities with Level 1 of seismicity
![](https://raw.githubusercontent.com/Gangelo99/Sismicita-Sicilia/main/histograms/histogram_1.png)
This python file create the histogram of the municipalities with Level 1 of seismicity using the data calculated by the `most_dangerous1.py` file, present in the module path. 

- ### histogram_2.py - Municipalities with Level 2 of seismicity
![](https://raw.githubusercontent.com/Gangelo99/Sismicita-Sicilia/main/histograms/histogram_2.png)
This python file create the histogram of the municipalities with Level 1 of seismicity using the data calculated by the `most_dangerous2.py` file, present in the module path. 

- ### histogram_3.py - Municipalities with Level 1 & 2 of seismicity
![](https://raw.githubusercontent.com/Gangelo99/Sismicita-Sicilia/main/histograms/histogram_3.png)
This python file create the histogram of the municipalities with Level 1 & 2 of seismicity using the data calculated by the `most_dangerous1e2.py` file, present in the module path.


## Choropleth maps
- ### choropleth_sicily.py - Choropleth maps with the level of sismicity
![]([https://raw.githubusercontent.com/Gangelo99/Sismicita-Sicilia/main/histograms/histogram_1.png](https://raw.githubusercontent.com/Gangelo99/Sismicita-Sicilia/main/choropleth/choropleth_sicily.png))
This python file create the choropleth maps of the Sicily with the 4 level of seismicity. This script use the geoJSON file taken from https://github.com/openpolis/geojson-italy/blob/master/geojson/limits_R_19_municipalities.geojson and use the `dataset_choropleth.csv` present in the data path

- ### choropleth_sicily.py - Choropleth maps with the level of sismicity
![](https://raw.githubusercontent.com/Gangelo99/Sismicita-Sicilia/main/choropleth/choropleth_sicily_2.png)
This python file create the choropleth maps of the Sicily with the ag value (accelerazione massima su suolo rigido, i.e. maximum acceleration on hard ground) of seismicity. This script use the geoJSON file taken from https://github.com/openpolis/geojson-italy/blob/master/geojson/limits_R_19_municipalities.geojson and use the `dataset_choropleth_2.csv` present in the data path
