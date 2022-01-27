from tkinter import *
from Produto import Produto
from tkinter import messagebox

class AdicionarCompra:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ('Arial', '12')
        self.conteiner1= Frame(master, padx=40, pady=30)
        self.conteiner1.pack()
        self.label1 = Label(self.conteiner1, font=self.fonte, text='Id do Produto: ', width=12)
        self.label1.pack(side=LEFT)
        self.idProd = Entry(self.conteiner1, font=self.fonte, width=10)
        self.idProd.pack(side=LEFT)
        self.botao1 = Button(self.conteiner1, font=self.fonte, text='Buscar', width=8, command=self.buscar)
        self.botao1.pack(side=RIGHT, padx=10)

        self.conteiner2 = Frame(master, padx=40, pady=10)
        self.label2 = Label(self.conteiner2, text='Produto selecionado: ', width=25, font=self.fonte)
        self.label3 = Label(self.conteiner2, text='---------', width=25, font=self.fonte)
        self.conteiner2.pack()
        self.label2.pack(side=LEFT)
        self.label3.pack(side=LEFT)

        self.conteiner3 = Frame(master, padx=40, pady=10)
        self.conteiner3.pack()
        self.label4 = Label(self.conteiner3, text='Quantidade Adiquirida: ', width=25, font=self.fonte)
        self.label4.pack(side=LEFT)
        self.compra = Spinbox(self.conteiner3, width=25, font = self.fonte, from_=0.0, to=10000.0, increment=1.0)
        self.compra.pack(side=LEFT)

        self.conteiner4 = Frame(master, padx=40, pady=30)
        self.conteiner4.pack()
        self.botao = Button(self.conteiner4, text='Adicionar Compra', font=self.fonte, width=18, command=self.adcompra)
        self.botao.pack(side=LEFT, padx=10)
        self.sair = Button(self.conteiner4, text='SAIR', width=18, command = self.sair, font=self.fonte)
        self.sair.pack(side=LEFT, padx=10)

    def adcompra(self):
        try:
            c = Produto(idproduto=self.idProd.get()).buscarProduto()
            i = c[0]
            f = i[2] + float(self.compra.get())
            Produto(idproduto=self.idProd.get() ,quantidade=str(f)).gastoProd()
            messagebox.showinfo("", "Compra Adicionada com Sucesso!")
        except:
            messagebox.showinfo("", "Gasto inválido")

    def buscar(self):
        try:
            c = Produto(idproduto=self.idProd.get()).buscarProduto()
            i = c[0]
            self.label3["text"]=i[1]
        except:
            messagebox.showinfo("","Produto Inexistente")

    def sair(self):
        self.master.destroy()
        from principal import abrirprincipal
        abrirprincipal()

def abrirCompra():
    root = Tk()
    AdicionarCompra(root)
    posx = root.winfo_screenwidth()/2 - 300
    posy = root.winfo_screenheight()/2 - 200
    root.geometry('%dx%d+%d+%d' %(600, 300, posx, posy))
    root.title("Adicionar Gasto")
    root.focus_force()
    root.mainloop()