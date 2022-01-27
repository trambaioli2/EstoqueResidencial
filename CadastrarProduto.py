from tkinter import *
from tkinter import messagebox
from Produto import Produto

class CadProduto:
    def __init__(self, master=None):
        self.fonte = ('Arial', '12')
        self.master = master
        self.conteiner1 = Frame(master)
        self.conteiner1["padx"]=40
        self.conteiner1["pady"]=10
        self.conteiner1.pack()
        self.label1 = Label(self.conteiner1, text='Nome do Produto: ', font=self.fonte, width=25)
        self.label1.pack(side=LEFT)
        self.nomepro = Entry(self.conteiner1, font=self.fonte, width=26)
        self.nomepro.pack(side=LEFT)

        self.conteiner2 = Frame(master)
        self.conteiner2["padx"]=40
        self.conteiner2["pady"]=10
        self.conteiner2.pack()
        self.label2 = Label(self.conteiner2, text='Quantidade inicial do Produto: ', font=self.fonte, widt=25)
        self.label2.pack(side=LEFT)
        self.quantpro = Spinbox(self.conteiner2, font=self.fonte, width=25, from_=0.0, to=10000.0, increment=1.0)
        self.quantpro.pack(side=LEFT)

        self.conteiner3 = Frame(master)
        self.conteiner3["padx"]=40
        self.conteiner3["pady"]=10
        self.conteiner3.pack()
        self.label3 = Label(self.conteiner3, text='Quantidade mínima: ', font=self.fonte, widt=25)
        self.label3.pack(side=LEFT)
        self.minpro = Spinbox(self.conteiner3, font=self.fonte, width=25, from_=0.0, to=10000.0, increment=1.0)
        self.minpro.pack(side=LEFT)

        self.conteiner4 = Frame(master)
        self.conteiner4["padx"]=40
        self.conteiner4["pady"]=10
        self.conteiner4.pack()
        self.label4 = Label(self.conteiner4, text='Quantidade máxima: ', font=self.fonte, widt=25)
        self.label4.pack(side=LEFT)
        self.maxpro = Spinbox(self.conteiner4, font=self.fonte, width=25, from_=0.0, to=10000.0, increment=1.0)
        self.maxpro.pack(side=LEFT)

        self.conteiner5 = Frame(master)
        self.conteiner5["padx"]=40
        self.conteiner5["pady"]=10
        self.conteiner5.pack()
        self.botao = Button(self.conteiner5, width=20, text='Cadastrar Produto', font=self.fonte, command = self.cadastrar)
        self.botao.pack(side=LEFT, padx=10)
        self.sair = Button(self.conteiner5, width=20, text='Sair', font=self.fonte, command=self.Sair)
        self.sair.pack(side=RIGHT, padx=10)

    def cadastrar(self):
        try:
            nome = self.nomepro.get()
            quantidade = self.quantpro.get()
            quantmin = self.minpro.get()
            quantmax = self.maxpro.get()
            Produto(nome=nome, quantidade=quantidade, quantmin=quantmin, quantmax=quantmax).criarProduto()
            messagebox.showinfo("","Produto Cadastrado com Sucesso!")
            self.master.destroy()
            from principal import abrirprincipal
            abrirprincipal()
        except:
            messagebox.showinfo("", "Erro ao Cadastrar")

    def Sair(self):
            self.master.destroy()
            from principal import abrirprincipal
            abrirprincipal()
    
def abrirCadProd():
    root = Tk()
    posx = root.winfo_screenwidth()/2 - 300
    posy = root.winfo_screenheight()/2 - 200
    root.geometry('%dx%d+%d+%d' %(600, 300, posx, posy))
    root.title("Cadastro de Produto")

    CadProduto(root)
    root.mainloop()    

