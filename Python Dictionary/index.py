d = {1:10, 2:20}

# print(d[1])

# for x in d.keys():
#     print(x)
    
# for index, value in d.items():
#     print(index, ":" ,value)
    
# for value in d.values():
#     print(value)

d1 = dict(a=100, b=200, c=300)
# print(d1['a'])

# print(d1.get('b'))
# print(d1.get('d',0))   # if key does not exist


# d1['a'] = d1['a'] * 10

# print(d1)

# del d1['c']

# print(d1)
 
# poppedItem = d1.pop('a')   # return value not key
# print(poppedItem)

# print(d1)

# key, val = d1.popitem()
# print(key, val)

print(d1)

print( 'c' in d1 )

print( 'c' in d1.keys() )

print(len(d1))

print(d1.setdefault("d" , "NITIN" ))

print(d1)

print( { key: value for key, value in d1.items() if key != "b"   } )

print(d1.pop('e', "Not Found"))
print(d1.pop('d', "Not Found"))
print(d1)

print(sum(d1.values()))

print( sum( map( lambda key : d1[key]  , d1  )    )  )     # Sum using map and lambda function 



key = [1,2,3]
values = ['a','b','c']

new_dict = { k:v for k,v in zip(key, values)}
print(new_dict)

print( dict([ (x, 2*x) for x in [1,2,3,4,5] ] ))