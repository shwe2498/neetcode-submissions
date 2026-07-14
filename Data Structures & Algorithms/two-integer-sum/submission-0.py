class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []

        seen_map = {} # num, index

        for i, num in enumerate(nums):
            comp = target - num

            if comp in seen_map:
                return [seen_map[comp], i]

            seen_map[num] = i

        return []