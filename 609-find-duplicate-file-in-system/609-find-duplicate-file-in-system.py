class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dup = {}
        for path in paths:
            
            path_and_files = path.split()
            path_name = path_and_files[0]
            files = path_and_files[1:]
            
            for file in files:
                file_name, content = file.split('(')
                if content not in dup:
                    dup[content] = []
                dup[content].append (path_name + '/' + file_name)
        return [v for k, v in dup.items() if len(v) > 1]
                