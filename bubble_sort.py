#                                                                  BUBBLE SORT
#                                                                  -----------


import sys

def b_sort(e):
    flg=0
    l=len(e)
    i=1
    j=0
    while(i<l):
        while(j<l-i):
            if(e[j] > e[j+1]):
                flg=1
                t=e[j]
                e[j]=e[j+1]
                e[j+1]=t
            j+=1
        if(flg==0):
           break
        else:
            flg=0
        j=0
        i+=1
    print("\nAfter sort:\n",e)



def main():
    no=int(input("Enter no of elements:"))
    ele=[0]*no
    for i in range(0,no):
         ele[i]=int(input())
    print("Before Sort:\n",ele)
    b_sort(ele)
    

if __name__=='__main__':
    main()
