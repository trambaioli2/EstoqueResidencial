from tkinter import *
from tkinter import messagebox
from usuario import Usuario

class cadastrarusuario:
    def __init__(self, master = None):
        self.fonte = ('Arial', '12')
        self.master = master
        self.conteiner1 = Frame(master, padx = 40, pady = 10)
        self.conteiner1.pack()
        self.label1 = Label(self.conteiner1, text = "Nome: ", font = self.fonte, width = 25)
        self.label1.pack(side = LEFT)
        self.nome = Entry(self.conteiner1, font = self.fonte, width = 25)
        self.nome.pack(side = LEFT)

        self.conteiner2 = Frame(master, padx = 40, pady = 10)
        self.conteiner2.pack()
        self.label2 = Label(self.conteiner2, text = "Nome do usuario: ", font = self.fonte, width = 25 )
        self.label2.pack(side = LEFT)
        self.nome2 = Entry(self.conteiner2, font = self.fonte, width = 25)
        self.nome2.pack(side = LEFT)

        self.conteiner3 = Frame(master, padx = 40, pady = 10)
        self.conteiner3.pack()
        self.label3 = Label(self.conteiner3, text = "Senha: ", font = self.fonte, width = 25)
        self.label3.pack(side = LEFT)
        self.nome3 = Entry(self.conteiner3, font = self.fonte, width = 25)
        self.nome3.pack(side = LEFT)

        self.conteiner4 = Frame(master, padx=40, pady=10)
        self.conteiner4.pack()
        self.botao = Button(self.conteiner4, width = 20, text = "Confirmar", font = self.fonte, command=self.cadastrar)
        self.botao.pack(side=LEFT, padx = 10)
        self.sair = Button(self.conteiner4, width=20, text='Sair', font=self.fonte, command=self.Sair)
        self.sair.pack(side=RIGHT, padx=10)
    
    def cadastrar(self):
        try:
            nome = self.nome.get()
            usuario = self.nome2.get()
            senha = self.nome3.get()
            print(nome, usuario, senha)
            if(nome == "" or usuario == "" or senha == ""):
                raise 
            Usuario(nome = nome, usuario = usuario, senha = senha).setUsuario()
            messagebox.showinfo("", "Cadastrado com Sucesso!")
            self.master.destroy()
        except:
            messagebox.showinfo("","Erro ao Cadastrar")
            self.master.focus_force()
        
    def Sair(self):
        self.master.destroy()


def cadusu():
    root = Tk()
    posx = root.winfo_screenwidth()/2 - 300
    posy = root.winfo_screenheight()/2 - 200
    root.geometry('%dx%d+%d+%d' %(600, 300, posx, posy))
    root.focus_force()
    root.title("Cadastrar Usuário")
    cadastrarusuario(root)
    root.mainloop()