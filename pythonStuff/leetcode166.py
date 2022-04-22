class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        whole, remainder = divmod(abs(numerator), abs(denominator))
        if numerator/denominator < 0:
            sign = '-'
        else:
            sign = ''
        result = [sign+str(whole),'.']
        remainders = {}
        
        while remainder not in remainders and remainder > 0:
            remainders[remainder] = len(result)
            whole, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(whole))
        
        if remainder in remainders:
            index = remainders[remainder]
            result.insert(index, '(')
            result.append(')')
        
        return ''.join(result).rstrip('.')