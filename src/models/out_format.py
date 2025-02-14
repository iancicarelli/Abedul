class OutFormat:
    def __init__(self,code,amount,id_local):
        self.code = code
        self.amount = amount
        self.id_local = id_local

    def __str__(self):
        return f"Format(code ={self.code}, amount ={self.amount}, id_local= {self.id_local})"    