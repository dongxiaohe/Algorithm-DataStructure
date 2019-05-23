class Solution:
    def simplifyPath(self, path):
        stack, pathList = [], path.split("/")
        for path in pathList:    
            if not path or path == "." or (path == ".." and not stack): continue
            elif path == "..": stack.pop()
            else: stack.append(path)

        return "/" + "/".join(stack) 
