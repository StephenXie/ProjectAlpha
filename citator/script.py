def GetResult(n):
    return n.title()
def GetWordCount(n):
    return len(n.split())
def twoSum(arr,target):
    hm = {}
    for i,n in enumerate(arr):
        if n in hm:
            return [hm[n], i]
        else:
            hm[target-n] = i