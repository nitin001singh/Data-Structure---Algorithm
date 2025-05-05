def strangeCounter(t):
    rem = 3
    while t > rem:
        t -= rem
        rem = rem*2
    return rem - t + 1


res = strangeCounter(10)
print(res)

