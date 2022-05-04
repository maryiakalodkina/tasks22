# task: find a needle in hain


def findANeedle(haystack, needle):
        index = -1
        firstEl = needle[0]

        if not haystack: 
            return 0
        if len(haystack)<len(needle):
            return index

        for indexHay, char in enumerate(haystack):
            if char == firstEl:
                tempIndex = indexHay
                for k in range(len(needle)): #0-3
                    if (tempIndex < len(haystack)) and (haystack[tempIndex] == needle[k]):
                        tempIndex += 1
                    else:
                        break

                    if (k == len(needle)-1):
                        return indexHay
                

        return index

haystack = "hello" 
needle = "lolo"
answer = findANeedle(haystack, needle)
print (answer)