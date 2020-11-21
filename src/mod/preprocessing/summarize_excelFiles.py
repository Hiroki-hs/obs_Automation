from class.company import Company
import openpyxl
import class.company
import os

def summerize(com_name, com_num, com_path, statement):
    """  
    引数　：企業名、企業コード、ファイルパス、財務表識別コード(0311 or 0312 or 0315)
    戻り値：なし
    
    年度別に分かれている財務Excelを1つのブックにまとめる。
    その際、年度別のシートが作成される。
    """
    com = Company()

    com.set_com_name(com_name)

    if os.path.exists()