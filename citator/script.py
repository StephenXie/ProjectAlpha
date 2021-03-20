def GetResult(n,style):
    if style == "upper":
        return n.upper()
    elif style == "lower":
        return n.lower()
    elif style == "title":
        return n.title()
    elif style == "one-line":
        res = ""
        for i in list(n):
            if i!="\r" and i!="\n":
                res+=i
        return res
    elif style == "space":
        return n.replace(" ","")
    elif style == "lstrip":
        res = []
        for i in n.split("\n"):
            res.append(i.lstrip())
        return "\n".join(res)
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