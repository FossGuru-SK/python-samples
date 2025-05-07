import heapq

company = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(1, company, key= lambda s: s['price'])
print("smallest", cheap)

cheap = heapq.nsmallest(3, company, key= lambda s: s['price'])
print("3 smallest", cheap)

cheapest = min(company, key= lambda s: s['price'])
print("Cheapest Company",cheapest)

expensive = max(company, key= lambda s: s['price'])
print("Expensive Company", expensive)