def GetResult(n, style):
    if style == "upper":
        return n.upper()
    if style == "lower":
        return n.lower()
    if style == "title":
        return n.title()
    if style == "one-line":
        res = ""
        for i in list(n):
            if i != "\r" and i != "\n":
                res += i
        return res
    if style == "space":
        return n.replace(" ", "")
    if style == "lstrip":
        res = []
        for i in n.split("\n"):
            res.append(i.lstrip())
        return "\n".join(res)
    return n


def GetWordCount(n):
    return len(n.split())


def GetCharCount(n):
    return str(len(n.replace(" ", "")))+"/" + str(len(n))


def twoSum(arr, target):
    hm = {}
    for i, n in enumerate(arr):
        if n in hm:
            return [hm[n], i]
        hm[target-n] = i
