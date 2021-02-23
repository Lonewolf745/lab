# priority

class  priority:
    wt=0
    tat=0
    ct=0
    def __init__(self,name,bt,priority):
        self.name=name
        self.bt=bt
        self.priority=priority
        
obj=[]
twt,ttat=0,0
np=int(input('Enter no of process:'))
for i in range(0,np):
    na,b,pr=input('Enter name , burst time, priority of process:').split()
    obj.append(priority(na,int(b),int(pr)))
obj.sort(key=lambda x:x.priority)
print('Sorted order:')
for i in range(np):
    print(obj[i].name,end=' ')
print()
             
# calculation of table values 
for i in range(np):
    if i==0:
        obj[i].wt=0
        obj[i].ct=obj[i].bt
        obj[i].tat=obj[i].ct
    else:
        obj[i].ct=obj[i-1].ct+obj[i].bt
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
