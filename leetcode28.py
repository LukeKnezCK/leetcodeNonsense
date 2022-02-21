def strStr(haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(haystack) == 0:
            return -1
        else:
            y = 0
            while y < len(haystack):
                if haystack[y] == needle[0]:
                    for x in range(len(needle)):
                        if y < len(haystack):
                            if haystack[y] != needle[x]:
                                y -= x -1
                                break
                            elif x == len(needle)-1:
                                return y - len(needle)+1
                            else:
                                y += 1
                        else:
                            return -1
                else:
                    y +=1
            return -1

strStr("mississippi"
,"issip")