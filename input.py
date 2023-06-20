# This py file import the dataset, use some columns and renamed them
import pandas as pd

import_dataset = pd.read_csv("classificazione_sismica.csv")

select_columns = ['ag', 'Sigla Provincia', 'Nuova Classificazione sismica']
dataset = import_dataset[select_columns]
dataset = dataset.rename(columns={'Sigla Provincia': 'province', 'Nuova Classificazione sismica': 'new_classification'})
# print(dataset.columns)