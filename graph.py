class Graphe: 

	def __init__(self,n):
		self.n=n
		self.adj=[[0]*n for i in range(n)]

	def afficher(self):
		for s in range(self.n):
			print(s,"-->",end="")
			for v in range(self.n):
				if self.adj[s][v] == 1:
					print("",v,end="")
			print()

	def ajouterArc(self,s1,s2):
		 self.adj[s1][s2]=1
		 """self.adj[s2][s1]=1"""

	def arc(self,s1,s2):
		return self.adj[s1][s2]

	def successeur(self,s):
		v=[]
		for i in range(self,n):
			if self.adj[s][i]==1:
				v.append(i)
		return v 

	def degreSortant(self,p1):
		tot = 0
		for i in range(len(self.adj)):
			if self.arc(p1,i) == 1:
				tot+=1
		return tot

	def nbarc(self):
		tot = 0
		for i in range(len(self.adj)):
			tot += self.adj[i].count(1)

		return tot
	def supprimerArc(self,s1,s2):
		try:
			self.adj[s1][s2] = 0
			
		except IndexError:
			print(f"L'arc allant de {s1} à {s2} n'existe pas")


G = Graphe(4)
G.ajouterArc(0,1)
G.ajouterArc(0,3)
G.ajouterArc(3,1)
G.ajouterArc(1,2)
G.afficher()

class Gr:

	def __init__(self):
		self.adj = {}

	def _afficher(self):
		for s in self.adj:
			if len(self.adj[s]) == 0:
				print(s, "{}")
			else: 
				print(s, self.adj[s])
	def ajouter_sommet(self,s):
		if s not in self.adj:
			self.adj[s]= []

	def ajouter_arc(self,s1,s2):
		self.ajouter_sommet(s1)
		self.ajouter_sommet(s2)
		self.adj[s1].append(s2)

		"""version nn orienté
		self.adj[s1].append(s2)
		self.adj[s2].append(s1)"""
	def arc(self,s1,s2):
		return s2 in self.adj[s1]

	def sommets(self):
		return list(self.adj)

	def successeur2(self,s):
		return self.adj[s]

	def nb_sommets(self):
		return len(list(self.adj))

	def degre_sortant(self, s):
		return len(self.adj[s])

	def nbarc(self):
		tot = 0
		for key in self.adj:
			tot += len(self.adj[key])
		return tot

	def supprimer_arc(self, s1,s2):
		try:
			self.adj[s1].remove(s2)
		except ValueError:
			print(f"L'arc allant de {s1} à {s2} n'existe pas")
Gr2 = Gr()
Gr2.ajouter_arc(0,1)
Gr2.ajouter_arc(0,3)
Gr2.ajouter_arc(1,2)
Gr2.ajouter_arc(3,1)
print()
Gr2._afficher()
print(Gr2.sommets())
print(Gr2.arc(0,1))
print(Gr2.successeur2(0))
print(Gr2.nb_sommets())
print(Gr2.degre_sortant(0))
print(Gr2.nbarc())
Gr2.supprimer_arc(0,1)
Gr2.ajouter_arc(2,3)
Gr2.ajouter_arc(2,0)
Gr2._afficher()




def deepFirstSearch(graph,node,visité=set()):
	
	if node not in visité:
		print(node)
		visité.add(node)
		for n in graph[node]:
			deepFirstSearch(graph,n,visité)

def breadthfirstsearch(graphe,node):
	visité = []
	file = []
	visité.append(node)
	file.append(node)
	while file:
		stack = file.pop(0)
		print(stack, end=" ")

		for voisin in graphe[stack]:
			if voisin not in visité:
				visité.append(voisin)
				file.append(voisin)

print('------------------')

breadthfirstsearch(Gr2.adj,0)
print('\n------------------')


Gr3 = Gr()
Gr3.ajouter_arc(5,3)
Gr3.ajouter_arc(5,7)
Gr3.ajouter_arc(3,2)
Gr3.ajouter_arc(3,4)
Gr3.ajouter_arc(7,8)
Gr3.ajouter_arc(4,8)
Gr3._afficher()
breadthfirstsearch(Gr3.adj,5)
