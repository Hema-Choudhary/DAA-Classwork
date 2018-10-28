import sys


def optimal_merge_seq(num):
	seq=[]
	tot=0
	sum=0
	while(len(num) > 1):
		min1=min(num)
		num.remove(min1)
		min2=min(num)
		num.remove(min2)
		seq+=[(min1,min2)]
		sum=min1+min2
		num+=[sum]
	return num[0],seq	
		 


def main():
	num=[int(x) for x in input('Enter the sequence: ').split(',')]
	cost,seq=optimal_merge_seq(num)

	print('optimal merge cost: ',cost)
	print('Merge sequence: ',seq)


if __name__ == '__main__':
	main()
