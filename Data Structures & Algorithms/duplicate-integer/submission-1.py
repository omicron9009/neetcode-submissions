class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = set()
        for n in nums :
            if n not in map1:
                map1.add(n)
            else :
                return True 
        return False   