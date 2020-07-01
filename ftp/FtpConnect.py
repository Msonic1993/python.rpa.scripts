import ftplib

import wget

from rossmann.xlsToCsv import ConverterXslToCsv
from rossmann.Constants import *
from mueller.MuellerUnzip import MuellerConverterXslToCsv


class FtpConnectClass:
    __session = None
    __host = None
    __user = None
    __pass = None
    __remoteDir = None

    def __init__(self, host, user, password, remoteDir):
        self.__password = password
        self.__user = user
        self.__host = host
        self.__remoteDir = remoteDir

    def __session(self):
        # sending  files form local directory to ftp
        print("open session ftp")
        self.__session = ftplib.FTP(self.__host, self.__user, self.__password)
        print("ftp login successfully")

    def __FTPListFilesRossmann(self):
        self.__session.cwd(self.__remoteDir)
        dir_list = []
        print("------Files list--------- " + self.__remoteDir)
        self.__session.dir(dir_list.append)

        for line in dir_list:
            print(line[29:].strip().split(' '))

    def __selectFiles(self, filePath, filePath1, remoteName, remoteName1):
        self.__session.cwd(self.__remoteDir)
        f = open(filePath, 'rb')
        self.__session.storbinary('STOR ' + remoteName, f)
        f = open(filePath1, 'rb')
        self.__session.storbinary('STOR ' + remoteName1, f)
        f.close()

    def __selectFilesREWE(self, FilePath, remoteName):
        self.__session.cwd(self.__remoteDir)
        f = open('C:\\temp_dm\\rsaUTF8.csv', 'rb')
        self.__session.storbinary('STOR ' + remoteName, f)
        print("Sending files to ftp directory "+remoteName)
        f.close()

    def __closeSession(self):
        self.__session.quit()
        print("Close session ftp")

    def uploadDM(self, filePath, filePath1, remoteName, remoteName1):
        self.__session()
        self.__selectFiles(filePath, remoteName, filePath1, remoteName1)
        self.__closeSession()

    def uploadRossmann(self):
        self.__session()
        self.__FTPListFilesRossmann()
        a = ConverterXslToCsv()
        a.Convert(self.__remoteDir, host, user, password)
        self.__closeSession()

    def uploadREWE(self, FilePath, remoteName):
        self.__session()
        self.__selectFilesREWE(FilePath, remoteName)
        self.__closeSession()

    def uploadMueller(self):
        self.__session()
        self.__FTPListFilesRossmann()
        a = MuellerConverterXslToCsv()
        a.Convert(self.__remoteDir, host, user, password)
        self.__closeSession()

    def PullIpraPharmacy(self):
        self.__session()
        link = 'ftp://ftp/Apteki.csv'
        wget.download(link)
        self.__closeSession()
