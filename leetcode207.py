class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create a list where each element is a list of the n's preReqs where n is the class and equal to list[n]
        pairs = [[] for i in range(numCourses)]
        #a list of each class and whether or not we have visited them yet. 
        #If 0, then we havent visited yet
        #If -1, then we have visited
        #If 1 then we have visited and there is no loop.
        visited = [0 for i in range(numCourses)]

        #Fill out our pairs ie. [  class0: [preReqs]  class 1: [preReqs]  class 2: [preReqs]    ]
        for x,y in prerequisites:
            pairs[x].append(y)
            
        #For each class passed, check the preReqs of that class and mark them as visited
        #If we visit a class twice in a single recursive call stack then return false
        def dfs(i):
            if visited[i]==-1:
                return False
            if visited[i]==1:
                return True
            visited[i] = -1
            for j in pairs[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
            
        #For each course determine if there is a loop that prevents completion
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

Solution.canFinish(Solution,3,[[1,0],[1,2],[0,1]])