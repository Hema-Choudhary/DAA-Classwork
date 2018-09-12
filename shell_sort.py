#                                                       SHELL SORT
#                                                       ----------

import sys

def shell_sort(n):
      l=len(n)
      t=0
      start=int(l/2)
      while(start>=1):
            for i in range(start,l):
                   '''
                   if n[i-start]>n[i]:
                          t=n[i-start]
                          n[i-start]=n[i]
                          n[i]=t
                   '''   
                   j=i-start
                   while(j-start>=0 and n[j-start] > n[j]):
                                t=n[j-start]
                                n[j-start]=n[j]
                                n[j]=t
                                j=j-start
            start=int(start/2)                  
                              
      print("Sorted Array:",n)

def main(a):
      arr=a[1].split(',')
      num=[]
      for n in arr:
            num+=[int(n)]
      shell_sort(num)

if __name__=='__main__':
      main(sys.argv)
