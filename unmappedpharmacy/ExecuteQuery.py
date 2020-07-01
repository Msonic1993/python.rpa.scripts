import csv
import mysql.connector
# from UnmappedPharmacy.Constants import xx, xx, xx
from unmappedpharmacy.Constants import xx, xx, xx
from unmappedpharmacy.PrepareInsertQuery import *



class SqlQuery():


    def SelectPharmacies(self):
        # DBcursor = xx.cursor()

        # #Query dla xx xx
        # DBcursor = xx.cursor()
        # DBcursor.execute("SELECT ph.xx, ph.xx, ph.xx, ph.xx, ph.xx, ph.xx "
        #                  "FROM pharmacy ph "
        #                  "join network ne on ne.networkId = ph.networkid "
        #                  "WHERE ne.networkId =" + xx + " and OmitInNumerical = 0" " ORDER BY ph.centralId+1")

    

        rows = DBcursor.fetchall()

        for x in rows:
            print(x)
        fp = open('C:\\temp_dm\\temp.csv', 'w',newline='')
        tempFile = csv.writer(fp)
        tempFile.writerows(rows)



    def InsertPharmacies(self):
        c = Query()
        c.Print()

        # DBcursor = PfizerDB.cursor()
        # DBcursor.execute(self.insertToPharmacies)

        print("wykonano Query ")
