import sys

def get_pattern(mat,p,q,s):
	i,j=p,q
	pat=[]
	val=mat[i][j]
	while(True):
		if(val==0):
			break
		elif(val==mat[i-1][j]):
			val=mat[i-1][j]
			i-=1
		elif(val==mat[i][j-1]):
			val=mat[i][j-1]
			j-=1
		elif(val==mat[i-1][j-1]+1):
			val=mat[i-1][j-1]
			j-=1
			i-=1
			pat=[s[i]]+pat
	return pat	

def get_lcs(s1,s2,m,n):
	
	mat=[]
	p=q=0

	for i in range(0,m+1): 	
	     lst=[]	
	     for j in range(0,n+1):
	           lst+=[0]
	     mat+=[lst]

	for i in range(0,m):			

		for j in range(0,n):
			if s1[i] == s2[j]:	
				mat[i+1][j+1]=mat[i][j]+1
			else:
				mat[i+1][j+1]=max(mat[i][j+1],mat[i+1][j])
			if mat[p][q] < mat[i+1][j+1]:
				p,q=i+1,j+1	
	for x in mat:
		print(x)

	pat=get_pattern(mat,p,q,s1)
	return (mat[p][q],p,q,pat)


def main(a):
	str1=a[1]
	str2=a[2]
	m=len(str1)
	n=len(str2)
	val,p,q,pat=get_lcs(str1,str2,m,n)
	print('val: ',val,'pattern: ',pat)
	
if __name__=='__main__':
	main(sys.argv)
