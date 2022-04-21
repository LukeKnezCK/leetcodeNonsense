class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for x in asteroids:
            while len(result) and x < 0 and result[-1] > 0:
                if result[-1] == -x:
                    result.pop()
                    break
                elif result[-1] < -x:
                    result.pop()
                    continue
                elif result[-1] > -x:
                    break
            else:
                result.append(x)
        return result