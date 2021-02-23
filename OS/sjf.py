#Shartest job first
class  sjf:
    wt=0
    tat=0
    ct=0
    def __init__(self,name,bt):
        self.name=name
        self.bt=bt
        
obj=[]
twt,ttat=0,0
n=int(input('Enter no of process:'))
for i in range(0,n):
    na,b=input('Enter name , burst time of process:').split()
    obj.append(sjf(na,int(b)))
obj.sort(key=lambda x:x.bt)
print('Sorted order:')
for i in range(n):
    print(obj[i].name,end=' ')
print()
             
# calculation of table values 
for i in range(n):
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
for i in range(n):
    print('{}    {}   {}   {}   {}'.format(obj[i].name,obj[i].bt,obj[i].ct,obj[i].tat,obj[i].wt))

print('\nTotal wt:',twt)
print('Total tat:',ttat)
print('Avg wt:',twt/np)
print('Avg tat:',ttat/np)
