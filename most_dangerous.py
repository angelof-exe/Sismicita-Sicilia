# This file filters all municipalities with classification level 1
# and calculates how many of these municipalities are present in the province
from input import dataset

# Group by Province and then count how many municipalities are classificated Level 1, then sorting them
dataset = dataset[dataset['new_classification'] == 1].groupby(by='province').count().sort_values(by='new_classification', ascending=False)
dataset = dataset['new_classification']

# Converting datas in list
province = dataset.index.to_list()  # Take the province and insert in a list
number = dataset.to_list()  # Take the numbers of the municipalities of every province and insert in a list

# print(province)
# print(number)
# print(dataset)
