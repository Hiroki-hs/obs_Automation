
from sys import path
from mod.preprocessing.pre1 import makeExcel_fromCsv
import numpy as np
import pandas as pd
import os

purima = "2281"
purima_path = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/excel/プリマハム/"
purima_csvPath= "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/csv/プリマハム/"
purima_excelPath="C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/excel/プリマハム/"

#財務諸表の番号
BS = "0311"
PL = "0312"
CF = "0315"


for year in range(2008,2020):
    
    filename1 = purima + str(year) + BS + "JP.csv"
    filename2 = purima + str(year) + BS + "JP.xlsx"
    path1 = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/csv/プリマハム/"
    path2 = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/excel/プリマハム/"
    df = pd.read_csv(path1 + filename1, encoding="shift-jis")
    
    if (os.path.exists(path2)):    
        df.to_excel(path2 + filename2, encoding="utf-8")
    else:
        os.mkdir(path2)
        df.to_excel(path2 + filename2, encoding="utf-8")
