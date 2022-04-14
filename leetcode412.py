class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5 == 0:
                result.append("FizzBuzz")
            elif x % 3 == 0:
                result.append("Fizz")
            elif x % 5 == 0:
                result.append("Buzz")
            else:
                stringed = str(x)
                result.append(stringed)
        return result