# python.rpa.scripts
These are my scripts that automate working with data

Description of the folder contents:

budni - a script that automates the download of CSV / xlsx data from the SAP system, file processing and sending to FTP

DM - a script that automates the download of CSV / xlsx data from the SAP system, file processing and sending to FTP

mueller - automation script. Download the file from the email, extract it, rename it, and send it to FTP.

ftp - module for connecting to FTP. Common module for all scripts.

Unmapedpharmacy - downloads the file from ftp and compares it with the table in the database. Saves differences to the csv file and creates and inserts into the mysql database

exportdata - executes a query based on mysql, saves data to csv and sends an email with this file.
