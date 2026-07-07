class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dublicate = {}
        for i in nums:
            if i in dublicate:
                return True
            else:
                dublicate[i] = 1
        else:
            return False