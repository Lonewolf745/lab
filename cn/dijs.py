#diijsktra's 
class node:
    def __init__(self):
        self.label=False 
        self.length=(1<<31)-1
        self.predecessor=None
class graph:
    def __init__(self):
        self.n=None
        self.adj=[]
        self.path=[]
    def dijkstra(self,src,dest):
        ele=[node() for i in range(self.n)]
        ele[src].length=0
        ele[src].lable=True
        k=src
        while k!=dest:
            for i in range(self.n):
                if self.adj[k][i]!=0 and (not ele[i].label) and  ele[i].length>self.adj[k][i]+ele[k].length:
                    ele[i].predecessor=k
                    ele[i].length=self.adj[k][i]+ele[k].length
            k=0
            mini=10**9
            for i in range(self.n):
                if (not ele[i].label) and ele[i].length<mini:
                    mini=int(ele[i].length)
                    k=i
            ele[k].label=True
        i,k=1,dest
        while k:
            self.path.append(k)
            k=ele[k].predecessor
            i+=1
        if self.path[-1]!=src:
            self.path.append(src)
                
        return i
    def print(self,n):
        for i in range(n-1,-1,-1):
            print(chr(self.path[i]+97),end='->')
        return    
            
g=graph()
g.n=int(input('Enter number of nodes:'))
print('Enter adjacency matrix:')
for i in range(g.n):
    g.adj.append(list(map(int,input().split())))
src,des=map(int,input('Enter src,des:').split())
ans=g.dijkstra(src,des)
g.print(ans)
            
            
            
