def GetResult(n,style):
    if style == "upper":
        return n.upper()
    elif style == "lower":
        return n.lower()
    elif style == "title":
        return n.title()
    else:
        return n
def GetWordCount(n):
    return len(n.split())
def GetCharCount(n):
    return str(len(n.replace(" ","")))+"/" + str(len(n))
def twoSum(arr,target):
    hm = {}
    for i,n in enumerate(arr):
        if n in hm:
            return [hm[n], i]
        else:
            hm[target-n] = i