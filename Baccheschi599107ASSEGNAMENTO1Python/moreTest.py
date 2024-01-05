from stud import *   # Funzioni necessarie da stud.py
from testMy import *   # Funzione di test

testFalliti=0

## Checkvoto
print("-----------------test checkvoto----------------")
testFalliti += testEqual((checkvoto(18)), True)
testFalliti += testEqual((checkvoto(22)), True)
testFalliti += testEqual((checkvoto(33)), False)
testFalliti += testEqual((checkvoto("r")), False) 
testFalliti += testEqual((checkvoto(str(18))), False)
testFalliti += testEqual((checkvoto(str(16))), False)
testFalliti += testEqual((checkvoto(12)), False)

x= {}
y = []

## Checkparams
print("-----------------test checkparams------------------")
testFalliti += testEqual((checkparams(x, 21, "Rossi", 599107, [], "note")), False)
testFalliti += testEqual((checkparams(y, 21, "Rossi", 599107, [], "note")), False)
testFalliti += testEqual((checkparams(x, "Mario", "Rossi", 599107, [], "note")), True)
testFalliti += testEqual((checkparams(y, "Mario", "Rossi", 599107, {}, "note")), False)
testFalliti += testEqual((checkparams(x, "Mario", "Rossi", 1, [], "note")), True)
testFalliti += testEqual((checkparams(x, "Mario", "Rossi", 0, [], "note")), False)


print("---------END-------------")


 # abbiamo finito ?
if testFalliti == 0:
    print("\t****Test completati -- passare ai test in main.py")
else:
    print("Test falliti: ",testFalliti)


"""" more test
x = {}

print(inserisci(x, "Lucato", 13, 345611, []))
print(inserisci(x, "Rossi", "Mario", 1, [("235AF", 22)], "Note"))
print(inserisci(x, "Rossi", "Mario", 1862705, [("235AF", 0)], "Note"))
print(inserisci(x, "Rossi", "Mario", 1862705, [("235AF", 50)], "Note"))
print(inserisci(x, "Rossi", "Mario", 1862705, [("", 22)], "Note"))
print(inserisci(x, "Rossi", "Mario", 0, [("235AF", 22)], "Note"))
print(inserisci(x, "Rossi", "Antonio", -2, [("235AF", 22)], "Note"))
print(inserisci(x, "Rossi", "Mario", 1862705, [(0, 22)]))
print(inserisci(x, "Rossi", "Mario", 1862705, [("235AF", 13)], "Note"))
print(inserisci(x, "Rossi", "Mario", 1862707, [("235AF", 18)]))
print(inserisci(x, "Rossi", "Mario", 1862706, [("235AF", 33)]))
print(inserisci(x, "Rossi", "Mario", 1862705, [("ADCFMM")]))


print(x)


## Serializza

print("Serializza..")

dicti = {
    345655: ('Mario', 'Rossi', 345655, [("544ML", 20)], ''),
    528611: ('Bianchi', 'Luigi', 528611, [('544MM', 23)], ''),
    345656: ('Mario', 'Rossi', 345656, [('SDF53', 26)], ''),
    528612: ('Bianchi', 'Luigi', 528612, [('544MM', 33)], 'note'),
    528613: ('Bianchi', 'Mario', 528613, [('544MM', 17), ('AC67MM', 18)], 'note'),
    565435: ('Bianchi', 'Giordano', 565435, [], 'note')
}

outputser = serializza(dicti)
print(outputser)


## Cerca studente
print("Cerca studente..")
print(studente(dicti,345656))
print(studente(dicti,345655))
print(studente(dicti,3455))


## Inserisci voto
print("Registra esame..")
print(registra_esame(dicti,528611, 's4fe2', 34))
print(registra_esame(dicti,528611, 's4fe2', 30)) #
print(registra_esame(dicti,528611, '', 18))
print(registra_esame(dicti,528612, 'XABML', 18))
print(registra_esame(dicti,528613, '', 18))
print(registra_esame(dicti,345656, 'ACV45', 18))
print(registra_esame(dicti,345656, 'ACV45', 16))

print(dicti)  


## Calcola media
print("Calcola media..")
print(media(dicti, 528611))
print(media(dicti, 528611))


## Aggiorna voto
print("Aggiorna voto..")
print(modifica_voto(dicti,345656,'SDF53',30))
print(modifica_voto(dicti,345678,'SDF53',30))
print(modifica_voto(dicti,345656,'SDF53',16))
print(modifica_voto(dicti,345656,'SDF51',30))
print(dicti)

x = {
    345655: ('Bianchi', 'Luigi', 345655, [('444GG', 23), ('564GG', 26), ('454FF', 29)], '')
}

## Elimina voto
print("Elimina esame..")
print(x)
print(serializza(x))
print(cancella_esame(x,345655, "444GG"))
print(x)
print(serializza(x))
print(cancella_esame(x,345655, "564GG"))
print(x)
print(serializza(x))
"""