operators = {"+","-","*","/"}
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return tokens[0]
        firstToken = tokens.pop()
        if tokens[-1] in operators:
            secondToken = self.evalRPN(tokens)
        else:
            secondToken = tokens.pop()
        if tokens[-1] in operators:
            thirdToken = self.evalRPN(tokens)
        else:
            thirdToken = tokens.pop()
            
        print(thirdToken, firstToken, secondToken)
        match firstToken:
            case '+':
                return int(thirdToken) + int(secondToken)
            case '-':
                return int(thirdToken) - int(secondToken)
            case '*':
                return int(thirdToken) * int(secondToken)
            case '/':
                return math.trunc(int(thirdToken) / int(secondToken)) 
