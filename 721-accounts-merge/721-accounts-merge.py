class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def dfs(key, connection):
            for node in graph[key]:
                if not visited.get(node, False):
                    visited[node] = True
                    connection.append(node)
                    dfs(node, connection)
            
        
        if len(accounts) < 1:
            return accounts
        
        graph = {}
        for account in accounts:
            
            account_name = account[0]
            emails = account[1:]
            email_key = emails[0]
            if email_key not in graph:
                graph[email_key] = []

            for email2 in emails[1:]:
                key2 = email2
                if key2 not in graph:
                    graph[key2] = []                
                graph[email_key].append(key2)
                graph[key2].append(email_key)
        
        visited = {}
        connections = []
        for account in accounts:
            account_name = account[0]
            emails = account[1:]
            email_key = emails[0]
            
            if not visited.get(email_key, False):
                visited[email_key] = True
                emails = [email_key]
                
                dfs(email_key, emails)
                
                
                connections.append([account_name, *sorted(emails)])
        
        return connections

        
        