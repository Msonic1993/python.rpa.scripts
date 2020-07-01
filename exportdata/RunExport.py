from SelectDataFromDB import DBSelectQuery
import SendMail

ExportDataFromDB = DBSelectQuery()
ExportDataFromDB.ReportPharmacyDay()
ExportDataFromDB.DataSample()
StartSending = SendMail.Send()
StartSending.SendMail()