class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        collection = []
        while len(nums) > 0:
            currentBig = "0"
            for x in nums:
                stringo = str(x)
                if stringo[0] > currentBig[0]:
                    currentBig = stringo
                elif stringo+currentBig > currentBig+stringo:
                    currentBig = stringo
            collection.append(currentBig)
            nums.remove(int(currentBig))
        
        result = "".join(collection)
        if int(result) == 0:
            return "0"
        else:
            return result