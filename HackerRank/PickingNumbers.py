def pickingNumbers(a):
    freq = [0] * 101 
    for num in a:
        freq[num] += 1

    max_count = 0
    for i in range(100):
        max_count = max(max_count, freq[i] + freq[i + 1])
    return max_count

        
res = pickingNumbers([4 ,6 ,5, 3 ,3, 1])
print(res)                              
