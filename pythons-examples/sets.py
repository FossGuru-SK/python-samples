# Curly brackets
nameSet = {"alex", "sujit", "foss", "foss"}
print(nameSet)

nameSet = set(("alex", "sujit", "foss", "foss"))
print(nameSet)

nameSet = {"alex", "brian", "charles"}
 
nameSet.add("david")
print(nameSet)
 
nameSet.update(["evan", "frank", "george"])
print(nameSet)

print("************Below is for Removing items from Set***************")

nameSet = {"alex", "brian", "charles", "evan", "frank"}
 
nameSet.remove("frank")
print(nameSet)
 
nameSet.discard("evan")
print(nameSet)
 
name = nameSet.pop()
print(name)
print(nameSet)
 
nameSet.clear()
print(nameSet)
 
del nameSet
#print(nameSet)


nameSet1 = {"alex", "brian", "charles"}
nameSet2 = {"evan", "frank"}
 
setUnion = nameSet1.union(nameSet2)
print(setUnion)

nameSet1 = {"alex", "brian", "charles"}
nameSet2 = {"alex", "brian", "david"}
 
diffSet = nameSet1.difference(nameSet2)
print(diffSet)

ameSet1 = {"alex", "brian", "charles"}
nameSet2 = {"alex", "brian", "david"}
 
result = nameSet1.symmetric_difference(nameSet2)
print(result)

nameSet1 = {"alex", "brian", "charles"}
nameSet2 = {"alex", "brian", "david"}
 
nameSet1.update(nameSet2)
print(nameSet1)