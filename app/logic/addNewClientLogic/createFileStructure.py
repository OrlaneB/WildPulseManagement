import os

def createFileStructure(path) :
    adminPath = path+"/01-Admin"
    os.mkdir(adminPath)
    os.mkdir(adminPath+"/Factures")
    os.mkdir(adminPath+"/Droits_Auteurs")
    musicPath = path+"/02-Musique"
    os.mkdir(musicPath)
    os.mkdir(musicPath+"/Démos")
    os.mkdir(musicPath+"/Stems")
    os.mkdir(musicPath+"/Paroles")
    os.mkdir(musicPath+"/Setlists")
    concertPath = path+"/03-Concerts"
    os.mkdir(concertPath)
    os.mkdir(concertPath+"/Tournées")
    os.mkdir(concertPath+"/Fiches_Techniques")
    promotionPath = path+"/04-Promotion"
    os.mkdir(promotionPath)
    os.mkdir(promotionPath+"/Dossier_Presse")
    os.mkdir(promotionPath+"/Logos")
    os.mkdir(promotionPath+"/Photos_Officielles")
    os.mkdir(promotionPath+"/Clips")
    reseauPath = path+"/05-Réseau"
    os.mkdir(reseauPath)
    os.mkdir(reseauPath+"/Labels")
    os.mkdir(reseauPath+"/Médias")
    os.mkdir(reseauPath+"/Booking")
    notesPath = path+"/06-Notes"
    os.mkdir(notesPath)
    os.mkdir(notesPath+"/Inpirations")
    os.mkdir(notesPath+"/Réunions")
    os.mkdir(notesPath+"/Idées")