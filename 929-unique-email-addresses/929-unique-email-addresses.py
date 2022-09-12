class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        output = set()
        
        for email in emails:
            local_name, domain_name = email.split('@')
           
            local_name = local_name.replace('.','')
           
                
            local_name = local_name.split('+')[0]
            output.add(local_name+'@'+domain_name)
        return len(output)