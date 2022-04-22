class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        for x in range(len(nums)):
            currentVal = [nums.pop(0)]
            results.append(currentVal)
            results.extend(self.subsetsHelper(nums, currentVal))
        results.append([])
        results.sort()
        return results               
            
    def subsetsHelper(self, nums: List[int], lastSet: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        else:
            results = []
            for y in range(len(nums)):
                currentVal = copy.deepcopy(lastSet)
                currentVal.append(nums[y])
                results.append(currentVal)
                currentBranch = self.subsetsHelper(nums[y+1:], currentVal)
                results.extend(currentBranch)
            return results