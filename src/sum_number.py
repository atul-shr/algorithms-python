class Solution:
    def two_sum(self, nums, target: int) :
        for i in range(0,len(nums)):
            if i + 1 == len(nums):
                # print(f"List Out of Range, sum not found")
                return []
            elif nums[i] + nums[i+1] == target:
                # print(f"Yes , nums[i] - {nums[i]} , nums[i+1] - {nums[i+1]}")
                return [i, i+1]
            else:
                # print(f"No , nums[i] - {nums[i]} , nums[i+1] - {nums[i + 1]}")
                return []


obj = Solution()

print(obj.two_sum([3,3], 6))
