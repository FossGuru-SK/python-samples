# Unpacking into variables
data = ('ACME', 50, 91.1)
name, shares, price = data

print("Name:", name)
print("Shares:", shares)
print("Price:", price)

# Unpacking into function arguments
def sample_func(x, y, z):
    print(x + y + z)

params = (10, 20, 30)
sample_func(*params)


#Skip which you want 
# Example tuple with a variable length
my_tuple = (1, 2, 3, 4, 5)
# Collect the first two elements, skip the third, and collect the rest
first, second, *skip, last = my_tuple
#result
print("first", first)
print("Second", second)
print("Skiped", skip)
print("last", last)

# Example tuple with unwanted values
my_tuple = (1, 2, 3, 4, 5, 6)

# Unpack the tuple and ignore unwanted values
first, _, third, _, _, _ = my_tuple

# Print the values you're interested in
print("First:", first)
print("Third:", third)


my_tuple = (1, 2, 3, 4, 5)
first, second, third = my_tuple
