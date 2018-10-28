import sys

#dict Col={}

def G_C(n,cc,cl,lst,node):
	#print('\n\nG_C')
	c=[1 for x in range(cc)]
	
	if node!=len(n):
		for x in n[node]:		#discard all colours that the neighbours are using
			if lst[x] != -1:
				c[lst[x]]=0
		
	#	print('lst,c: ',lst,c)
		
		for i in range(cc):		#use the remaining colours
			if c[i]==1:
				lst[node]=i
				
				G_C(n,cc,cl,lst,node+1)
				
				lst[node]=-1
	else:
		print([cl[x] for x in lst])						
	

def main():
	neigh=[]
	n = int(input('Enter the no of nodes:'))	
	for i in range(n):
		neigh+=[[int(x) for x in input('Enter neighbours of node (itself if no neighbour) '+str(i)+': ').split(',')]]
	print(neigh)
	colours=input('Enter the list of colours:').split(',')
		
	print('~~~~~~~~~~THE GRAPH COLOURING PATTERNS~~~~~~~~~~~~')
	G_C(neigh,len(colours),colours,[-1 for x in range(n)],0)

if __name__ == '__main__':
	main()
