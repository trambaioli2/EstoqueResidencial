from tkinter import *
from tkinter import ttk
from CadastrarProduto import abrirCadProd
from AlterarProduto import abreAltProd
from Produto import Produto
from AdicionarGasto import abrirgasto
from AdicionarCompra import abrirCompra
from alterarusuario import altusu
from cadastrarusuario import cadusu
from criaRel import criaPDF
import os


class principal:
    def __init__(self, master=None):
        self.conteiner = Frame(master)
        self.conteiner.pack()
        self.tree = ttk.Treeview(self.conteiner, selectmode='browse', column=(
            'coluna1', 'coluna2', 'coluna3', 'coluna4', 'coluna5'), show='headings')
        self.tree.column('coluna2', width=300, minwidth=200, stretch=NO)
        self.tree.heading('#2', text='Nome')
        self.tree.column('coluna3', width=150, minwidth=100, stretch=NO)
        self.tree.heading('#3', text='Quantidade')
        self.tree.column('coluna4', width=150, minwidth=100, stretch=NO)
        self.tree.heading('#4', text='Quant Min')
        self.tree.column('coluna5', width=150, minwidth=100, stretch=NO)
        self.tree.heading('#5', text='Quant Max')
        self.tree.column('coluna1', width=75, minwidth=50, stretch=NO)
        self.tree.heading('#1', text='Id')
        self.tree.pack()
        self.preencheTree()

        self.conteiner2 = Frame(master, pady=40)
        self.conteiner2.pack()
        self.botao = Button(self.conteiner2, text="GERAR LISTA DE COMPRAS", font=(
            "Arial", "12", "bold"), width=30, height=3, bg='#B0C4DE', command=criaPDF)
        self.botao.pack()

    def preencheTree(self):
        x = Produto()
        lista = x.selectProduto()
        for i in lista:
            self.tree.insert("", END, values=i)


def abrirprincipal():
    rootp = Tk()
    posx = rootp.winfo_screenwidth()/2 - 450
    posy = rootp.winfo_screenheight()/2 - 350
    rootp.geometry('%dx%d+%d+%d' % (900, 600, posx, posy))
    rootp.title("Estoque Residencial")

    menubar = Menu(rootp)

    usumenu = Menu(menubar)
    usumenu.add_command(label="Cadastrar Usuario", command=cadusu)
    usumenu.add_command(label="Alterar Usuario", command=altusu)
    menubar.add_cascade(label="Usuario", menu=usumenu)

    def abrirCP():
        rootp.destroy()
        abrirCadProd()

    def abrirAP():
        rootp.destroy()
        abreAltProd()

    def abrirAG():
        rootp.destroy()
        abrirgasto()

    def abrirAC():
        rootp.destroy()
        abrirCompra()

    produmenu = Menu(menubar)
    produmenu.add_command(label="Cadastrar Produto", command=abrirCP)
    produmenu.add_command(label="Alterar Produto", command=abrirAP)
    menubar.add_cascade(label="Produto", menu=produmenu)

    estomenu = Menu(menubar)
    estomenu.add_command(label="Adicionar Gasto", command=abrirAG)
    estomenu.add_command(label="Adicionar Compra", command=abrirAC)
    menubar.add_cascade(label="Estoque", menu=estomenu)

    rootp.config(menu=menubar)
    rootp.focus_force()
    principal(rootp)
    rootp.mainloop()
