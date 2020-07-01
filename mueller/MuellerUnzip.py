import ftplib
from mueller.Constants import LocalName, NewName, remoteDir, ExtractFolder
from mueller.unzip import UnzipFile


class MuellerConverterXslToCsv:


    def Convert(self, remoteDir, host, user, password):

        login = ftplib.FTP(host,user,password)
        login.cwd(remoteDir)
        data = []
        login.dir(data.append)
        for line in data:
            print(line[55:59].strip())
            if line[55:59].strip() == LocalName:
                UnzipFile()
                # dst = NewName
                # src = remoteDir + line[55:].strip()
                # dst = remoteDir + dst
                #
                # ftplib.ftp.rename(login,src, dst)
                print("Rename file on ftp - Success")
        # # data_xls = pd.read_excel(LocalPath + LocalName, index_col=1)
        # data_xls.to_csv(LocalPath + NewName, encoding='utf-8')

        print("zmiana formatu pliku - sukces")



