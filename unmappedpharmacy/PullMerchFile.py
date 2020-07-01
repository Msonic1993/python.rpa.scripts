import csv
import ftplib
import os
from ftplib import FTP
from ftp.FtpConnect import FtpConnectClass
# from UnmappedPharmacy.Constants import host, user, password, RemoteName, xx, xx
from unmappedpharmacy.Constants import host, user, password, xx, xx


class DownloadPharmacyFiles:

    __remoteDir = None

    def __init__(self):
        self.__remoteDir = RBPartnerPlusRemoteDir

    def PullFile(self):
        ftp = ftplib.FTP(host, user, password)
        self.files = ftp.dir(self.__remoteDir)
        ftp.cwd(self.__remoteDir)
        filematch = 'Apteki.csv'
        TargetDir = 'C:/temp_dm'

        for filename in ftp.nlst(filematch):                                        #download files from FTP server
            print("Starting downloading file Apteki.csv from FTP "+self.__remoteDir)
            TargetFileName = os.path.join(TargetDir, os.path.basename(filename))
            with open(TargetFileName,'wb') as fhandle:
                    ftp.retrbinary('RETR %s' % filename, fhandle.write)
                    print("File downloaded")


                                                                                 # # deletes the files from the FTP after transfer
                #     ftp.delete(os.path.basename(filename))


