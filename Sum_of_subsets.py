import sys


def sum_of_subsets(lst,s,ans,i,seq):
	
	if ans==s:
		print(seq)
		return
	
	elif i==len(lst) or ans > s:
		return	
	
	else:
		seq+=[lst[i]]
		sum_of_subsets(lst,s,ans+lst[i],i+1,seq)
		seq.remove(lst[i])
		sum_of_subsets(lst,s,ans,i+1,seq)
		

def main():

	lst=[int(x) for x in input('Enter the numbers: ').split(',')]
	#print(lst)
	s=int(input('Enter the sum value: '))
	#print(s)	
	sum_of_subsets(lst,s,0,0,[])	
	
	
if __name__=='__main__':
	main()
