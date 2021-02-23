#Round Robin 
class roundrobin:
    wt=0
    tat=0
    ct=0
    def __init__(self,name,bt):
        self.name=name
        self.bt=bt
obj=[]
np=int(input('Enter no of process:'))
ts=int(input('Enter time slice:'))
tbt=[]
twt,ttat=0,0
for i in range(np):
    na,bt=input('Enter name,burst time of process:').split()
    obj.append(roundrobin(na,int(bt)))
    tbt.append(int(bt))
i=0
count=0
flag=set()
f=0
tct=0
while(True):
    if tbt[i]>0:
        if i==0 and f!=1:
            if tbt[i]>=ts:
                obj[i].ct=ts
                tct+=ts
            else:
                obj[i].ct=tbt[i]
                tct+=tbt[i]
            tbt[i]-=ts
        else:
            f=1
            if tbt[i]>=ts:
                tbt[i]-=ts
                tct+=ts 
            else:
                tct+=tbt[i]
                tbt[i]-=ts
            obj[i].ct=tct
    if tbt[i]<=0 and i not in flag:
        flag.add(i)
        count+=1
        if count==np:
            break
    i+=1
    if i==np:
        i=0

#calculating tat,twt
for i in range(np):
    obj[i].tat=obj[i].ct
    obj[i].wt=obj[i].tat-obj[i].bt
    ttat+=obj[i].tat
    twt+=obj[i].wt
#table printing
print('\nTable:')
print('name bt  ct  tat  wt')
for i in range(np):
    print('{}    {}   {}   {}   {}'.format(obj[i].name,obj[i].bt,obj[i].ct,obj[i].tat,obj[i].wt))

print('\nTotal wt:',twt)
print('Total tat:',ttat)
print('Avg wt:',twt/np)
print('Avg tat:',ttat/np)          
            
            
            
        

    
    


            
            
            
    
 

