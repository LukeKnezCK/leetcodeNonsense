def reverse(self, x: int) -> int:
        if x < 0:
            convertedList = list(map(int, str(abs(x))))
            pointer = len(convertedList) - 1
            flippedList = []
            while pointer >= 0:
                flippedList.append(convertedList[pointer])
                pointer -=1
            sList = [str(integer) for integer in flippedList]
            sList.insert(0,'-')
            s = ''.join(sList)
            result = int(s)
            if -2**31 <= result:
                return result
            else:
                return 0
        else:
            convertedList = list(map(int, str(x)))
            pointer = len(convertedList) - 1
            flippedList = []
            while pointer >= 0:
                flippedList.append(convertedList[pointer])
                pointer -=1
            sList = [str(integer) for integer in flippedList]
            s = ''.join(sList)
            result = int(s)
            if result <= 2**31:
                return result
            else:
                return 0