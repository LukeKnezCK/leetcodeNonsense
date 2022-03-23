class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 1 and gas[0]-cost[0] >= 0:
            return 0
        start = 0
        while start < n:
            if gas[start]-cost[start] > 0:
                currTotal = gas[start]-cost[start]
                counter = start+1
                while currTotal >= 0:
                    if counter == n:
                        counter = 0
                    elif counter == start:
                        return start
                    else:
                        currTotal += gas[counter]-cost[counter]
                        counter += 1
                if counter > start:
                    start = counter
                else:
                    start += 1
            else:
                start += 1
        return -1