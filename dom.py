import pandas as pd
import random as random
# Read the CSV file
data= pd.read_csv("table2.csv")
# data['ID'] = range(1, len(data) + 1)
# column_order = ['ID'] + [col for col in data.columns if col != 'ID']
# data.iloc[:, 1] = 'META-' + data.iloc[:, 1].astype(str)
# data = data[column_order]
# View the first 5 rows

# data.insert(2,"Random",[random.randint(0,1) for i in range (0,len(data))])
data_transposed = data.T
print(data_transposed.head())
data_transposed.to_csv("table1.csv",index=False)


