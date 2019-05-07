from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def breadth_search(self, u):

        visited_list=[False]*(len(self.graph))
        queue=[]
        queue.append(u)
        visited_list[u]=True

        while(queue):
            vertex=queue.pop(0)
            print(vertex)
            for node in self.graph[vertex]:

                if(visited_list[node]==False):

                    queue.append(node)
                    visited_list[node]=True

    def depth_search_utils(self,u,visited_list):
        visited_list[u]=True
        print (u)
        for i in self.graph[u]:
            if(visited_list[i]==False):
                self.depth_search_utils(i, visited_list)

    def depth_first_search(self,u):
        visited_list=[False]*(len(self.graph))
        self.depth_search_utils(u,visited_list)

    



if __name__=='__main__':

    graph=Graph()
    u=[0,0,1,2,2,3]
    v=[1,2,2,3,3,0]
    for u,v in zip(u,v):
        graph.add_edge(u,v)
    graph.breadth_search(0)
    graph.depth_first_search(0)





