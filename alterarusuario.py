from tkinter import *
from tkinter import messagebox
from usuario import Usuario

class alterarusuario:
    def __init__(self, master = None):
        self.master = master
        self.fonte = ('Arial', '12')
        self.conteiner1 = Frame(master, padx = 40, pady = 10)
        self.conteiner1.pack()
        self.label1 = Label(self.conteiner1, text = "Id do usuario:", font = self.fonte, width = 20)
        self.label1.pack(side = LEFT)
        self.nome = Entry(self.conteiner1, font = self.fonte, width = 30)
        self.nome.pack(side = LEFT)
        self.botao = Button(self.conteiner1, width = 25, text = "Buscar", command = self.buscar)
        self.botao.pack(side = RIGHT)

        self.conteiner2 = Frame(master, padx = 40, pady = 10)
        self.conteiner2.pack()
        self.label2 = Label(self.conteiner2, text = "Nome do usuario: ", font = self.fonte, width = 15)
        self.label2.pack(side = LEFT)
        self.nome2 = Entry(self.conteiner2, font = self.fonte, width = 25)
        self.nome2.pack(side = LEFT)

        self.conteiner3 = Frame(master, padx = 40, pady = 10)
        self.conteiner3.pack()
        self.label3 = Label(self.conteiner3, text = "Senha: ", font = self.fonte, width = 15)
        self.label3.pack(side = LEFT)
        self.nome3 = Entry(self.conteiner3, font = self.fonte, width = 25)
        self.nome3.pack(side = LEFT)

        self.conteiner4 = Frame(master, padx = 40, pady = 10)
        self.conteiner4.pack()
        self.botao2 = Button(self.conteiner4, width = 25, text = "Alterar", command = self.alterar)
        self.botao2.pack(side = LEFT)
        self.botao3 = Button(self.conteiner4, width = 25, text = "Excluir", command = self.deletar)
        self.botao3.pack(side = LEFT)
        self.sair = Button(self.conteiner4, width=15, text='Sair', font=self.fonte, command=self.Sair)
        self.sair.pack(side=RIGHT, padx=10)

    def buscar(self):
        try:
            id = self.nome.get()
            x = Usuario(idusuario = id).busUsuario()
            i = x[0]
            self.nome2.delete(0,END)
            self.nome2.insert(INSERT, i[2])
            self.nome3.delete(0, END)
            self.nome3.insert(INSERT, i[3])
        except:
            messagebox.showinfo("", "Usuario Inexistente")
            self.master.focus_force()

    def alterar(self):
        try:
            usuario = self.nome2.get()
            senha = self.nome3.get()
            id = self.nome.get()
            Usuario(usuario=usuario, senha=senha, idusuario=id).altUsuario()
            messagebox.showinfo("","Alterado com Sucesso")
            self.nome2.delete(0, END)
            self.nome3.delete(0, END)
            self.nome.delete(0, END)
            self.nome.focus_force()
        except:
            messagebox.showinfo("", "Erro ao Alterar")


    def deletar(self):
        try:
            id = self.nome.get()
            Usuario(idusuario=id).delUsuario()
            messagebox.showinfo("","Deletado com sucesso")
            self.nome2.delete(0, END)
            self.nome3.delete(0, END)
            self.nome.delete(0, END)
            self.nome.focus_force()
        except:
            messagebox.showinfo("", "Erro ao deletar")

    def Sair(self):
            self.master.destroy()
            


def altusu():
    root = Tk()
    posx = root.winfo_screenwidth()/2 - 300
    posy = root.winfo_screenheight()/2 - 200
    root.geometry('%dx%d+%d+%d' %(600, 300, posx, posy))
    root.focus_force()
    root.title("Alterar Usuário")
    alterarusuario(root)
    root.mainloop()