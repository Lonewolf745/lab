class routing_table:
    max_num = (1<<31)-1
    d = {'dist':max_num,'next_hop':-1}
    def __init__(self, n):
        #initiating dist to max and next hop -1
        self.n = n
        self.dest = [{'dist':(1<<31)-1,'next_hop':-1} for i in range(n)] 

    def print1(self):
        for i in range(self.n):
            print(i,self.dest[i]['dist'],self.dest[i]['next_hop'])
        print()

class graph:
    def __init__(self,n):
        self.n = n
        self.nodes = [routing_table(n) for i in range(n)]
        print('Adjacency matrix:')
        self.adj_mat = [list(map(int,input().split())) for i in range(n)]

    def first_change(self):
        nodecount = 0
        for node in self.nodes:
            for i in range(self.n):
                node.dest[i]['dist'] = self.adj_mat[nodecount][i]
                node.dest[i]['next_hop'] = i
                #self.print1()
            nodecount+=1
        return True
    

    def find_next_hops(self):
        flag = False
        for node in self.nodes:
            #for every dest "i" in "node"'s routing table find next min possible hop
            for i in range(self.n):
                for j in range(self.n):
                    via_j = node.dest[j]['dist'] + (self.adj_mat[j][i] if self.adj_mat[i][j]!=0 else (1<<31)-1)
                    if node.dest[i]['dist']>via_j:
                        node.dest[i]['dist'] = via_j
                        node.dest[i]['next_hop'] = j
                        flag = True
        return flag


    def distance_vector_routing(self):
        changed = self.first_change()
        while changed:
            changed = self.find_next_hops()

    def print1(self):
        for node in range(self.n):
            print('node{}-dist-nextHop'.format(node))
            self.nodes[node].print1()
            





n = int(input('Enter no.of nodes:'))

#creating graph
g = graph(n)

g.distance_vector_routing()
print()
g.print1()


