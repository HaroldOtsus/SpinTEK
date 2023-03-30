
#Vajalik, et kasutada CSV moodulit
#Kasutame CSV faili kirjutamiseks
import csv
#Impordime "datetime" moodulist klassid "datetime" ja "timedelta"
#Vajalik kuupäevade aritmeetika tegemiseks
from datetime import datetime, timedelta

#Palga meeldetuletuse funktsioon, mis võtab sisendiks aasta
def palgaMeeldetuletus(aasta):

    #Määrame pühad
    pyhad = [(aasta, 1, 1), (aasta, 2, 24), (aasta, 4, 7), (aasta, 4, 9), (aasta, 5, 1), (aasta, 5, 28), (aasta, 6, 23), (aasta, 6, 24), \
       (aasta, 8, 20), (aasta, 12, 24), (aasta, 12, 25), (aasta, 12, 26)]

    #Palgapäeva ja meeldetuletus päeva arvutamine
    palgaP2evad = []
    meeldetuletusPaevad = []
    #Tsükkel käib läbi kõik kuud
    for kuu in range(1, 13):

        #Määrame algse palgapäeva
        palgaPaev = datetime(aasta, kuu, 10)

        #Kontrollime, kas palgapäev langeb nädalavahetusele või pühale
        #Tsükkel käib nii kaua, kuni palgapäev langeb tööpäevale
        while palgaPaev.weekday() >= 5 or (palgaPaev.year, palgaPaev.month, palgaPaev.day) in pyhad:
            #Kui langeb, siis vähendame päeva ühe korra
            palgaPaev -= timedelta(days = 1)
        
        #Määrame algse meeldetuletus päeva
        meeldetuletusPaev = palgaPaev
        #Muutuja, mis loeb, mitu korda meeldetuletus päeva vähendame ühe korra kui meeldetuletus päev langeb tööpäeva peale
        counter = 0

        #Tsükkel käib nii kaua, kuni meeldetuletus päeva on vähendatud kolm korda. Ei arvesta päevade vähendamist, kui päev
        # langeb nädalavahetustele või pühadele
        while counter < 3 or meeldetuletusPaev.weekday() >= 5:
            #Kontrollime, kas meeldetuletus päev langeb nädalavahetusele või pühale
            if meeldetuletusPaev.weekday() >= 5 or (meeldetuletusPaev.year, meeldetuletusPaev.month, meeldetuletusPaev.day) in pyhad:
                #Kui langeb, siis vähendame päeva ühe korra
                meeldetuletusPaev -= timedelta(days = 1)
            else:
                #Kui langeb tööpäevale, siis vähendame päeva ühe korra ja maksimaalselt kolm korda
                meeldetuletusPaev -= timedelta(days = 1)
                counter += 1

        #Lisame palgapäeva palgapäevade listi ja meeldetuletus päeva meeldetuletus päevade listi
        palgaP2evad.append(palgaPaev)
        meeldetuletusPaevad.append(meeldetuletusPaev)

    #Palgapäeva ja meeldetuletus päev kirjutatakse CSV faili
    #Avame CSV faili kirjutamise režiimis
    with open(f'palgaMeeldetuletus_{aasta}.csv', 'w', newline = '') as csvFail:
        #Määrame veerude pealkirjad
        v2ljaNimed = ['Palgap2ev', ' Meeldetuletus kuup2ev']
        #Kirjutab andmed ridades vastavalt veergudele
        kirjutaja = csv.DictWriter(csvFail, fieldnames=v2ljaNimed)

        #Kirjutab veergude pealkirjad
        kirjutaja.writeheader()
        #Tsükkel, mis kirjutab palgapäevad ja meeldetuletus päevad CSV faili
        for palgaP2ev, meeldetuletusPaev in zip(palgaP2evad, meeldetuletusPaevad):
            kirjutaja.writerow({'Palgap2ev': palgaP2ev.strftime('%d-%m-%Y'), ' Meeldetuletus kuup2ev': meeldetuletusPaev.strftime('%d-%m-%Y')})

#Küsime kasutajalt sisendit ja konverteerime selle integeriks
while True:
        #Küsime kasutajalt sisendit
        aasta = input("Sisesta aasta: ")
        #Kontrollime, et stringi pikkus oleks 4 ühikut ja et sisend oleks numbrites
        if len(aasta) == 4 and aasta.isdigit():
            #Konverteerima muutuja aasta integeriks
            aasta = int(aasta)
            break
        else:
            #Vale sisendi korral annab rakendus kasutajale sellest teada
            print("Vale sisend. Sisestage aasta(YYYY): ")

#Kutsume välja palga meeldetuletuse funktsiooni
palgaMeeldetuletus(aasta)


