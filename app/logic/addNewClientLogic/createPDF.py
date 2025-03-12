from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def createPDF(path,content):
    pdf = canvas.Canvas(path,pagesize=A4)

    pdf.setFont("Helvetica-Bold",16)
    x,y = 60,800
    interlignage = 15

    pdf.drawString(x,y,"Informations du groupe")
    y-=interlignage*2

    pdf.setFont("Helvetica",12)

    for line in content.split("\n") :
        pdf.drawString(x,y,line)
        y-=interlignage

    pdf.save()