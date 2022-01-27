from tkinter import *
from Produto import Produto
from tkinter import messagebox

class AlteraProduto:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ('Arial', '12')
        self.conteiner1= Frame(master, padx=40, pady=30)
        self.conteiner1.pack()
        self.label1 = Label(self.conteiner1, font=self.fonte, text='Id do Produto: ', width=12)
        self.label1.pack(side=LEFT)
        self.idProd = Entry(self.conteiner1, font=self.fonte, width=10)
        self.idProd.pack(side=LEFT)
        self.botao1 = Button(self.conteiner1, font=self.fonte, text='Buscar', width=8, command=self.busca)
        self.botao1.pack(side=RIGHT, padx=10)

        self.conteiner2 = Frame(master, padx=40, pady = 10)
        self.conteiner2.pack()
        self.label2 = Label(self.conteiner2, text='Nome do Produto: ', font=self.fonte, width=25)
        self.label2.pack(side=LEFT)
        self.nomepro = Entry(self.conteiner2, font=self.fonte, width=26)
        self.nomepro.pack()

        self.conteiner3 = Frame(master, padx=40, pady = 10)
        self.conteiner3.pack()
        self.label3 = Label(self.conteiner3, text='Quantidade mínima: ', font=self.fonte, widt=25)
        self.label3.pack(side=LEFT)
        self.quantmin = Spinbox(self.conteiner3, font=self.fonte, width=25, from_=0.0, to=10000.0, increment=1.0)
        self.quantmin.pack(side=LEFT)

        self.conteiner4 = Frame(master, padx=40, pady = 10)
        self.conteiner4.pack()
        self.label4 = Label(self.conteiner4, text='Quantidade máxima: ', font=self.fonte, widt=25)
        self.label4.pack(side=LEFT)
        self.quantmax = Spinbox(self.conteiner4, font=self.fonte, width=25, from_=0.0, to=10000.0, increment=1.0)
        self.quantmax.pack(side=LEFT)

        self.conteiner5 = Frame(master, padx=40, pady=10)
        self.conteiner5.pack()
        self.alterar = Button(self.conteiner5, width=15, text='Alterar', font=self.fonte, command=self.altera)
        self.alterar.pack(side=LEFT,padx=10)
        self.excluir = Button(self.conteiner5, width=15, text='Excluir', font=self.fonte, command=self.deleta)
        self.excluir.pack(side=LEFT, padx=10)
        self.sair = Button(self.conteiner5, width=15, text='Sair', font=self.fonte, command=self.Sair)
        self.sair.pack(side=RIGHT, padx=10)

    def busca(self):
        c = Produto(idproduto=self.idProd.get()).buscarProduto()
        for i in c:
            self.nomepro.delete(0, END)
            self.quantmin.delete(0, END)
            self.quantmax.delete(0, END)
            self.nomepro.insert(INSERT, i[1])
            self.quantmin.insert(INSERT, str(i[3]))
            self.quantmax.insert(INSERT, str(i[4]))
    
    def deleta(self):
        try:
            Produto(idproduto=self.idProd.get()).deletaProduto()
            messagebox.showinfo("","Produto Excluído com Sucesso!")
            self.master.destroy()
            from principal import abrirprincipal
            abrirprincipal()
        except:
            messagebox.showinfo("Aviso","Erro ao Excluir")

    def altera(self):
        try:
            Produto(nome=self.nomepro.get(), quantmin=self.quantmin.get(), quantmax=self.quantmax.get(), idproduto=self.idProd.get()).alteraProduto()
            messagebox.showinfo("","Produto Alterado com Sucesso!")
            self.master.destroy()
            from principal import abrirprincipal
            abrirprincipal()
        except:
            messagebox.showinfo("Aviso","Erro ao Alterar")
    
    def Sair(self):
        self.master.destroy()
        from principal import abrirprincipal
        abrirprincipal()
        



def abreAltProd():
    root = Tk()
    posx = root.winfo_screenwidth()/2 - 300
    posy = root.winfo_screenheight()/2 - 200
    root.geometry('%dx%d+%d+%d' %(600, 300, posx, posy))
    root.title("Alterar Produto")
    AlteraProduto(root)
    root.mainloop()

#abreAltProd()