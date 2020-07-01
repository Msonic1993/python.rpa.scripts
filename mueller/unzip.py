from zipfile import ZipFile


def UnzipFile():
    with ZipFile('C:\\temp_dm\\RCBK_0720.zip', 'r') as zf:
        zf.extractall('C:\\temp_dm')
        print("file unziped")
        zf.close()