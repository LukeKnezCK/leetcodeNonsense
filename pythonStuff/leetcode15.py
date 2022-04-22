def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        collection = []
        for x in range(len(nums)-2):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            l, r = x+1, len(nums)-1
            while l < r:
                sum = nums[x] +nums[l] +nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    collection.append((nums[x], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l +=1
                    r-=1
        return collection