#Banker's Algo for deadlock avoidance
def bankers(Max,allocated,available):
    #calculation of available array
    for i in allocated:
        l=0
        for j in i :
            available[l]-=j
            l+=1
    print('Available cpu instances:',available)
    safesequence=''
    flag=set()
    rows=len(Max)
    col=len(Max[0])
    print('rows:{} col:{}'.format(rows,col))
    i=0
    while True:
        if len(flag)==rows:
            print('safe sequence:',safesequence)
            break
        if i==rows:
            i=0
        count=0
        for j in range(col):
            if (Max[i][j]-allocated[i][j])<=available[j]:
                count+=1
            else:
                break
        if count==col and i not in flag:
            flag.add(i)
            safesequence+='p'+str(i)+'->'
            for t in range(col):
                #print('allocated instances of {} type resource for process p{}:{} '.format(t,i,Max[i][t]))
                available[t]+=allocated[i][t]
        i+=1
                     
resrc=int(input('Enter no of resource types :'))
cpuinst=list(map(int,input('Enter cpu instances for each resource with space').split()))
np=int(input('Enter number of process:'))
Max=[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
allocated=[[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
# taking Max matrix
#print('Enter Max matrix of process:')
#for i in range(np):
    #tl=[int(i) for i in input().split()]
    #Max.append(tl)
# taking Allocated matrix
#print('Enter Allocated matrix of process:')
#for i in range(np):
    #tl=[int(i) for i in input().split()]
    #allocated.append(tl)

while True:
    bankers(Max,allocated,cpuinst.copy())
    f=input('Do you want to continue press 1:')
    if f=='1':
        m=int(input(('Enter the process that is requesting:')))
        print('enter resource instances:')
        Max[m]=list(map(int,input().split()))
    else:
        break
        

        
        

