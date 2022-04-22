class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        sum = 1
        zeroCounter = 0
        for x in nums:
            if not x == 0:
                sum = sum * x
            else:
                zeroCounter += 1
        
        if zeroCounter == 0:
            for y in nums:
                result.append(sum//y)
        elif zeroCounter <= 1:        
            for y in nums:
                if y == 0:
                    result.append(sum)
                else:
                    result.append(0)
        else:
            for y in nums:
                result.append(0)
        return result