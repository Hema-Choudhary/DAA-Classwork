import sys

def merge(n1,n2):
      i=0
      j=0
      k=0
      m=len(n1)
      e=len(n2)
      new=[0]*(m+e)
      while(i<m and j<e):
            if n1[i]<=n2[j]:
                  new[k]=n1[i]
                  k+=1
                  i+=1
            else:
                  new[k]=n2[j]
                  k+=1
                  j+=1
      if i!=m:
            for j in range(i,m):
                  new[k]=n1[j]  
                  k+=1                        
      elif j!=e:
            for i in range(j,e):
                  new[k]=n2[i] 
                  k+=1
      return new                                

def divide(num,i,j):
      k=0
      if i<j:
            k=int((i+j)/2)
            num[i:k+1] = divide(num,i,k)
            num[k+1:j+1] = divide(num,k+1,j)
            return merge(num[i:k+1],num[k+1:j+1])
      else:
            return [num[i]]

def main(a):
      arr=a[1].split(',')
      num=[]
      for x in arr:
            num+=[int(x)]
      num=divide(num,0,len(num)-1)      
      print(num)

if __name__=='__main__':
      main(sys.argv)
