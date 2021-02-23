#first come first serve
class fcfs:
    wt=0 #waiting time
    ct=0 #comletion time
    tat=0 #turn arund time
    def __init__(self,name,at,bt):
        self.name=name
        self.at=at
        self.bt=bt
obj=[]
twt,ttat=0,0

np=int(input('Enter number of process:'))
for i in range(np):
    name,at,bt=input('Enter process name arrival time and burst time:').split()
    obj.append(fcfs(name,int(at),int(bt)))
    
#sorting  according to arrival time
obj.sort(key=lambda x:x.at)

print('\nSorted order:')
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
        obj[i].tat=obj[i].ct-obj[i].at
        obj[i].wt=obj[i].tat-obj[i].bt
    ttat+=obj[i].tat
    twt+=obj[i].wt


#table printing
print('\nTable:')
print('name  at  bt  ct  tat  wt')
for i in range(np):
    print('{}     {}   {}   {}   {}   {}'.format(obj[i].name,obj[i].at,obj[i].bt,obj[i].ct,obj[i].tat,obj[i].wt))

print('\nTotal wt:',twt)
print('Total tat:',ttat)
print('Avg wt:',twt/np)
print('Avg tat:',ttat/np)
