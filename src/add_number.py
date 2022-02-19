class Solution:
    def twoSum(self, nums, target):
        if len(nums) == 0:
            print("list Empty")
            return []
        for i in range(0,len(nums)):
            print(nums[i])
            for j in range(i+1, len(nums)):
                try:
                    if nums[i] + nums[j] == target:
                        return [i, j]
                except:
                    print("List Ended")
                    return []


num = Solution()

print(num.twoSum(nums = [2,7,11,15], target = 9) == [0,1])
print(num.twoSum(nums = [3,2,3], target = 6) == [0,2])
