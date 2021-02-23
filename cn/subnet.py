#broadcast tree
class node:
    def __init__(self,name):
        self.predessor = None
        self.length = (1<<31)-1
        self.label = False #tentative
        self.successor = False
        self.name = name
    def print1(self):
        print(self.predessor,self.length,self.label,self.successor)

class graph:
    def __init__(self,n):
        self.adj = []
        self.n = n
        self.path_array = []
        self.nodes = [node(i) for i in range(n)]
    
    def dijsktra(self, src, des):
        nodes = [node(i) for i in range(self.n)]
        nodes[src].length = 0
        nodes[src].label  = True #permanent

        k = src
        while k!=des:
            for i in range(self.n):
                if self.adj[k][i]!=0 and (not nodes[i].label) and nodes[i].length>self.adj[k][i]+nodes[k].length:
                    nodes[i].predessor = k
                    nodes[i].length = nodes[k].length+self.adj[k][i]
            k = 0
            mini = 10**9
            for i in range(self.n):
                if (not nodes[i].label) and nodes[i].length<mini:
                    mini = int(nodes[i].length)
                    k = i
            nodes[k].label = True #permanent

            self.nodes[nodes[k].predessor].successor = True
            self.nodes[k].length = nodes[k].length
            self.nodes[k].label = nodes[k].label
            self.nodes[k].predessor = nodes[k].predessor
            
            
    
    def print1(self):
        print('\nSubnet of hosts:')
        for i in range(self.n):
            if self.nodes[i].successor == False:
                ans=[]
                p = self.nodes[i]
                while True:
                    ans.append(p.name)
                    if p.predessor==None:
                        break
                    p = self.nodes[p.predessor]
                ans = list(ans[::-1])
                for j in ans[:-1]:
                    print(j,end='->')
                print(ans[-1],end='\n\n')



g = graph(int(input('enter number of nodes:')))
print('enter adjacent matrix:')
for i in range(g.n):
    g.adj.append(list(map(int,input().split())))

router = int(input('enter router:'))

for i in range(g.n):
    g.dijsktra(router,i)

g.print1()
