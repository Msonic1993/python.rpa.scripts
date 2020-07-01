import time
import os

from dm.DMPortal import DownloadingDMReportFiles
from ftp.FtpConnect import FtpConnectClass

obj = DownloadingDMReportFiles(True)
obj.downloadFiles()



timestr = time.strftime("%Y-%m-%d")
ftp = FtpConnectClass('xx.xx.xx', 'xx', 'xx!', '/xx/xx-common/common-etl/x-x-germany/x-x-etl/dm-raw/raw/out')

filePath = obj.donwloadWhonelishTemp()
filePath1 = obj.donwloadStuckTemp()

remoteName = "xx_Germany_xx_Value_Raw-"+timestr+".xlsx"
remoteName1 = "xx_Germany_xx_Amount_Raw-"+timestr+".xlsx"

ftp.uploadDM(filePath, remoteName, filePath1, remoteName1,)

os.remove(filePath)
os.remove(filePath1)
print("old files removed temp directory is clear")

# file = obj.donwloadUmsatz()
# ftpUpload.upload(file)
