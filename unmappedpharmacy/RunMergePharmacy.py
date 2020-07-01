
from unmappedpharmacy.PullMerchFile import DownloadPharmacyFiles
from unmappedpharmacy.ExecuteQuery import SqlQuery
from unmappedpharmacy.Compare import CompareFiles
from unmappedpharmacy.PrepareInsertQuery import Query

PharmacyFile = DownloadPharmacyFiles()
PharmacyFile.PullFile()

selectFromPharmacies = SqlQuery()
selectFromPharmacies.SelectPharmacies()

RunCompare = CompareFiles()
RunCompare.Compare()



InsertToBase = SqlQuery()
InsertToBase.InsertPharmacies()



