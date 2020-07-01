from builtins import print
from datetime import time
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DownloadingDMReportFiles:
    __driver = None
    __headless = True

    def __init__(self, headless=True):
        self.__headless = headless

    def __start(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": "C:\\temp_dm"}
        chromeOptions.add_experimental_option("prefs", prefs)
        chromedriver = "C:/chromedriver/chromedriver.exe"
        if (self.__headless):
            chromeOptions.add_argument("--headless")
        self.__driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions, )
        self.__driver.get(
            'https://de.dm-extranet.com/')

        user = self.__driver.find_element_by_name('UserName')
        user.send_keys('xx')
        p = self.__driver.find_element_by_name('Password')
        p.send_keys('xx')

        print("click on button_element_submit")
        button_element_submit = self.__driver.find_element_by_id('submitButton')
        button_element_submit.click()
        print("log in to portal successfully")

        button_element_Category_Management = WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="FolderIcons"]/tbody/tr[1]/td[1]/div/table/tbody/tr/td[2]/a')))
        button_element_Category_Management = self.__driver.find_element_by_xpath(
            '//*[@id="FolderIcons"]/tbody/tr[1]/td[1]/div/table/tbody/tr/td[2]/a')
        button_element_Category_Management.click()
        print("click on button_element_Category_Management")

    def __clickWhone(self, __driver):
        __driver = self.__driver
        button_element_Umsatz_wochentlich = WebDriverWait(self.__driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="FolderIcons"]/tbody/tr[5]/td/div/table/tbody/tr/td[2]/a')))
        time.sleep(2)
        button_element_Umsatz_wochentlich = self.__driver.find_element_by_xpath(
            '//*[@id="FolderIcons"]/tbody/tr[5]/td/div/table/tbody/tr/td[2]/a')
        print(button_element_Umsatz_wochentlich)
        button_element_Umsatz_wochentlich.click()

    def __clichUmsatz(self, __driver):
        __driver = self.__driver
        button_element_Menge_stuck = WebDriverWait(__driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="FolderIcons"]/tbody/tr[3]/td[2]/div/table/tbody/tr/td[2]')))
        time.sleep(2)
        button_element_Menge_stuck = __driver.find_element_by_xpath(
            '//*[@id="FolderIcons"]/tbody/tr[3]/td[2]/div/table/tbody/tr/td[2]')
        print("click on button_element_Menge_stuck")
        button_element_Menge_stuck.click()

    def __download(self):

        dd = WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_mstr133"]/img')))
        add = self.__driver.find_element_by_xpath('//*[@id="id_mstr133"]/img')
        add.click()

        mstrPromptTOCListItemTitle = self.__driver.find_element_by_xpath(
            '//*[@id="id_mstr78"]/table/tbody/tr[10]/td[2]')
        mstrPromptTOCListItemTitle.click()
        self.__driver.implicitly_wait(2)
        print("click mstrPromptTOCListItemTitle")

        mstrCheckListItemSelected = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='id_mstr266ListContainer']/div[3]/div")))
        mstrCheckListItemSelected = self.__driver.find_element_by_xpath(
            "//div[@id='id_mstr266ListContainer']/div[3]/div")
        mstrCheckListItemSelected.click()

        mstrCheckListItem = self.__driver.find_element_by_xpath('//*[@id="id_mstr253"]')
        mstrCheckListItem.click()

        # addDate = WebDriverWait(self.__driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//*[@id='id_mstr50']")))
        for x in range(5):
            if x < 5:
                addDate = self.__driver.find_element_by_xpath("//*[@id='id_mstr50']")
                addDate.click()

        runReport = self.__driver.find_element_by_xpath('//*[@id="id_mstr59"]')
        runReport.click()
        print("run reports... ")
        mstrListBlockToolbarItemName = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="ribbonToolbarTabsListContainer"]/div[1]/table/tbody/tr/td[2]')))
        mstrListBlockToolbarItemName = self.__driver.find_element_by_xpath(
            '//*[@id="ribbonToolbarTabsListContainer"]/div[1]/table/tbody/tr/td[2]')
        mstrListBlockToolbarItemName.click()
        time.sleep(2)

        mstrListBlockToolbarItemName = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="ribbonToolbarTabsListContainer"]/div[3]/table/tbody/tr/td[2]')))
        mstrListBlockToolbarItemName = self.__driver.find_element_by_xpath(
            '//*[@id="ribbonToolbarTabsListContainer"]/div[3]/table/tbody/tr/td[2]')
        mstrListBlockToolbarItemName.click()

        showTotals = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tbToggleTotals"]')))
        showTotals = self.__driver.find_element_by_xpath('//*[@id="tbToggleTotals"]')
        showTotals.click()
        time.sleep(2)
        ReportHome = WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ribbonToolbarTabsListContainer"]/div[1]')))
        ReportHome = self.__driver.find_element_by_xpath('//*[@id="ribbonToolbarTabsListContainer"]/div[1]')
        ReportHome.click()

        export = self.__driver.find_element_by_xpath('//*[@id="tbExport"]')
        export.click()
        c

        exportHeadersAsText = WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="exportFormatGrids_excelPlaintextIServer"]')))
        exportHeadersAsText = self.__driver.find_element_by_xpath('//*[@id="exportFormatGrids_excelPlaintextIServer"]')
        exportHeadersAsText.click()

        export_button2 = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="3131"]')))
        export_button2 = self.__driver.find_element_by_xpath('//*[@id="3131"]')
        export_button2.click()
        time.sleep(10)
        print("reports downloaded to local directory")
        print("start downloading another file")
        self.__driver.quit()

    def donwloadWhonelishTemp(self):
        return "C:\\temp_dm\\Umsatz wöchentlich.xlsx"

    def donwloadStuckTemp(self):
        return "C:\\temp_dm\\Menge (Stück) wöchentlich.xlsx"

    def downloadValue(self):
        self.__start()
        self.__clickWhone(self.__driver)
        self.__download()
        return "C:\\temp_dm\\Umsatz wöchentlich.xlsx"

    def downloadVolume(self):
        self.__start()
        self.__clichUmsatz(self.__driver)
        self.__download()
        return "C:\\temp_dm\\Menge (Stück) wöchentlich.xlsx"

    def downloadFiles(self):
        self.downloadValue()
        self.downloadVolume()
