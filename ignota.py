import sys
import itertools

places_ocupades = []
numero_nodes = 0
numero_arestes = 0
nodes = []
inversa = []
cicles = []
totes_combinacions = []

def main ():	#Main
	places_ocupades, numero_nodes, numero_arestes, nodes = tractament_parametres()
	#print places_ocupades
	#print nodes
	inversa = generar_nodes_no_amics(places_ocupades,numero_nodes)
	totes_combinacions = obtenir_totes_combinacions(nodes)
	#print totes_combinacions
	cicles = buscar_cicles(inversa,totes_combinacions)
	final = max(cicles, key=len)
	for t in final:
		print t,

def tractament_parametres():
	if(len(sys.argv) != 2): # En cas de no haber parametres d'entrada
		print "[Info] Us: python iteratiu.py [fitxer-nodes]"
		try:
			llegir_entrada_standard()
			parametres = False
			places_ocupades, numero_nodes, numero_arestes = llegir_fitxer(parametres)
			return places_ocupades, numero_nodes, numero_arestes
		except IndexError:
			print "[Error] Format de dades incorrecte."
	else: #En cas d'haber parametres d'entrada
		try:
			parametres = True
			places_ocupades, numero_nodes, numero_arestes, nodes = llegir_fitxer(parametres)
			return places_ocupades, numero_nodes, numero_arestes, nodes
		except IOError:
			print "[Error] No s'ha pogut trobar el fitxer especificat."
			# Tractament d'error en cas de fitxer inexistent.

def llegir_entrada_standard():
	new_nodes = open("landings.txt", 'w') # No parametre -> arxiu per defecte.
	print "[Info] Introdueix una llista amb format: 'p' 'edge' 'numero de nodes' 'numero darestes'"
	print "[Info] A continuacio: 'e' 'node' 'node al que anira conectat'"
	print "[Info] Per acabar, prem [Enter] en una linea en blanc."
	acabat = False
	while (acabat != True): #Anar llegint i escribint d'entrada standard.
		llista = raw_input()
		if(llista == ""):
			acabat = True
		else:
			new_nodes.write(llista + "\n")

def llegir_fitxer(parametres):
	if(parametres == True): # En cas d'haber parametre d'entrada usara aquest.
		fitxer = sys.argv[1]
	else:					# En cas contrari en creem un i l'utilitzem.
		fitxer = 'landings.txt'
	nodes = open(fitxer,'r')
	for linea in nodes:			# Llegir totes les linees i tractarles.
		splited = linea.split( )
 		if(splited[0]=='p'):
			numero_nodes = int(splited[2])
			numero_arestes = int(splited[3])
		else:
			places_ocupades.append((int(splited[1]),int(splited[2])))
	nodes.close()
	nodes = list(range(1,numero_nodes+1))
	return places_ocupades, numero_nodes, numero_arestes, nodes

def generar_nodes_no_amics(places_ocupades,numero_nodes):
	inversa1 = []
	inversa2 = []
	for i in range(1,numero_nodes):
		for j in range(2,numero_nodes+1):
			if(i!=j):
				inversa1 = (i,j)
				inversa2 = (j,i)
				if inversa1 not in places_ocupades and inversa2 not in places_ocupades and inversa2 not in inversa:
					inversa.append(inversa1)
	#print inversa
	return inversa

def obtenir_totes_combinacions(nodes):
	temporal = []
	for L in range(0,len(nodes)+1):
		for subset in itertools.combinations(nodes,L):
			temporal.append(subset)
	return temporal

def buscar_cicles(inversa,totes_combinacions):
	temporal = []
	bones = []
	trobat = True
	for combinacio in totes_combinacions:
		if len(combinacio)>=1:
			trobat = True
			for x in range(len(combinacio)):
				for y in range(x+1,len(combinacio)):
					temporal = (combinacio[x],combinacio[y])
					if temporal not in inversa:
						trobat = False
						break
			if trobat == True:
				bones.append(combinacio)
	return bones

if __name__ == "__main__":		#Anem al main
	main();
