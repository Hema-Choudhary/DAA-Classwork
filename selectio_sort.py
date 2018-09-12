#                                                          SELECTION SORT
#                                                          --------------
import sys

def find_min(e):
    min=0
    for x in range(0,len(e)):
        if e[x] < e[min]:
            min=x
    return(min)    


def s_sort(e):
    l=len(e)
    for i in range(0,l-1):
        min=i+1+find_min(e[i+1:])
        if(e[i]>e[min]):
            t=e[i]
            e[i]=e[min]
            e[min]=t
    return e        

def main():
    ele=[]
    no=int(input("\nEnter no of elements:"))
    for i in range(0,no):
        ele=ele+[int(input())]
    print("Elements before sorting:\n",ele)
    print("After Sort\n",s_sort(ele))
    

if __name__=='__main__':
    main()
