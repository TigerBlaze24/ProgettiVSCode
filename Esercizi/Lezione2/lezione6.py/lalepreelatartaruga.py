import random
def visualizza_posizioni(pos_tartaruga:str, pos_lepre:str) ->int:   
    corsa_animali :list = []
    for i in range (71):    
        corsa_animali.append("_")
    print(corsa_animali)
def movimento_tartaruga(passo_veloce,scivolata,passo_lento)->int:
    i = random.randint(0,10)
    if i in range (1,5):
        mossa = 3 
        return mossa
    if i in range (6,7):
      mossa = -6
      return mossa
    if i in range(8,9,10):
        mossa = 1 
        return mossa
def movimento_lepre(riposo,grande_balzo,grande_scivolata,piccolo_balzo,piccola_scivolata)->int:
    i = random.randint(0,10)
    if i in range(1,2):
        mossa = 0
    if i in range(1,2):
        mossa = 9
    if i in range (1,1):    
        mossa = -12
    if i in range (1,3):
        mossa = 1
    if i in range(1,2): 
        mossa = -2
print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
tartaruga = 1
tartaruga = movimento_tartaruga()   
lepre = 1
lepre = movimento_lepre()




    
