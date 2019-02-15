copy_list = lambda list: list[:]
import itertools

def permutation(lst):  
    if len(lst) == 0: 
        return []  
    if len(lst) == 1: 
        return [lst]
  
    l = []  
 
    for i in range(len(lst)): 
       m = lst[i] 


       remLst = lst[:i] + lst[i+1:] 
   
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
     
def sucessora(p):
		for i in range(8):                       #Compares one spot in the Vector with all the others spots, besides himself
				for j in range(8):
						if j > i :
							if p[j] - p[i] == j - i or p[j] - p[i] == ( j - i )*-1 :       #Second line of conditional : Diagonal
								return True
							if i > j :
								if p[i] - p[j] == i - j or p[i] - p[j] == ( i - j )*-1 :       #Third line of conditional : Diagonal
									return True
								
		return p

deuBom = 0
deuRuim = 1
data = list([0,1,2,3,4,5,6,7]) 
for p in permutation(data): 
    if sucessora(p) != True:
    	print(p)









    	#oi gente
