def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> int:
    
    def minHeightHelper(lowest:int, rootPursuit: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 0
        else:
            lowestReturn = lowest
            for z in range(len(edges)):
                if rootPursuit in edges[z]:
                    if rootPursuit == edges[z][0]:
                        newPursuit = edges[z][1]
                    else:
                        newPursuit: int = edges[z][0]
                    copyEdges = copy.deepcopy(edges)
                    del copyEdges[z]
                    checker = minHeightHelper(lowestReturn, newPursuit, copyEdges) + 1
                    if checker < lowestReturn:
                        lowestReturn = checker
        return lowestReturn
    
    
    
    if n <= 2:
        printOut: List = []
        for i in range(n):
            printOut.append(i)
        return printOut
    else:
        printOut: List = []
        minHeightCount: int = n
        heightHolder: int
        for i in range(n):
            deepEdges = copy.deepcopy(edges)
            heightHolder = minHeightHelper(n, i, deepEdges)
            if heightHolder < minHeightCount:
                minHeightCount = heightHolder
                printOut.clear()
                printOut.append(i-1)
            elif heightHolder == minHeightCount:
                printOut.append(i-1)
        return printOut
        
findMinHeightTrees("aye", 4, [[1,0],[1,2],[1,3]]) 

