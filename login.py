from tkinter import *
from usuario import Usuario
from tkinter import messagebox

class login:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ("Arial", "12")
        self.conteiner1 = Frame(master, padx=10, pady=10)
        self.conteiner1.pack()
        self.label1 = Label(self.conteiner1, text='Usuário: ', font=self.fonte, width=15)
        self.label1.pack(side=LEFT)
        self.usuario = Entry(self.conteiner1, font= self.fonte, width=25)
        self.usuario.pack(side=LEFT)
        
        self.conteiner2 = Frame(master, padx=10, pady=10)
        self.conteiner2.pack()
        self.label2 = Label(self.conteiner2, text='Senha: ', font=self.fonte, width=15)
        self.label2.pack(side=LEFT)
        self.senha = Entry(self.conteiner2, font=self.fonte, width=25)
        self.senha.pack(side=LEFT)

        self.conteiner3 = Frame(master, padx=10, pady=20)
        self.conteiner3.pack()
        self.botao = Button(self.conteiner3, text = 'LOGIN', font=self.fonte, width=15, command=self.logar)
        self.botao.pack()


    def logar(self):
        try:
            usu = self.usuario.get()
            sen = self.senha.get()
            c = Usuario().selectUsu()
            x = 0
            for i in c:
                if(i[2]==usu and i[3]==sen):
                    messagebox.showinfo("","Login Autorizado")
                    self.master.destroy()
                    from principal import abrirprincipal
                    abrirprincipal()
                    x = 1
                    break
                    
            
            if(x==0):
                raise
        except:
            messagebox.showinfo("","Login Não Autorizado")
        









root = Tk()
posx = root.winfo_screenwidth()/2 - 250
posy = root.winfo_screenheight()/2 - 170
root.geometry('%dx%d+%d+%d' %(500, 200, posx, posy))
root.title("Cadastro de Produto")
login(root)
root.mainloop()