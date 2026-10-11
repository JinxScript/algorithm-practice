
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        storeSet = set()

        for i in nums:
            if i in storeSet:
                return True
            storeSet.add(i)

        return False