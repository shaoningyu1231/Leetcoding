class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        graph = defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                graph[accounts[i][j]].append(i)
        #dfs
        visit = set()
        def dfs(i, email):
            if i in visit:
                return
            visit.add(i)
            for m in range(1, len(accounts[i])):
                email.add(accounts[i][m])
                for nei in graph[accounts[i][m]]:
                    dfs(nei, email)
        #traverse
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if i in visit:
                    continue
                email, name = set(), accounts[i][0]
                dfs(i, email)
                res.append([name] + sorted(email)) 
        return res
