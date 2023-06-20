# This py file import the dataset, use some columns and renamed them
import pandas as pd

import_dataset = pd.read_csv("classificazione_sismica.csv")

select_columns = ['ag', 'Sigla Provincia', 'Nuova Classificazione sismica']
select_columns2 = ['ag', 'Sigla Provincia','Comune', 'Nuova Classificazione sismica']

dataset = import_dataset[select_columns]
dataset_2 = import_dataset[select_columns2]

dataset = dataset.rename(columns={'Sigla Provincia': 'province', 'Nuova Classificazione sismica': 'new_classification'})
dataset_2 = dataset_2.rename(columns={'Sigla Provincia': 'province','Comune': 'municipality','Nuova Classificazione sismica': 'new_classification'})
#Casting the ag columns from string to float
dataset_2['ag'] = dataset_2['ag'].str.replace(",", ".")
dataset_2['ag'] = dataset_2['ag'].astype('float')

# print(dataset_2)