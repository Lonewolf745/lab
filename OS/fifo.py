#fifo
n=int(input('Enter no of frames:'))
l=int(input('Enter length of ref string:'))
li=list(input('Enter reference string:').split())
a=[-1]*n
j=0
pf=0
t=0
for i in li:
    print('Pages in frames are:',end=' ')
    if i not in a:
        pf+=1
        if a[j]==-1:
            a[j]=i
            j+=1
        else:
            a[t]=i
            t+=1
        if j==n:
            j=0
        if t==n:
            t=0
        
        for k in a:
            print(k,end=' ')
        print()
    else:
        
        print('no page fault')
print('At the end of memory stream Pages in frames are:',end=' ')
for i in a:
    print(i,end=' ')
print()
print('page fault count=',pf)
