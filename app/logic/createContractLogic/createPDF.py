from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from app.logic.createContractLogic.contractText import contractText
from app.logic.readJSONfile import readJSONFile

p = os.path

def createPDF(contractInfo):
    pathForPDF = readJSONFile("app/logic/parameters","pathClientFile")+"\\"+contractInfo["groupName"]+"\\Contrat.pdf"

    pdf = canvas.Canvas(pathForPDF,pagesize=A4)
    textContent = contractText(contractInfo)

    interlignage = 15
    maxChar = 100

    x,y = 60,800

    pdf.setFont("Helvetica-Bold",16)
    pdf.drawString(x,y,"CONTRAT DE REPRESENTATION ET DE GESTION ARTISTIQUE")
    y-=interlignage*1.5

    pdf.setFont("Helvetica-Bold",12)
    pdf.drawString(x,y,"Wild Pulse Management")
    y-= interlignage*3

    pdf.setFont("Helvetica",10)

    for line in textContent.split("\n") :
        
        while(len(line)>maxChar):
            indexEndLine = line[maxChar:].find(" ")

            if indexEndLine != -1:
                smallLine = line[:maxChar + indexEndLine]
                line = line[maxChar + indexEndLine:]
            else :
                smallLine = line
                line = ""

            pdf.drawString(x,y,smallLine)
            y-=interlignage

        pdf.drawString(x,y,line)
        y-=interlignage

    pdf.save()