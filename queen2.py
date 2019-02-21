def sucessora(vectorTeste):
	for i in range(8):                       
			for j in range(8):
				if i!= j:                               #Compares one spot in the Vector with all the others spots, besides himself

					if vectorTeste[j]==vectorTeste[i]:
						vectorTeste[0]+=1
						return vectorTeste
					if j > i : 							#Second line of conditional : Diagonal
					

						if vectorTeste[j] - vectorTeste[i] == j - i or vectorTeste[j] - vectorTeste[i] == ( j - i )*-1 :       
							vectorTeste[0]+=1
							return vectorTeste
					if i > j : 							#Third line of conditional : Diagonal
					

						if vectorTeste[i] - vectorTeste[j] == i - j or vectorTeste[i] - vectorTeste[j] == ( i - j )*-1 :       
							vectorTeste[0]+=1
							return vectorTeste		
	print(vectorTeste)						
	vectorTeste[0]+=1
	return vectorTeste


vector = [0,0,0,0,0,0,0,0]
while vector[7] != 8:
	vector = sucessora(vector)
	if vector[0]==8:
		vector[1]+=1
		vector[0]=0
	
	if vector[1]==8:
		vector[2]+=1
		vector[1]=0
	
	if vector[2]==8:
		vector[3]+=1
		vector[2]=0
	
	if vector[3]==8:
		vector[4]+=1
		vector[3]=0
	
	if vector[4]==8:
		vector[5]+=1
		vector[4]=0
	
	if vector[5]==8:
		vector[6]+=1
		vector[5]=0
	
	if vector[6]==8:
		vector[7]+=1
		vector[6]=0
