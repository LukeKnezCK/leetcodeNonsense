class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        outputList: int = []
        for x in range(len(nums)):
            
            #Check and see if the compliment of that number has been added to the dictonary
            compliment = target - nums[x]
            if str(compliment) in dict:
                outputList.append(dict[str(compliment)])
                outputList.append(x)
                return outputList
            #if the compliment for that number isnt found in the dictonary we add the number
            else:
                dict[str(nums[x])] = x
            