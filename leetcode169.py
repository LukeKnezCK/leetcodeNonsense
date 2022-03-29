class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        counter = {}
        biggo = nums[0]
        for x in nums:
            if x in counter:
                counter[x] += 1
                if counter[x] > counter[biggo]:
                    biggo = x
            else:
                counter[x] = 1
        return biggo