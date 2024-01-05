# Script di test Assegnamento 1py 622AA 2023/24 (non modificare)
from testMy import *
from stud import *

def controllo():
    #contiamo i test falliti
    testFalliti=0
    print("==========> Inizio nuovo test <=============\n\n")
    # creo un dizionario
    x = {}

    # test inserimento studente e serializza
    print("==========> Test 1")
    #
    # inserimenti corretti e sbagliati
    testFalliti += testEqual(inserisci(x, "Rossi", "Mario", 345655, []), True)
    testFalliti += testEqual(studente(x,345655)[1], "Mario")
    testFalliti += testEqual(inserisci(x, 12, "Rossi", 345655, []), False)
    testFalliti += testEqual(inserisci(x, "Lucato", "Giusi", 345665, [1, 2, 3]), False)
    testFalliti += testEqual(inserisci(x, "Lucato", "Giusi", -2, []), False)
    testFalliti += testEqual(inserisci(x, "Lucato", 13, 345611, []), False)
    testFalliti += testEqual(inserisci(x, "Lucato", "giusi", 345655, [(45, 46)]), False)
    print(x)
    print(serializza(x))
    testFalliti += testEqual(str(x), "{345655: ('Rossi', 'Mario', 345655, [], '')}")
    testFalliti += testEqual(inserisci(x, "Bianchi", "Luigi", 528611, [("544MM", 23)]), True)
    print(x)
    print(serializza(x))
    testFalliti += testEqual(inserisci(x, "Bilenchi", "Maria", 235655, [("655DD",30)]), True)
    testFalliti += testEqual(inserisci(x, "Neri", "Marcella Gianna", 237755, []), True)

    # test su registra_esame
    print("==========> Test 2")
    testFalliti += testEqual(registra_esame(x, 345655, "444GG", 27), True)
    testFalliti += testEqual(registra_esame(x, 345655, "564GG", 18), True)
    testFalliti += testEqual(registra_esame(x, 528611, "564GG", 21), True)
    testFalliti += testEqual(registra_esame(x, 444655, "564GG", 18), False)  # matricola non presente
    print(str(x))

# test su media
    print("==========> Test 3")
    testFalliti += testEqual(media(x, 111111), None)
    testFalliti += testEqual(media(x, 345655), 22.5)

#test su modifica voto
    print("==========> Test 4")
    testFalliti += testEqual(modifica_voto(x,345655, "444GG", 30),True)
    testFalliti += testEqual(modifica_voto(x,345655, "564GG", 20),True)
    testFalliti += testEqual(modifica_voto(x,345655, "456FF", 18),False) #matricola non presente
    print(str(x))
    testFalliti += testEqual(media(x,345655),25)

#test su conta studenti promossi
    print("==========> Test 5")
    testFalliti += testEqual(conta_studenti_promossi(x,"564GG"),2)
    testFalliti += testEqual(conta_studenti_promossi(x,"564GG",21),1)
    testFalliti += testEqual(conta_studenti_promossi(x,"564GG",25),0)

#test su lista studenti promossi
    print("==========> Test 6")
    testFalliti += testEqual(conta_studenti_promossi(x, "564GG"), len(lista_studenti_promossi(x, "564GG")))
    testFalliti += testEqual(conta_studenti_promossi(x, "564GG", 21),len(lista_studenti_promossi(x, "564GG", 21)))
    testFalliti += testEqual(studente(x, 345655)[1], "Mario")
    testFalliti += testEqual(conta_studenti_promossi(x, "564GG", 25), len(lista_studenti_promossi(x, "564GG", 25)))

# test su lista_media
    print("==========> Test 7")
    testFalliti += testEqual(len(lista_studenti_media(x)), 3)
    testFalliti += testEqual(len(lista_studenti_media(x,23)), 2)
    testFalliti += testEqual(studente(x, 345655)[1], "Mario")
    testFalliti += testEqual(len(lista_studenti_media(x, 26)), 1)

# test su cancella esame
    print("==========> Test 8")
    testFalliti += testEqual(cancella_esame(x,345655, "444GG"),True)
    testFalliti += testEqual(cancella_esame(x,345655, "564GG"),True)
    testFalliti += testEqual(cancella_esame(x,345655, "456FF"),False) #matricola non presente

#stampa finale archivio
    testFalliti += testEqual(x, {345655: ('Rossi', 'Mario', 345655, [], ''), 528611: ('Bianchi', 'Luigi', 528611, [('544MM', 23), ('564GG', 21)], ''), 235655: ('Bilenchi', 'Maria', 235655, [('655DD', 30)], ''), 237755: ('Neri', 'Marcella Gianna', 237755, [], '')})
    print("==========> Stampa finale archivio")
    print(serializza(x))

    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- effettuare la consegna come da README")
    else:
        print("Test falliti: ",testFalliti)


# eseguo i test automatici
controllo()