import codecs

import pandas as pd

print("---Starting Compare files---")

f1 = pd.read_csv('C:\\temp_dm\\Apteki.csv', encoding="ISO-8859-1", header=None, sep=';')
f2 = pd.read_csv('C:\\temp_dm\\temp.csv', encoding="ISO-8859-1", header=None, sep=';')

# f3 = pd.concat([f2, f1[~f1[0].isin(f2[0])]])
# print(f3)
f4 = f1[~f1[0].isin(f2[0])]
print(f4)

f4.to_csv(r'C:\\temp_dm\\result.csv', index=True, header=True, encoding="ISO-8859-1")



