
job_info={'no':0,'p':0,'d':0,'s':-1}

def calc(jobs,m):
        slots=[0]*m
        p=0
        for j in jobs:
                i=j['d']-1
                if slots[i] == 0:
                        slots[i]=j['no']
                        j['s']=i
                        p+=j['p']                
                else:
                        while(slots[i]!=0 and i>=0):
                                i-=1
                        if(i!=-1):
                                slots[i]=j['no']                              
                                j['s']=i  
                                p+=j['p']
        print("profit: ",p,"\n slots assigned: ",slots)                                             

def main():
        max=0
        job_lst=[]
        no=int(input('Enter no of jobs'))
        for i in range(0,no):
                job_info['no']=i+1
                job_info['p']=int(input('Enter profit'))
                job_info['d']=int(input('Enter deadline'))
                job_lst.append(job_info.copy())
                if max<job_info['d']:
                        max=job_info['d']
        job_lst=sorted(job_lst,key=lambda i: i['p'],reverse=True)
        calc(job_lst,max)
                           
if __name__=='__main__':
        main()
