class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        currentKeep = -float('inf')
        currentSell = 0
        
        for stockPrice in prices:
            prevKeep = currentKeep
            prevSell = currentSell
            
            currentKeep = max(prevKeep, prevSell - stockPrice)
            currentSell = max(prevSell, prevKeep + stockPrice)
            
        return currentSell