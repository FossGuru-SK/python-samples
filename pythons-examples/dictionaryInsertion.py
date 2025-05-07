# Find comman keys and items
a = {'x': 1, 'y': 2, 'z': 1 }
b =  {'u': 1, 'x': 1, 'y': 2, 'v': 3, 'w': 4}

commanKeys = a.keys() & b.keys()
print(commanKeys)

commanItems = a.items() & b.items()
print(commanItems)

#Dictionary Intersection using ‘&’ Operator
setA = set(a)
setB = set(b)

setOfCommanKeys = setA & setB
print(setOfCommanKeys)

#Dictionary Intersection using Set.intersection()

setA = set(a)
setB = set(b)

setOfCommanKeysInsertion = setA.intersection( setB )
print(setOfCommanKeysInsertion)

#Dictionary Intersection using ‘collections‘ Module
from collections import Counter

comman_Keys = (Counter(a) & Counter(b)).keys()
print("Using Counter", comman_Keys)
print("Using Set with Counter", set(comman_Keys))

#Dictionary Intersection using Comprehension

comman_Comprehension_Keys = {key: a[key] for key in a if key in b}
print("Comprehension", comman_Comprehension_Keys)

