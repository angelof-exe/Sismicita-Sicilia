# This file sort all municipalities by ag value (Only the first 5 municipalities with the highest ag value")
from input import dataset_2 as dataset


dataset = dataset[dataset['ag'] >= 0.25].sort_values(by='ag', ascending=False).head(5)

municipalities = dataset['municipality'].to_list()
province = dataset['province'].to_list()
ag_value = dataset['ag'].to_list()
# print(dataset)

for i in range(len(municipalities)):
    municipalities[i] = municipalities[i] + " (" + province[i] + ")"

# print(municipalities)
# print(province)
# print(ag_value)
