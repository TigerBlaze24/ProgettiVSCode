def construct_rectangle(area: float) -> list[float]:
    min_diff = float('inf')
    result = [1, area]
    
    for i in range(1, int(area**0.5) + 1):
        if area % i == 0:
            if area // i - i < min_diff:
                min_diff = area // i - i
                result = [area // i, i]
    
    return result

#esrcizio stop word(della verifica 4 in classe)
import re
from collections import Counter
def wod_frequenty(text:str,stopwords:list[str]) -> dict[str,int]:
    text = re.sub(r'[^\w\s]','' , text.lower())
    words= list()
    for word in text.split():
        if word not in stopwords:
            words.append(word)
    result = Counter(words)
    
    return dict(result)

#esrcizio gioielli verifica
def thirs_max(gems:list[int]) -> int:
    gems = sorted(list(set(gems)), reversed = True)
    if len(gems) >= 3:
        return gems[2]
    else:
        return gems[0]
    #