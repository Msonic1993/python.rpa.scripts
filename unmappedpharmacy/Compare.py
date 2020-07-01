import csv
from builtins import print
from logging import setLogRecordFactory

import pandas as pd

class CompareFiles:

    def Compare(self):
        print("---Starting Compare files---")

        f1 = pd.read_csv('C:\\temp_dm\\Apteki.csv', encoding="Windows-1250", header=None, sep=';')
        f2 = pd.read_csv('C:\\temp_dm\\temp.csv', encoding="Windows-1250", header=None, sep=',')

        # f3 = pd.concat([f2, f1[~f1[0].isin(f2[0])]])
        # print(f3)
        f4 = f1[~f1[0].isin(f2[0])]
        print(f4)

        f4.to_csv(r'C:\\temp_dm\\result.csv', index = False, header=True,encoding="Windows-1250")



