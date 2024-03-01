# Da completare con il codice

""""
Corrado Baccheschi
Matricola: 599107
Email: c.baccheschi@studenti.unipi.it

"""

##### Questa personalizzata per "alleggerire" le funzioni registra e modifica --- DRY
### Verifica che il voto sia un intero positivo tra 18 e 33
def checkvoto(num):
     if type(num)!=int or num <= 0 or num >= 33 or num < 18:
        print("Il voto inserito non è corretto. Assicurarsi che", num, " sia un numero compreso tra 18 e 33") 
        return False
     else:
        return True
     
### Questa anche personalizzata per controllare i parametri e "alleggerire" la funzione inserisci
### Verifica che stud sia un dizionario, nome e cognome stringhe, la matricola un intero positivo, la listaesami una lista e le note una stringa
def checkparams(stud, nome, cognome, matricola, listaesami, note):
    if (type(stud) is not dict or type(nome) != str or type(cognome) != str or type(matricola) != int or matricola <= 0 or type(listaesami) != list or type(note) != str):
            print("I parametri inseriti non sono corretti, verificarli")
            return False
    return True


def inserisci(stud, cognome, nome, matricola, listaesami, note=""):
    if(checkparams(stud, nome, cognome, matricola, listaesami, note)):  ## Se i parametri sono corretti

        for esame in listaesami:  # per ogni esame nella lista esami [(ESAME),..]
            if not (   # se le successive condizioni NON sono tutte vere
                type(esame) == tuple and   # se l'esame NON è una tupla non vuota con 2 valori (x string, y num)
                len(esame) == 2 and
                type(esame[0]) == str and
                esame[0] != "" and   
                checkvoto(esame[1])  # e se l'esame NON passa il controllo della funzione checkvoto
            ):
                return False   # se le precedenti non sono soddisfatte "not" interrompo e torno false
    else:
        print("Inserimento fallito")
        return False  # i parametri non sono corretti, interrompo e false
    if note == "":  # se le note sono vuote
        studente = (cognome, nome, matricola, listaesami, "") # di default è "" questo per evitare problemi successivi 
    else:
        studente = (cognome, nome, matricola, listaesami, note)

    stud[matricola] = studente   # aggiungo la tupla al dizionario
    return True


def serializza (stud):
    riga = ""
    for tupla in stud.values():    # scorro le tuple nel dizionario (cognome, nome, matricola, listaesami)
        cognome = tupla[0]
        nome = tupla[1]
        matricola = tupla[2]
        listaesami = tupla[3]

        note = tupla[4] if len(tupla) > 4 else ""   # se ci sono note esiste anche il quarto elemento della tupla, altrimenti non eseguire assegnamento per evitare index out of range

        if(listaesami=="" or listaesami==[]):  # se la lista è vuota 
            listaesami="no" #
        if(note==""):
            note="no"

        stringa = cognome + " " + nome + " mat: " + str(matricola) + " esami: " + str(listaesami) + " note: " + note # note e listaesami dipendono dalle condizioni successive, ci sono oppure "no"
        
        riga =  riga + stringa + "\n"  # accumulo righe con la stringa

    return riga


def studente(stud,matricola):
    if(matricola in stud.keys()): # se la matricola è presente nelle chiavi del dizionario
        t= stud[matricola] # ottengo la tupla
        return t
    else:
        print("Ricerca dello studente fallita: la matricola ", matricola, " inserita non esiste")
        return None


def registra_esame(stud,matricola,codice,voto):

    tupla = studente(stud, matricola) # ottengo lo studente
    if(tupla is not None): # se non torna None ma una tupla lo studente esiste
        if(checkvoto(voto)):  ## Controllo il voto con la funzione personalizzata
            if(codice!=""): ##Controllo sul codice
                stud[matricola][3].append((codice, voto))  # Nuova tupla con l'esame registrato per la matricola scelta
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def media(stud, matricola):    
    tupla = studente(stud, matricola) # come sopra
    if(tupla is not None):
        somma = 0  # Inizializzo la somma a 0 ed anche l'indice i
        i =  0
        listaesami = tupla[3]  
        for codice, voto in listaesami:  # scorro la lista di tuple [(codice, voto)i, (codice, voto)i...i a n]
            somma += voto  # accumulo una somma sui voti presi
            i += 1
            f = float(somma/i)   # che divido per il numero di esami (i= scorrimenti del for)
        return f
    else:
        return None


def modifica_voto(stud,matricola,codice,voto):
    tupla = studente(stud, matricola) # come sopra ^
    if(tupla is not None):
        listaesami = tupla[3]
        if(checkvoto(voto)):
            for i in range(len(listaesami)): # scorro da i a n = lunghezza di listaesami
                cod = listaesami[i][0]  # primo elemento della tupla i nella lista [(CODICE, voto)i...n], quindi il codice
                if(cod == codice):   # se nella lista degli esami trova il codice
                    stud[matricola][3][i] = (codice, voto) # aggiorna la tupla corrispondente con il nuovo voto
                    return True
            return False
        else:
            return False
    else:
        return False


def cancella_esame(stud,matricola,codice):
    tupla = studente(stud, matricola) # come sopra ^
    if(tupla is not None):
        listaesami = tupla[3]
        for i in range(len(listaesami)):
            esame = listaesami[i]  # elementoi della lista, (codice, voto)i...n
            if(esame and esame[0] == codice):   # se tupla non vuota e trova il codice
                del stud[matricola][3][i] # aggiorna la tupla corrispondente cancellando esame
            return True
        return False
    else:
        return False
    

def lista_studenti_promossi(stud, codice, soglia=18):
    listapromossi = []  # inizializzo la lista dei promossi 
    for studente in stud.values(): # per ogni valore del dizionario 
        for esame in studente[3]:  # scorro internamente anche ogni singolo esame (scorro le tuple di listastudenti)
            if esame[0] == codice and esame[1] >= soglia:  # quindi ho adesso (codice, voto) e controllo che il codice sia corretto e che il voto superi una soglia
                listapromossi.append((studente[0], studente[1], studente[2])) # appendo la tupla (cognome, nome, matricola) alla lista dei promossi

    return listapromossi

def conta_studenti_promossi(stud, codice, soglia=18):
          
        return len(lista_studenti_promossi(stud, codice, soglia))

def lista_studenti_media (stud, soglia=18):
        listasuff = [] # lista vuota dei sufficienti
        for matricola, studente in stud.items():
            if studente[3]!=[] and studente[3]!="":
                avg = media(stud, matricola)  #funzione media definita precedentemente
                if avg>=soglia:  # se la media è maggiore od uguale della soglia
                    listasuff.append((matricola, studente[0], studente[1], avg)) #appendo matricola, cognome, nome e anche la media
        return listasuff







