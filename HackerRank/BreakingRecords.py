import sys
def breakingRecords(scores):

    if not scores:
        return []
        
    highestScore = []
    lowestScore = []
    currentHighScore = 0
    currentLowScore = sys.maxsize
    for index, score in enumerate(scores):
        currentHighScore = max(currentHighScore, score)
        currentLowScore = min(currentLowScore, score)
        highestScore.append(currentHighScore)
        lowestScore.append(currentLowScore)
        
        
    pCount = 0    
    lCount = 0
    for index in range(1, len(highestScore)):
        if highestScore[index - 1] < highestScore[index]:
            pCount += 1
    
    for index in range(1, len(lowestScore)):
        if lowestScore[index - 1] > lowestScore[index]:
            lCount += 1
            
    return [pCount, lCount]
        
res = breakingRecords([10 ,5 ,20 ,20 ,4 ,5, 2, 25, 1])
print(res)