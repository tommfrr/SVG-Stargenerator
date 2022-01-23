import math
import random


def create_Ergebnisdatei():
    #Datei welche die Pfade enthält wird erzeugt 
    try:
        ergebnisdatei = open("ergebnis.txt", 'x')
    except FileExistsError:
        ergebnisdatei = open("ergebnis.txt", 'w')
    ergebnisdatei.write("")
    ergebnisdatei.close()


def get_Pfadende():
    #Auslesen der pfadEnde Datei
    pfadEnde = f""
    file = open("pfadEnde.txt") #die Datei muss sich im selben Ordner befinden
    for line in file:
        pfadEnde+=line.rstrip()
    file.close()
    return pfadEnde


def drawStern(posX, posY, anzahlEcken, radius, pfadEnde):
    ra = radius     #Radius des äußeren Kreises
    ri = radius*0.3 #Radius des inneren Kreises
    pi = math.pi
    alpha = 2*pi/anzahlEcken/2 #Kleinster Winkel

    curX = 0         #aktuelles x
    curY = 0         #aktuelles y
    curAlpha = alpha #aktueller Winkel

    #Erstellen des Pfades
    pfad = f"<path d=\"M {posX} {posY - ra} " #Cursor an Startposition bewegt

    #Pro Schleifendurchlauf wird String um 2 Punkte erweitert (innerer und äußerer Kreis)
    for i in range(anzahlEcken):
        
        #Berechnen des nächsten Punktes (innerer Ring)
        curX = round(ri * math.sin(curAlpha) + posX) 
        curY  = round(-ri * math.cos(curAlpha) + posY)

        #Ergänzen des Pfades (Punkt am inneren Ring)
        pfad += f"L {curX} {curY } "

        #Winkel eine Einheit weitersetzen
        curAlpha += alpha 
        
        #Berechnen des nächsten Punktes (äußerer Ring)
        curX = round(ra * math.sin(curAlpha) + posX)
        curY  = round(-ra * math.cos(curAlpha) + posY)

        #Ergänzen des Pfades (Punkt am äußeren Ring)
        pfad += f"L {curX} {curY} "

        #Winkel eine Einheit weitersetzen
        curAlpha += alpha

    #Abschließen der Pfadanweisung
    pfad += pfadEnde

    pfad = pfad.replace("{posX}",str(posX))
    pfad = pfad.replace("{posY}",str(posY))
    
    #Pfad-String wird ausgegeben
    return pfad


def drawSterne(anzahlSterne):
    eckenliste = [5,8,10,15,18,30] #mögliche Anzahlen für die Ecken
    pfadEnde= get_Pfadende() #Deklarieren des Pfadende Strings

    
    create_Ergebnisdatei()#erstellen der Ergebnisdatei
    
    ergebnisdatei = open('ergebnis.txt','a')
    for i in range(anzahlSterne):
        #zufälliges Generieren der Variablen des Sterns
        posX = random.randint(0,1000)
        posY = random.randint(0,500)
        anzahlEcken = random.choice(eckenliste)
        radius = random.randint(10,30)
        
        pfad = drawStern(posX, posY, anzahlEcken, radius, pfadEnde)
        ergebnisdatei.write(f"<!--Stern {i+1}-->\n{pfad}\n\n")
    ergebnisdatei.close()


    
if __name__=="__main__":
    anzahlSterne = int(input("Wie viele Sterne sollen erzeugt werden? "))
    drawSterne(anzahlSterne)
    print("Sternenpfade wurden in der Datei ergebnis.txt gespeichert")
    
    
