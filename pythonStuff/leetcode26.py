class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        past = 101
        x= 0
        while not x > len(nums)-1:
            if nums[x] == past:
                while not x > len(nums)-1 and nums[x] == past:
                    nums.pop(x)
            else:
                past = nums[x]
                x +=1