class Solution(object):
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]


#My solution which was too slow :<
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        if target == 0:
            return 1
        if target < 0:
            return 0
        counter = 0
        for x in nums:
            counter += Solution.combinationSum4(Solution,nums,target-x)
        return counter

print(Solution.combinationSum4(Solution,[4,2,1],32))