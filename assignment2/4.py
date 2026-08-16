digits = [1, 0, 2, 4, 1, 7, 0, 4]

A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("Set A:", A)
print("Set B:", B)

union = A.union(B)
print("Union of A and B:", union)

intersection = A.intersection(B)
print("Intersection of A and B:", intersection)

A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print("A - B:", A_minus_B)
print("B - A:", B_minus_A)

# difference() gives elements unique to one specified set,
# while symmetric_difference() gives elements unique to both sets combined.

symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference:", symmetric_diff)

print("Is A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))

#Remove X using discard()
X = int(input("Enter a value X: "))
A.discard(X)

# discard() is safer than remove() because it does not raise an error if X is absent.

print("Set A after discard:", A)