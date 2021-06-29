def getGPA_w(score_arr, weight_arr, credit_arr):
    res = 0
    credit = 0
    for i in range(len(score_arr)):
        temp = scoreToVal(score_arr[i])
        temp = getWeighted(temp, weight_arr[i])
        res += temp*float(credit_arr[i])
        credit += float(credit_arr[i])
    # print(score_arr, weight_arr, credit_arr)
    # print(res/credit)
    return res/credit


def getGPA_u(score_arr, credit_arr):
    res = 0
    credit = 0
    for i in range(len(score_arr)):
        temp = scoreToVal(score_arr[i])
        res += temp*float(credit_arr[i])
        credit += float(credit_arr[i])
    # print(score_arr, credit_arr)
    # print(res/credit)
    return res/credit


def getMaxGPA(weight_arr):
    res = 0
    for i in range(len(weight_arr)):
        res += getWeighted(4, weight_arr[i])
    # print("Max")
    # print(weight_arr)
    # print(res/len(weight_arr))
    return res/len(weight_arr)


def scoreToVal(grade):
    dic = {
        "A+": 4.3,
        "A": 4,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1,
        "D-": 0.7,
        "F": 0
    }
    return dic[grade]


def getWeighted(score, t):
    """
    H
    4 -> 5
    IB
    4 -> 5
    AP
    4 -> 5
    """
    if t == "AP/IB":
        score += 1
    if t == "H+":
        score += 1
    if t == "H-":
        score += 0.5
    if t == "C":
        score += 1
    return score
