#ESERCIZI SULLE FUNZIONI:
def rewrite_dict(d:dict[str, int]) -> dict[str ,int]:
    somma = sum(list(d.values()))
    print(f"la somma è {somma}")
    d1 = {}
    for k in d:
        d1[k] = d[k]/somma
    return d1
d ={"scarpe":10, "vestito":30 , "occhiali":20}
out = rewrite_dict(d)
print(out)
#esempio di funzine con i dizionari

#definisci una funzione substract che prende due parametri e poi ritorna il risultato

def substract(z:int , y:int):
    a:int = z-y
    return a
out = substract (8,4)
print(out)

#
def median(l:list[float]) -> float:
    l= sorted(l)#dopoaverdefinitolafunzioneho ordinato la lista
    mid = len(l) //2
    if len(l)%2!=0:#(ildispari)
        print("la mia lista ha lunghezza disapri")
        mediana = l[mid]
    else:#(il pari)
        print("la mia lista ha lungheza pari")
        mediana = (l[mid] + l[mid -1]) /2

    return mediana
l=[2,9,0,-2,25,2,4]
mediana = median(l)
print(f"la mediana della lista{l} è {mediana}")

#fare una funzione dove c'è  la differenza  cumulativa
def diff_cum(l:list[float]):
    x = l[0]
    for i in l[1:]:
        x = x-i
    return x
l=[1,2,3,4,5,6]
print(f'La differenza cumulativa è {diff_cum(l)}')

#come creare una funzione che sottrae tutti i numeri di una lista
def subtract_all(x: list[float], y: float) -> list[float]:
    res:list[float]=[]
    for elem in x:
        diff:float = elem -y
        res.append(diff)
    return res
res:list=[1,2,3,4,5]
y:float =10
result=subtract_all(res , y)
print(f"il risutato dopo la sottrazione è{result}")

#ESERCIZIO CON IL SET E I DIZIONARI:
s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
def counter(s:str) -> list[int]:
    """
    questa funzione prende una stringa in imput e restituisce una lista
    costruita nel modo  seguente:
    1)il primo elemento della lista contiene il numero di caratteri della stringa
    2)il secondo elemento della lista contiene il numero di parole nella stringa
    3)ilterzo elemento della lista contiene il numero di parole distinte nella lista
    4)il quarto elemento contiene il numero di frasi nella stringa
    """
    res :list[int]=[]
    #1
    res.append(len(s))
    #2
    res.append(len(s.split()))  # s ="ciao bello" -> ["ciao" , "bello"]
    #3
    parole= s.split() 
    parole_distinte = set(parole)
    res.append(len(s.split('.')) -1)

    return res


result = counter(s)#(chiamo la funzione)
print(f'Ecco il risultato {result}')

