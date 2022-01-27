from Produto import Produto
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

dirc = os.path.dirname(__file__)

c = Produto().selectProduto()

def criaPDF():
    cnv = canvas.Canvas(dirc+"\\ListaCompra.pdf", pagesize=A4)
    cnv.drawString(220,800,"LISTA DE COMPRAS")
    cnv.drawString(80,750,"Item")
    cnv.drawString(250,750,"Quantidade em Estoque")
    cnv.drawString(450,750,"Quantidade a Comprar")
    y = 700
    for i in c:
        if (i[2] <= i[3]):
            compra = i[4] - i[2]
            cnv.drawString(80,y,i[1])
            cnv.drawString(250,y,str(i[2]))
            cnv.drawString(450,y,str(compra))
            y -= 30



    cnv.save()
    os.system("ListaCompra.pdf")
