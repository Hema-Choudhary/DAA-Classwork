import sys


def find_num(num):
	i=1
	res=0
	res2=0
	
	for x in num:
		res^=i^x
		i+=1
		
	res^=(i)
	res^=(i+1)
	r=res
	res=bin(res)[2:].zfill(5)[::-1]
	
	pos=[i for i in range(len(res)) if res[i]=='1']
	
	
	i=1
	for x in num:
		if bin(i)[2:].zfill(5)[::-1][pos[0]]=='1':
			res2^=i
		
		if bin(x)[2:].zfill(5)[::-1][pos[0]]=='1':
			res2^=x
		i+=1
	if bin(i)[2:].zfill(5)[::-1][pos[0]]=='1':
			res2^=(i)
	if bin(i+1)[2:].zfill(5)[::-1][pos[0]]=='1':
			res2^=(i+1)
	
	return res2,r^res2
def main():
	num=[int(x) for x in input('Enter the numbers: ').split(',')]
	num1,num2=find_num(num)
	print('Missing numbers are: ',num1,'  ',num2)

if __name__=='__main__':
	main()
