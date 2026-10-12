class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexMap = {}
        for index_i, value_n in enumerate (nums):
            diff = target - value_n
            if diff in indexMap:
                return [indexMap[diff], index_i]
            indexMap[value_n] = index_i
        return 
