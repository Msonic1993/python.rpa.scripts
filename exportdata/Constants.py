import mysql.connector

# Dostęp do bazy PROD
DB = mysql.connector.connect(
    host="xx.xx.xx.xx",
    port="xx",
    user="xx",
    passwd="xx",
    database="xx")

xxx = "665"

Query = ("SELECT "
         "rpd.date AS DATA, "
         "ph.centralId AS ID_APTEKI, "
         "ph.address AS ULICA_APTEKI, "
         "ph.city AS MIASTO_APTEKI, "
         "pr.ean AS EAN, "
         "pr.bloz7 AS BLOZ, "
         "pr.name AS NAZWA_PRODUKTU, "
         "SUM(rpd.sell) AS SPRZEDAZ, "
         "SUM(rpd.buy) AS ZAKUP, "
         "SUM(rpd.stock) AS STAN "
         "FROM report_pharmacy_day rpd, pharmacy ph, product pr "
         "WHERE rpd.productId = pr.productId AND rpd.pharmacyId = ph.pharmacyId "
         "AND rpd.date between '2020-05-01' AND '2020-05-30' AND rpd.pharmacyId IN "
         "(SELECT pharmacyId FROM pharmacy p WHERE p.networkId =" + xxx + ") GROUP BY rpd.date, ph.kamsoftId, ph.name, pr.ean, pr.bloz7,	pr.name")
