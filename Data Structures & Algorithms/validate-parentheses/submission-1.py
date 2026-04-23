class Solution:
    def isValid(self, s: str) -> bool:
        map1 = { ')':'(',  
                 '}':'{'  ,   
                 ']':'[' }
        stack = []
        for c in s :
            if c in map1 :
                if not stack or stack[-1] != map1[c]:
                    return False 
                stack.pop()
            else :
                stack.append(c)
        return not stack 