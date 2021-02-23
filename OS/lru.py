#lru 
def lru(li,ta):
    m=-1
    for i in range(len(li)-1,-1,-1):
        if li[i] in ta:
            ta.remove(li[i])
            if m==-1:
                m=i
            elif m>i:
                m=i            
    return li[m]
n=int(input('Enter no of frames:'))
l=int(input('Enter length of ref string:'))
li=list(input('Enter reference string:').split())
a=[-1]*n
j=0
pf=0
for i in range(l):
    print('Pages in frames are:',end=' ')
    if li[i] not in a:
        pf+=1
        if -1 in a:
            a[j]=li[i]
            j+=1
        else:
            t=a.index(lru(li[:i],a.copy()))
            a[t]=li[i]
        if j==n:
            j=0
        for k in a:
            print(k,end=' ')
        print()
    else:
        print('no page fault')
print('At the end of memory stream Pages in frames are:',end=' ')
for i in a:
    print(i,end=' ')
print()
print('page fault count:',pf)
    




    
