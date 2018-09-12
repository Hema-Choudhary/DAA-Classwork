#                                                             INSERTION SORT
#                                                             --------------

import sys

def i_sort(e):
    l=len(e)
    for i in range(1,l):
        j=i
        while(j>0):
            if(e[j]<e[j-1]):
                e[j]=e[j]^e[j-1]
                e[j-1]=e[j-1]^e[j]
                e[j]=e[j]^e[j-1]
                j-=1
            else:
                break
           
    print("After sort\n",e)           

def main():
    ele=[]
    no=int(input("Enter no of elements:"))
    for i in range(0,no):
        ele.append(int(input()))
    print("Before Sort:\n",ele)
    i_sort(ele)

if __name__=='__main__':
    main()
