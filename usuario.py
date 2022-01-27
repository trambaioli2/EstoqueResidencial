import sqlite3

class Usuario:
    def __init__(self, idusuario = "", nome = "", usuario = "", senha = ""):
        self.idusuario = idusuario
        self.nome = nome
        self.usuario = usuario
        self.senha = senha

   

    def setUsuario(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("insert into usuarios(nome, usuario, senha) values('"+self.nome+"', '"+self.usuario+"', '"+self.senha+"')")
        conexao.commit()

    def altUsuario(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("update usuarios set nome ='"+self.nome+"', usuario = '"+self.usuario+"', senha = '"+self.senha+"' where idusuario = "+self.idusuario+" ")
        conexao.commit()

    def delUsuario(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("delete from usuarios where idusuario = "+self.idusuario+" ")
        conexao.commit()


    def busUsuario(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("select * from usuarios where idusuario = "+self.idusuario+" ")
        return c.fetchall()       
         
    def selectUsu(self):
        conexao = sqlite3.connect("EstoqueRes.db")
        c = conexao.cursor()
        c.execute("select * from usuarios")
        return c.fetchall()

