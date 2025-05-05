def eventConflicts(event1, event2):
    event1 = [ int(e1.replace(":",""))  for e1 in event1 ]
    event2 = [ int(e1.replace(":",""))  for e1 in event2 ]
    
    startEvent1 = event1[0]
    endEvent1 = event1[1]
    
    startEvent2 = event2[0]
    endEvent2 = event2[1]
    

    if (startEvent1 > endEvent2) or (startEvent2 > endEvent1):
        return False
    
    return True
    

res = eventConflicts(["10:00","11:00"], ["14:00","15:00"])
print(res)