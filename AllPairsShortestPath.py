import sys


def Short_P(mat,i,n):
	if i==n:
		return mat
	else:
		mat2=[[0 for x in range(n)] for x in range(n)]	
		j=0
		while(j<n):
			k=0
			while(k<n):
				sum=0
				if j==i or k==i:
					mat2[j][k]=mat[j][k]
				else:
					if mat[j][i]=='N' or mat[i][k]=='N':
						mat2[j][k]=mat[j][k]
						
					else:
						sum=mat[j][i]+mat[i][k]
						if mat[j][k]=='N':
							mat2[j][k]=sum			
						elif sum < mat[j][k]:
							mat2[j][k]=sum	
				k+=1
			j+=1	
		return Short_P(mat2,i+1,n)


def main():
	n=int(input('Enter number of Vertices:'))
	mat=[[0 for x in range(n)] for y in range(n)]
	for x in range(n):
		for y in range(n):
			ip=input('Enter the weight of the edge between V'+str(x)+' to V'+str(y)+' (N if no edge): ')
			if ip=='N':
				mat[x][y]='N'
			else:
				mat[x][y]=int(ip)				
	res=Short_P(mat,0,n)
	print('---------------Shortest Paths for---------------')
	for x in range(n):
		for y in range(n):
			print('V'+str(x)+'->V'+str(y)+': ',res[x][y])
				
if __name__=='__main__':
	main()
