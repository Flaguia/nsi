""" p et q > Premier
	
	n = pq
	f = (p-1)(q-1)
	e = premier<f
	(e,n) = clé publique

	p = 6991 
	q= 7529
	n = pq = 6991*7529 = 52 635 239
	f = 52 620 720


	chiffrage:
		écrire en nombre entier naturel  m (ASCII)
		si m<n:
			reste de (m**e)%n
		sinon:
		découpée le message en sous message jusqu'à
		m<n possible avec m premier avec n (algo d'euclide)

	déchiffrage: avec cle (d,n)
		d avec d<n tel que
		(e*d)%f=1

		mess = c**d%n
		 """
def Rsa(chara, e, n):
	"""first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,31, 37, 41, 43, 47, 53, 59, 61, 67,  
                     71, 73, 79, 83, 89, 97, 101, 103,  
                     107, 109, 113, 127, 131, 137, 139,  
                     149, 151, 157, 163, 167, 173, 179,  
                     181, 191, 193, 197, 199, 211, 223, 
                     227, 229, 233, 239, 241, 251, 257, 
                     263, 269, 271, 277, 281, 283, 293, 
                     307, 311, 313, 317, 331, 337, 347, 349] """
	chifrage = ""
	for lettre in chara:
		chifrage += str(ord(lettre))
	chifrage = int(chifrage)
	return (chifrage**e)%n

def Trouverd(e,f):
	first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,31, 37, 41, 43, 47, 53, 59, 61, 67,  
                     71, 73, 79, 83, 89, 97, 101, 103,  
                     107, 109, 113, 127, 131, 137, 139,  
                     149, 151, 157, 163, 167, 173, 179,  
                     181, 191, 193, 197, 199, 211, 223, 
                     227, 229, 233, 239, 241, 251, 257, 
                     263, 269, 271, 277, 281, 283, 293, 
                     307, 311, 313, 317, 331, 337, 347, 349]
	p = 0
	q = 1
	for i in range(f):
		
		if (first_primes_list[p]-1)*(first_primes_list[q]-1) == f:
 			break
		p += 1
		q += 1
	n = first_primes_list[p]*first_primes_list[q]
	for d in range(n):
		
		if (e*d)%f==1:
			return d



def Dechiffre(c,d,n):
	variable = 1
	for i in range(d):
		print("variable",variable)
		print("c",c)
		print("n",n)
		print("v*c = ",variable*c)
		print("v*c%n = ",(variable*c)%n)
		
		variable = (variable*c)%n
		print("var",variable)
		
	print(variable)

	
	

#mot de base, e, n
print("yes",Rsa("RSA", 23,77))
#e, f

mot = Rsa("RSA", 23,77)

Dechiffre(mot,Trouverd(23,24) ,77)
#mot chiffrer, d, n
""" p et q > Premier
	
	n = pq
	f = (p-1)(q-1)
	e = premier<f
	(e,n) = clé publique

	déchiffrage: avec cle (d,n)
		d avec d<n tel que
		(e*d)%f=1

		mess = c**d%n"""