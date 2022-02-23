#Strange solution, runs in nlogn time but is still accepted under the O(n) requirement

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        counter = 1
        for x in nums:
            if x == counter:
                counter +=1
        return counter