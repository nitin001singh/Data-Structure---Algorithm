def designerPdfViewer(h, word):
    # Write your code here
    point = 0
    for chars in word:
        index = ord(chars) - 97
        point = max(point, h[index] )
    return point * len(word)

        
res = designerPdfViewer([1 ,3 ,1 ,3 ,1 ,4 ,1 ,3 ,2 ,5 ,5 ,5, 5, 5 ,5 ,5 ,5 ,5 ,5, 5, 5, 5, 5, 5 ,5 ,5],'abc')
print(res)                              
