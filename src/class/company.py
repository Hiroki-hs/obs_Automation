class Company:
    """
    分析対象会社を表すクラス
    
    フィールド
    　com_name : 会社名
    　com_num  : 株式番号
    　com_path : 会社の財務諸表へのパス
    """
    def __init__(self):
        
        self.com_name = ""
        self.com_num = ""
        self.com_path = ""
    
    #----------setter-------------------------------------
    def set_com_name(self, com_name):
 
        self.com_name = com_name
        
    def set_com_num(self, com_num):
 
        self.com_num = com_num

    def set_com_path(self, com_path):

        self.com_path = com_path

    #----------getter-------------------------------------
    def get_com_name(self):
 
        return self.com_name
        
    def get_com_num(self):
 
        return self.com_num

    def get_com_path(self):

        return self.com_path
    
    #企業名から証券コードを検索（EDINET）
    def get_Code(com_name):
        """
        企業名は EDNINET の記載通り
        """
        
        code = 0
        
        return code