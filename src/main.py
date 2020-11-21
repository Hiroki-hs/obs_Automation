from sys import path
from class.company import Company
from mod.preprocessing.pre1 import makeExcel_fromCsv
import class.company

#

# 分析対象の会社名をユーザーに入力させる
x = input("分析対象企業は何社ありますか？ > ")
com_list = list[]
for i in range(1, int(x)+1):
    com_i = input("分析したい企業名を入力してください > ")
    com_list.append(com_i)
    i += 1


# 企業objectを生成する
for i in range(1, int(x) + 1):
    com_i = Company()
    com_i.set_com_name(com_list[i-1])
    com_i.set_com_num()
    com_i.set_com_path()
    

# 各会社の株番号
purima = "2281"
purima_path = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/excel/プリマハム/"
purima_csvPath = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/csv/プリマハム/"
purima_excelPath = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/excel/プリマハム/"

marudai = "2288"
marudai_path = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/excel/丸大食品"
marudai_csvPath = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/csv/丸大食品/"
marudai_excelPath = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/excel/丸大食品/"

nitihamu = "2282"
nitihamu_path = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/excel/日本ハム"
nitihamu_csvPath = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/csv/日本ハム/"
nitihamu_excelPath = "C:/Users/mamum/Source/python_projects/obs_automation/financial_statements/excel/日本ハム/"

companies = [purima, marudai, nitihamu]

# 財務諸表の番号
BS = "0311"
PL = "0312"
CF = "0315"
financial_statements = [BS, PL, CF]


'''
csvファイル　→　excelファイル

➀csvファイルを読み込み、Excelとして保存
➁全角を半角へ変換する
⓷空欄を取り除く

'''

# -----------------------------------------------------------
#　➀csvファイルを読み込み、Excelとして保存
# -----------------------------------------------------------

makeExcel_fromCsv(purima, BS, purima_csvPath, purima_excelPath)
makeExcel_fromCsv(marudai, BS, marudai_csvPath, marudai_excelPath)
makeExcel_fromCsv(nitihamu, BS, nitihamu_csvPath, nitihamu_excelPath)

makeExcel_fromCsv(purima, PL, purima_csvPath, purima_excelPath)
makeExcel_fromCsv(marudai, PL, marudai_csvPath, marudai_excelPath)
makeExcel_fromCsv(nitihamu, PL, nitihamu_csvPath, nitihamu_excelPath)

makeExcel_fromCsv(purima, CF, purima_csvPath, purima_excelPath)
makeExcel_fromCsv(marudai, CF, marudai_csvPath, marudai_excelPath)
makeExcel_fromCsv(nitihamu, CF, nitihamu_csvPath, nitihamu_excelPath)
