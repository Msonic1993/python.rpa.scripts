import csv
from unmappedpharmacy.Constants import xx, xx


# from UnmappedPharmacy.Constants import xx, xx


class Query:

            def __init__(self, insertToPharmacies=None, v=None):
                self.__insertToPharmacies = insertToPharmacies
                self.v = v
            def PrepareInsertPharmacies(self):

                global __networkId
                openFile = 'C:\\temp_dm\\result.csv'
                print("Przygotowywanie insert query na podstawie pliku " + openFile)

                # csvFile = csv.reader(openFile)
                print("skipowanie nagłówka")
                with open(openFile, 'r') as file:
                    reader = csv.reader(file)
                    skipFirstRow = list(reader)

                # skipuje pierwszy wiersz

                for item in range(1, len(skipFirstRow)):
                    # Print each row using "item" as the index value

                    # header = next(csvFile)
                    __networkId = xx
                    headers = ('networkId', 'centralId', 'teamviewerId', 'name', 'phone', 'city', 'address')
                    query = 'INSERT INTO pharmacy (' + ", ".join(headers) + ") VALUES "

                    # values = map((lambda x: "'"+ x + "'"), item)
                    self.__insertToPharmacies = (
                            query + "(" "'" + __networkId + "', '" + "', '".join(skipFirstRow[item]) + "');")

                    self.v =  print(self.__insertToPharmacies)

               # print("Wygenerowane query dla networkID " + __networkId)

            def ReturnZmienna(self):
               return  self.v

            def Print(self):
                c = Query(self)
                c.PrepareInsertPharmacies()














