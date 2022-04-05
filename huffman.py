
class ArbreBinaire:
    def __init__(self, r,g=None,d=None):
        self.r = r
        self.gauche = g
        self.droit = d

    def __str__(self):
    	return f"r: {self.r}  gauche: {self.gauche}  droite: {self.droit} "

def coder(dico, mess):
    messCode =""
    
    for letter in mess:
        messCode+= dico[letter]
       
  
    return messCode

def compteLettre(message):
    dic = {}
    for lettre in message:
        try:
            
            dic[lettre]+=1
        except KeyError:
            dic[lettre] = 1
    return dic

def decode(dico,messCode):
    streak = ""
    mot = ""
    trueDic = {}
    for key in dico:
        trueDic[dico[key]]=key
    for digit in messCode:
        streak+=digit
        try:
            mot +=trueDic[streak]
            streak = ""
        except KeyError:
            continue
        
    return mot
def triDic(dic):
	finalDic = {}
	for w in sorted(dic, key=dic.get, reverse=True):
   	    finalDic[w]=dic[w]    
	return finalDic
def deuxMinTuple(List):
	min1 = List[0]
	min2 = List[1]

	if min2[1]<min1[1]:
		min2,min1 = min1,min2
	
	for item in List:
		
		if item[1]<min2[1]:
			if item[1]<min1[1]:
				min1 = item
				continue
			min2 = item
	return min1,min2




def messToDico(mess):
    finalDic = triDic(compteLettre(mess))
    print(finalDic)
    l = [(c,finalDic[c]) for c in finalDic]
    print(l)
    print("les min sont", deuxMinTuple(l))
    while len(finalDic)>1:
    	

    	a=ArbreBinaire(finalDic[list(finalDic.keys())[-1]]+finalDic[list(finalDic.keys())[-2]],finalDic.pop(list(finalDic.keys())[-2]),finalDic.pop(list(finalDic.keys())[-1]))
    	l.pop



    print(l)
    print(finalDic)
