#Task 1: Join set A and set B
A = {19, 22, 24, 20, 25, 26};
B = {19, 22, 20, 25, 26, 28, 27};
# C = A | B; #joining operation |
C = A.union(B);
print(C);

#Task 2: Find Intersection of A and B
intersection = A.intersection(B); #Another way of performing intersection "A & B"
print(intersection);

#Task 3: Is A subset of B
is_subset = B.issubset(A);
print(is_subset);

#Task 4: A and B are disjoint sets
is_disjoint = A.isdisjoint(B);
print(is_disjoint);

#Task 5: Join A with B and B with A
A_with_B = A.union(B);
B_with_A = B.union(A);
print(A_with_B)
print(B_with_A);

#Task 6: What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B);
print(symmetric_diff);

#Task 7: Delete the sets completely
del A, B;
