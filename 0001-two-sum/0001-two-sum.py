class Solution(object):
    def twoSum(self, nums, target):
        store_dict = {}

        for i, num in enumerate(nums):
            if target - num in store_dict:
                return [store_dict[target - num], i]

            store_dict[num] = i

        return []