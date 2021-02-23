#best fit 
import random as ra
def allocate(start,end,j,i):
    global ms,hob,pro
    print('start:{},end:{},j:{},i:{}'.format(start,end,j,i))
    tms=ms-pro[i].size 
    print('Enter a starting address for process {} in range {} {} both inclusive:'.format(i,start,end-pro[i].size+1))
    pro[i].sadd=int(input())
    print('start add of pro :',i,pro[i].sadd)
    pro[i].min=pro[i].sadd
    pro[i].max=pro[i].min+pro[i].size-1
    print('pro min , pro max,pro size',pro[i].min,pro[i].max,pro[i].size)
    ms=tms # available memory after allocating process
    print('free size=',ms)
    
    hob[j].max=pro[i].sadd-1
    hob[j].size=hob[j].max-hob[j].min+1   #hob[j].min+pro[i].sadd #check this
    print('hole min,max,size:',hob[j].min,hob[j].max,hob[j].size)
    #new hole creation
    hob.append(hole(end-pro[i].max+1)) #check this
    
    lh=len(hob)-1
    hob[lh].min=pro[i].max+1
    hob[lh].max=end #check this
    print('new hole min,max,size:',hob[lh].min,hob[lh].max,hob[lh].size)

class hole:
    min=0
    max=0
    def __init__(self,size):
        self.size=size
class process:
    min,max,sadd=0,0,0
    def __init__(self,name,size):
        self.name=name
        self.size=size
#main
pro=[]
hob=[]
ms=int(input('Enter total memory size:'))
hob.append(hole(ms))
hob[0].min=0
hob[0].max=ms-1
print('hole0 min:0\nhole0 max:',ms-1)
i,j=0,0
while True:
    pn,ps=input('Enter pname,psize:').split()
    ps=int(ps)
    if ps>=ms:
        print('Can\'t allocate memory')
        i-=1
    else:
        pro.append(process(pn,ps))
        if i==0:
            allocate(0,ms-1,0,0)
        else:
            #hole is to be selected
            hob.sort(key=lambda x:x.size)
            lh=len(hob)
            for j in range(lh):
                if hob[j].size>=pro[i].size:
                    print('Seleceted hole min,max,size:',hob[j].min,hob[j].max,hob[j].size)
                    allocate(hob[j].min,hob[j].max,j,i)
                    break
            else:
                print('External frag')
    i+=1         
    x=input('Enter 1 to continue:')
    if x!='1':
        break
            
            
        

        
        
        
    
    

