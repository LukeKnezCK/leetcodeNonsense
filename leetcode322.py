class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        x = 0
        combos = []
        while x < len(coins):
            combos.append([coins[x:],[amount]])
            x+=1
            
        def rCoins(combos: list[int],layer:int) -> int:
            newCombos = []
            for x in combos:
                if len(x[0]) == 0:
                    continue
                x[1][0] = x[1][0] - x[0][0]
                if x[1][0] == 0:
                    return layer
                if x[1][0] > 0:
                    newCombos.append(x)
                    newCombos.append([x[0][1:], x[1]])
            if len(newCombos) == 0:
                return -1
            layer += 1
            return rCoins(newCombos,layer)
                
        return rCoins(combos,1)

print(Solution.coinChange(Solution, [1,2], 3))