def happyLadybugs(bug):
    ladybugs = set([string for string in bug if string != "_"])
    if list(bug).count("_") < 1 and not isBugHappy(bug):
        return "NO"
    
    for ladybug in ladybugs:
        if list(bug).count(ladybug) < 2:
            return "NO"
    return "YES"
       

def isBugHappy(b):
    for bug in range(1, len(b)-1):
        if b[bug] == b[bug - 1] or b[bug] == b[bug + 1]:
            continue
        else:
            return False
    return True
    
    
res = happyLadybugs('RBY_YBR')
print(res)
