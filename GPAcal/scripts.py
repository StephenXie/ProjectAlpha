def getGPA(score_arr,weight_arr,flag):
    res = 0
    for i in range(len(score_arr)):
        temp = scoreToVal(score_arr[i])
        if flag:
            temp = getWeighted(temp,weight_arr[i])
        res+=temp
    return res/len(score_arr)
def scoreToVal(grade):
    dic = {
        "A+":4.3,
        "A":4,
        "A-":3.7,
        "B+":3.3,
        "B":3,
        "B-":2.7,
        "C+":2.3,
        "C":2,
        "C-":1.7,
        "D+":1.3,
        "D":1,
        "D-":0.7,
        "F":0
    }
    return dic[grade]
def getWeighted(score,t):
    """
    H
    4 -> 5
    IB
    4 -> 5
    AP
    4 -> 5
    """
    if t:
        score+=1
    return score
