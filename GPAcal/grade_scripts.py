def getFinal(G, w, C):
    """
    F = Final exam grade
    G = Grade you want for the class
    w = Weight of the final exam, divided by 100 (put weight in decimal form vs. percentage form)
    C = Your current grade
    """
    w /= 100
    F = (G-((1-w)*C))/w
    return F


def getScore(F, w, C):
    """
    F = Final exam grade
    G = Grade you will get
    w = Weight of the final exam, divided by 100 (put weight in decimal form vs. percentage form)
    C = Your current grade
    Final Grade = Initial Grade*(1-W) + S*W
    """
    w /= 100
    G = C*(1-w) + F*w
    return G


def getScore_avg(F, w, C, A, N):
    """
    F = Final exam grade
    N = Number of graded assignments in the category
    A = Average assignments grade in the category
    G = Grade you will get
    w = Weight of the final exam, divided by 100 (put weight in decimal form vs. percentage form)
    C = Your current grade
    Final Grade = Initial Grade*(1-W) + ((A*N+S)/(N+1))*W
    """
    w /= 100
    G = C*(1-w) + ((A*N+F)/(N+1))*w
    return G

print(getScore_avg(100,20,97,100,5))
