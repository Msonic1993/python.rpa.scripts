import csv
import sqlite3
import time
import sys
from Constants import DB, Query
sys.stdout.write("hello from Python %s\n" % (sys.version,))

class DBSelectQuery:
    timestr = time.strftime("%Y-%m-%d")
    tempExtractFileName = "DataExtract " + timestr + ".csv"

    def ReportPharmacyDay(self):
        print("I make a query on the table report pharmacy day ... ")

        # Wykonuje query które wyświetla dane dzienne
        DBcursor = ReckittDB.cursor()
        DBcursor.execute(Query)
        try:
            #stworzenie pliku z danymi
            rows = DBcursor.fetchall()
            fp = open('C:\\temp_ZW\\' + self.tempExtractFileName, 'w' ,newline='' ,encoding="utf-8-sig")
            tempFile = csv.writer(fp)
            tempFile.writerows(rows)
            print("Total rows are:  ",DBcursor.rowcount)

            #Zmiana formatu pliku
            reader = csv.reader(open('C:\\temp_ZW\\' + self.tempExtractFileName, 'r+' ,newline='' ,encoding="utf-8-sig"), delimiter=',')
            writer = csv.writer(open('C:\\temp_ZW\\' + self.tempExtractFileName , 'r+',newline='',encoding="utf-8-sig"), delimiter=';')
            writer.writerows(reader)

        except sqlite3.Error as error:
            print("Failed to read data from table", error)

        #Zwraca scieżkę do pliku
        GetFileName = self.tempExtractFileName
        return GetFileName

    def DataSample(self):

        #wyświetla 10 pierwszych lini danych
        print("Printing data sample from file "+self.tempExtractFileName)
        with open('C:\\temp_ZW\\' + self.tempExtractFileName) as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                print(row)
                if (i >= 9):
                    break
