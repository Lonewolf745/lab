class node:
    def __init__(self):
        self.predecessor = None
        self.length = None
        self.label = False #tentative

class graph:
    def __init__(self):
        self.adj = []
        self.n = None
        self.path = []
    
    def dijsktra(self, src, des):

        ele = [node() for i in range(self.n)]
        ele[src].length = 0
        ele[src].label  = True #permanent

        k = src
        while k!=des:
            for i in range(self.n):
                if self.adj[k][i]!=0 and not ele[i].label and ele[i].length>self.adj[k][i]+ele[k].length:
                    ele[i].predecessor = k
                    ele[i].length = ele[k].length+self.adj[k][i]
        
            k = 0
            min = 10**9
            for i in range(self.n):
                if (not ele[i].label) and ele[i].length<min:
                    min = ele[i].length
                    k = i
            ele[k].label = True #permanent
        
        i,k = 1,des
        while k:
            self.path.append(k)
            k = ele[k].predecessor
            i+=1
        self.path.append(src)
        print(self.path)
        
        return i
    
    def print(self, n, ip2):
        print('The shortest path is:')
        for i in range(n-1,-1,-1):
            print(chr(self.path[i]+97),end='')
            if i>0:
                print('-->',end='')
        print('\n\nThe fwd tables are:')
        print('Dest address\t\tO/p Interface')
        for i in range(n-1,-1,-1):
            print(ip2,chr(self.path[i]+97))


g = graph()
g.n = int(input('enter number of nodes:'))
print('enter adjacent matrix:')
for i in range(g.n):
    g.adj.append(list(map(int,input().split())))

src,des = input('Enter src and dest:').split()
ip1,ip2 = input("Enter Ip's of src & dest:").split()

ans = g.dijsktra(ord(src)-97,ord(des)-97)

g.print(ans,ip2)