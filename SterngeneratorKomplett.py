import math

def draw_sterne(x, y, ecken, radius):
    ra = radius     #Radius des äußeren Kreises
    ri = radius*0.3 #Radius des inneren Kreises
    pi = 3.141
    alpha = 2*pi/ecken/2 #Kleinster Winkel

    a_x = 0         #aktuelles x
    a_y = 0         #aktuelles y
    a_alpha = alpha #aktueller Winkel

    #Erstellen des Pfades, wird im Laufe des Programms erweitert und am Schluss ausgegeben
    Pfad = "<path d=\"M " + str(x) + " " + str(y - ra) + " " #Cursor an Startposition bewegt

    #Pro Schleifendurchlauf wird String um 2 Punkte erweitert (innerer und äußerer Kreis)
    for i in range(ecken):
        
        #Berechnen des nächsten Punktes (innerer Ring)
        a_x = round(ri * math.sin(a_alpha) + x) 
        a_y = round(-ri * math.cos(a_alpha) + y)

        #Ergänzen des Pfades (Punkt am inneren Ring)
        Pfad = Pfad + "L " + str(a_x) + " " + str(a_y) + " "

        #Winkel eine Einheit weitersetzen
        a_alpha = a_alpha + alpha 
        
        #Berechnen des nächsten Punktes (äußerer Ring)
        a_x = round(ra * math.sin(a_alpha) + x)
        a_y = round(-ra * math.cos(a_alpha) + y)

        #Ergänzen des Pfades (Punkt am äußeren Ring)
        Pfad = Pfad + "L " + str(a_x) + " " + str(a_y) + " "

        #Winkel eine Einheit weitersetzen
        a_alpha = a_alpha + alpha

    #Abschließen der Pfadanweisung
    Pfad = Pfad + "z\" fill=\"yellow\"> <animateTransform attributeName=\"transform\" type=\"rotate\" from=\"0 " + str(x) + " " + str(y) + "\" to=\"360 " + str(x) + " " + str(y) + "\" dur=\"4s\" repeatCount=\"indefinite\"/> </path>"

    #Pfad-String wird ausgegeben
    print(Pfad)


#Ein Aufruf der Funktion -> Stern an Punkt (200,200) mit 5 Ecken und Radius 100
draw_sterne(200, 200, 5, 100)
