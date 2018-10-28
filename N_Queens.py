import sys

def n_queens(n,j,pos,seq,cnt):
	pos=[0 for x in pos]
	if j==n:
		print(seq)
		
	for i in range(0,j):
		
			pos[seq[i]]=1
			
			if seq[i]-(j-i) >= 0 :
				pos[seq[i]-(j-i)]=1
			if seq[i]+(j-i) <= n-1 :
				pos[seq[i]+(j-i)]=1
		
	for i in range(0,n) :
		if pos[i] == 0 :
			seq[j]=i
			n_queens(n,j+1,pos,seq,cnt)
			
						

def main(a):
	n=int(a[1])
	pos,seq=[],[]
	for i in range(0,n):
		pos+=[0]
		seq+=[0]
		
	n_queens(n,0,pos,seq,0)


if __name__=="__main__":
	main(sys.argv)
