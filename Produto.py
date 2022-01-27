import sqlite3


class Produto:
    def __init__(self, idproduto="", nome="", quantidade = "", quantmin="", quantmax = ""):
        self.nome = nome
        self.quantidade = quantidade
        self.quantmin = quantmin
        self.quantmax = quantmax
        self.idproduto = idproduto

    def criarProduto(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("insert into Produtos(nome, quantidade, quantmin, quantmax) values ('"+self.nome+"',"+self.quantidade+","+self.quantmin+","+self.quantmax+")")
        conexao.commit()

    def selectProduto(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("""

        select * from produtos
        
        """)
        return c.fetchall()
    
    def buscarProduto(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("select * from produtos where idproduto = "+self.idproduto+" ")
        return c.fetchall()

    def deletaProduto(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("delete from produtos where idproduto = "+self.idproduto+" ")
        conexao.commit()

    def alteraProduto(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("update produtos set nome='"+self.nome+"', quantmin="+self.quantmin+", quantmax="+self.quantmax+" where idproduto ="+self.idproduto+" ")
        conexao.commit()
    
    def gastoProd(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("update produtos set quantidade="+self.quantidade+" where idproduto ="+self.idproduto+" ")
        conexao.commit()