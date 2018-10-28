import sys

def H_P(ng,st,i,cycle):
	cycle+=[i]
	ele=[]
	for x in ng[i]:
		if x not in cycle:
			ele+=[x]
			
	if len(ele) == 0:
		if len(cycle) == len(ng):
			if st in ng[i]:
				print(cycle+[st])
			else:
				return	
		else:
			return
	else:
		for x in ele:
			H_P(ng,st,x,cycle)
			cycle.remove(x)					
def main():
	ng=[]
	n =int(input('Enter no of nodes:'))
	for x in range(n):
		ng+=[[int(x) for x in input('Enter the neighbours of  V'+str(x)+': ').split(',')]]
	print('\n~~~~~~~~~~The Hamiltonian Paths are~~~~~~~~~~~~')
	H_P(ng,0,0,[])
	
if __name__=='__main__':
	main()
