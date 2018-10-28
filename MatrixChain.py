import sys


def generate_seq(B,lst1,f,l):
	lst=[]
	if l > f:
		b=B[f][l]
		lst+= [generate_seq(B,lst1[f:b],f,b-1)]
		lst+= [generate_seq(B,lst1[b:l+1],b,l)]
		return lst
	else:
		lst+= ['M'+str(f)]		
		return lst


def mat_chain(dim):
	k=1
	n=len(dim)
	M=[[0 for i in range(0,n)] for j in range(0,n)] 	
	B=[[0 for i in range(0,n)] for j in range(0,n)] 	

	
	while(k<n):
		j=k;
		for i in range(0,n):
			if j==n:
				break
			pos=0
			for x in range(i,j):
				m=M[i][x]+M[x+1][j]+dim[i][0]*dim[x][1]*dim[j][1]
				if pos==0:
					min=m
					pos=x+1
				elif min > m:
					min=m
					pos=x+1
					
			M[i][j]=min	
			B[i][j]=pos		
			j+=1	
		k+=1	
	
	print('\nMemoised Results:\n')
	
	for x in M:
		print(x)
	print('\n\nBracketing Matrix:\n')	
	
	for x in B:
		print(x)
	seq=generate_seq(B,[x for x in range (1,n+1)],0,n-1)	
	
	return seq

def main():
	dim=[]

	n=int(input('Enter no of matrices: '))
	for i in range(0,n):
		dim+=[[int(x) for x in input('Enter rows and cols of Matrix'+str(i+1)+': ').split(',')]]
	c=dim[0][1]
	for x in dim[1:]:
		if x[0]!=c:
			print("ERROR : Invalid input for multiplication:",x)
			return
		c=x[1]
				
	print('\n\nThe Optimal Sequence of multiplication is: ',mat_chain(dim))		

if __name__=='__main__':
	main()
