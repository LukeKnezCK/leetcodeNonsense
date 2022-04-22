class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        allPermutations = []
        for x in nums:
            holdinglist = []
            holdinglist.extend(self.permuteHelper([x],nums))
            if len(holdinglist) ==  0:
                    holdinglist = [[x]]
            else:
                for y in holdinglist:
                    y.append(x)
            allPermutations.extend(holdinglist)
        return allPermutations
            
    def permuteHelper(self, elements: list[int], nums: list[int] ) -> list[list[int]]:
        if len(elements) == len(nums):
            return []
        allPermutations = []
        for x in nums:
            holdinglist = []
            if x in elements:
                continue
            else:
                elements.append(x)
                holdinglist.extend(self.permuteHelper(elements,nums))
                elements.pop()
                if len(holdinglist) ==  0:
                    holdinglist = [[x]]
                else:
                    for y in holdinglist:
                        y.append(x)
                allPermutations.extend(holdinglist)
        return allPermutations