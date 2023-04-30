class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        num_words = len(strs)
        adj = defaultdict(list)

        def dfs(node):
            visited[node]=True
            for ngh in adj[node]:
                if not visited[ngh]:
                    dfs(ngh)

        def isSimilar(a,b):
            diff = 0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    diff+=1
            return True if diff in [0,2] else False

        for i in range(num_words):
            for j in range(i,num_words):
                if isSimilar(strs[i],strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        
        visited = [False]*num_words
        component = 0
        for i in range(num_words):
            if not visited[i]:
                dfs(i)
                component+=1
    
        return component
    
strs = ["tars","rats","arts","star"]
obj = Solution()
obj.numSimilarGroups(strs)
