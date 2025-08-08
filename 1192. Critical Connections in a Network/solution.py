class Solution:
    def __init__(self):
        self.timer=0
    def dfs(self,node,parent,adj,vis,tin,low,bridges):
        vis[node]=1
        tin[node]=low[node]=self.timer
        self.timer+=1
        for i in adj[node]:
            if i==parent:
                continue
            if vis[i]==0:
                self.dfs(i,node,adj,vis,tin,low,bridges)
                low[node]=min(low[node],low[i])
                if tin[node]<low[i]:
                    bridges.append([i,node])
            else:
                low[node]=min(low[node],low[i])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj=[[] for i in range(n)]
        for i in connections:
            u=i[0]
            v=i[1]
            adj[u].append(v)
            adj[v].append(u)
        vis=[0]*n
        tin=[0]*n
        low=[0]*n
        bridges=[]
        self.dfs(0,-1,adj,vis,tin,low,bridges)
        return bridges