class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        map1 = {}
        map2 = {}
        for i,c in enumerate(s) :
            map1[c] = map1.get(c,0)+1

        for i,c in enumerate(t) :
            map2[c] = map2.get(c,0)+1
        return map1==map2