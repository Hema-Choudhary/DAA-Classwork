import sys

obj_info={'no':0,'p':0,'w':0,'p/w':0}

def calc(maxP,wg):
        f=0.0
        p=0
        for d in maxP:
                        wg-=d['w']
                        if wg<0:
                                wg+=d['w']
                                f=wg/d['w']
                                wg=0
                                p+=f*d['p'] 
                                break    
                        p+=d['p']
        print("Profit: ",p)                


def main():
        obj_lst=[]
        no=int(input('Enter no of objects:'))
        wg=int(input('Enter the capacity of bag(in weight)'))
        for i in range(0,no):
                obj_info['no']=i+1
                obj_info['p']=int(input('Enter profit'))        
                obj_info['w']=int(input('Enter weight'))
                obj_info['p/w']=float(obj_info['p']/obj_info['w'])
                obj_lst.append(obj_info.copy())
        #print(obj_lst)
        maxP=sorted(obj_lst,key=lambda i : i['p'],reverse=True)
        calc(maxP,wg)
        
        maxP=sorted(obj_lst,key=lambda i : i['w'])
        calc(maxP,wg)
        
        maxP=sorted(obj_lst,key=lambda i : i['p/w'],reverse=True)
        calc(maxP,wg)

if __name__ == '__main__':
        main()
