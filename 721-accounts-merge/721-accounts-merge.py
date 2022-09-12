class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def dfs(key, connection):
            
            for node in graph[key]:
                if node not in visited:
                    visited.add(node)
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

            for email in emails[1:]:
                if email not in graph:
                    graph[email] = []                
                graph[email_key].append(email)
                graph[email].append(email_key)
        
        visited = set()
        merged_accounts = []
        
        for account in accounts:
            account_name = account[0]
            emails = account[1:]
            email_key = emails[0]
            
            if email_key not in visited:
                visited.add(email_key)
                emails = [email_key]
                dfs(email_key, emails)
                emails.sort()
                merged_accounts.append([account_name, *emails])
        return merged_accounts