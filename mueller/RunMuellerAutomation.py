
from ftp.FtpConnect import FtpConnectClass
from mueller.Constants import *

FtpConnect = FtpConnectClass(host, user, password, remoteDir)
FtpConnect.uploadMueller()