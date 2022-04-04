class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqs = [[] for i in range(numCourses)]
        visited = [[0] for i in range(numCourses)]
        result = []
        
        for x, y in prerequisites:
            preReqs[x].append(y)
            
        def courseTraversal(classNum):
            if visited[classNum] == -1:
                return False
            if visited[classNum] == 1:
                return True
            visited[classNum] = -1
            for j in preReqs[classNum]:
                if not courseTraversal(j):
                    return False
            visited[classNum] = 1
            result.append(classNum)
            return True
        
        for x in range(numCourses):
            if not courseTraversal(x):
                return []
        return result
        
        