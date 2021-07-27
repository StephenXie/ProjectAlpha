def getFinal(G,w,C):
    """
    F = Final exam grade
    G = Grade you want for the class
    w = Weight of the final exam, divided by 100 (put weight in decimal form vs. percentage form)
    C = Your current grade
    """
    F = (G-((1-w)*C))/w
    return F

def getScore(F,w,C):
    """
    F = Final exam grade
    G = Grade you will get
    w = Weight of the final exam, divided by 100 (put weight in decimal form vs. percentage form)
    C = Your current grade
    Final Grade = Initial Grade*(1-W) + S*W
    """
    G = C*(1-w) + F*w
    return G