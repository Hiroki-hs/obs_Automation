import os
import pandas as pd


def makeExcel_fromCsv(company, statement, path_csv, path_excel):
    '''
    会社、財務諸表名、csvパス、excelパス
    '''
    
    for year in range(2008, 2020):

        filename1 = company + str(year) + statement + "JP.csv"  #csvファイル名
        filename2 = company + str(year) + statement + "JP.xlsx" #excelへ変換後のファイル名
        
        csvPath2 = path_csv + str(year) + "/"
        excelPath2 = path_excel  + str(year) + "/"
        
        df = pd.read_csv(csvPath2 + filename1, encoding="cp932")

        if (os.path.exists(excelPath2)):
            df.to_excel(excelPath2 + filename2, encoding="utf-8")
        else:
            os.mkdir(excelPath2)
            df.to_excel(excelPath2 + filename2, encoding="utf-8")
