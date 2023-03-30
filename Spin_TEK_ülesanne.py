
#Vajalik, et kasutada CSV moodulit
#Kasutame CSV faili kirjutamiseks
import csv
#Impordime "datetime" moodulist klassid "datetime" ja "timedelta"
#Vajalik kuup�evade aritmeetika tegemiseks
from datetime import datetime, timedelta

#Palga meeldetuletuse funktsioon, mis v�tab sisendiks aasta
def palgaMeeldetuletus(aasta):

    #M��rame p�had
    pyhad = [(aasta, 1, 1), (aasta, 2, 24), (aasta, 4, 7), (aasta, 4, 9), (aasta, 5, 1), (aasta, 5, 28), (aasta, 6, 23), (aasta, 6, 24), \
       (aasta, 8, 20), (aasta, 12, 24), (aasta, 12, 25), (aasta, 12, 26)]

    #Palgap�eva ja meeldetuletus p�eva arvutamine
    palgaP2evad = []
    meeldetuletusPaevad = []
    #Ts�kkel k�ib l�bi k�ik kuud
    for kuu in range(1, 13):

        #M��rame algse palgap�eva
        palgaPaev = datetime(aasta, kuu, 10)

        #Kontrollime, kas palgap�ev langeb n�dalavahetusele v�i p�hale
        #Ts�kkel k�ib nii kaua, kuni palgap�ev langeb t��p�evale
        while palgaPaev.weekday() >= 5 or (palgaPaev.year, palgaPaev.month, palgaPaev.day) in pyhad:
            #Kui langeb, siis v�hendame p�eva �he korra
            palgaPaev -= timedelta(days = 1)
        
        #M��rame algse meeldetuletus p�eva
        meeldetuletusPaev = palgaPaev
        #Muutuja, mis loeb, mitu korda meeldetuletus p�eva v�hendame �he korra kui meeldetuletus p�ev langeb t��p�eva peale
        counter = 0

        #Ts�kkel k�ib nii kaua, kuni meeldetuletus p�eva on v�hendatud kolm korda. Ei arvesta p�evade v�hendamist, kui p�ev
        # langeb n�dalavahetustele v�i p�hadele
        while counter < 3 or meeldetuletusPaev.weekday() >= 5:
            #Kontrollime, kas meeldetuletus p�ev langeb n�dalavahetusele v�i p�hale
            if meeldetuletusPaev.weekday() >= 5 or (meeldetuletusPaev.year, meeldetuletusPaev.month, meeldetuletusPaev.day) in pyhad:
                #Kui langeb, siis v�hendame p�eva �he korra
                meeldetuletusPaev -= timedelta(days = 1)
            else:
                #Kui langeb t��p�evale, siis v�hendame p�eva �he korra ja maksimaalselt kolm korda
                meeldetuletusPaev -= timedelta(days = 1)
                counter += 1

        #Lisame palgap�eva palgap�evade listi ja meeldetuletus p�eva meeldetuletus p�evade listi
        palgaP2evad.append(palgaPaev)
        meeldetuletusPaevad.append(meeldetuletusPaev)

    #Palgap�eva ja meeldetuletus p�ev kirjutatakse CSV faili
    #Avame CSV faili kirjutamise re�iimis
    with open(f'palgaMeeldetuletus_{aasta}.csv', 'w', newline = '') as csvFail:
        #M��rame veerude pealkirjad
        v2ljaNimed = ['Palgap2ev', ' Meeldetuletus kuup2ev']
        #Kirjutab andmed ridades vastavalt veergudele
        kirjutaja = csv.DictWriter(csvFail, fieldnames=v2ljaNimed)

        #Kirjutab veergude pealkirjad
        kirjutaja.writeheader()
        #Ts�kkel, mis kirjutab palgap�evad ja meeldetuletus p�evad CSV faili
        for palgaP2ev, meeldetuletusPaev in zip(palgaP2evad, meeldetuletusPaevad):
            kirjutaja.writerow({'Palgap2ev': palgaP2ev.strftime('%d-%m-%Y'), ' Meeldetuletus kuup2ev': meeldetuletusPaev.strftime('%d-%m-%Y')})

#K�sime kasutajalt sisendit ja konverteerime selle integeriks
while True:
        #K�sime kasutajalt sisendit
        aasta = input("Sisesta aasta: ")
        #Kontrollime, et stringi pikkus oleks 4 �hikut ja et sisend oleks numbrites
        if len(aasta) == 4 and aasta.isdigit():
            #Konverteerima muutuja aasta integeriks
            aasta = int(aasta)
            break
        else:
            #Vale sisendi korral annab rakendus kasutajale sellest teada
            print("Vale sisend. Sisestage aasta(YYYY): ")

#Kutsume v�lja palga meeldetuletuse funktsiooni
palgaMeeldetuletus(aasta)


