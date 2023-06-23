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
