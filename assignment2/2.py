scores = (1, 0, 2, 4, 1, 7, 0, 4)

highest = max(scores)
highest_index = scores.index(highest)

lowest = min(scores)
lowest_count = scores.count(lowest)

print("Highest score:", highest)
print("Index of highest score:", highest_index)
print("Lowest score:", lowest)
print("Number of times lowest appears:", lowest_count)

#Reverse the tuple and return it as a list
# Tuples are immutable, so they cannot be reversed in place.
reversed_scores = list(reversed(scores))
print("Reversed tuple as list:", reversed_scores)

#Search for a user-input score
score = int(input("Enter a score: "))

if score in scores:
    print("First occurrence index:", scores.index(score))
else:
    print("Score not present")

#Attempt to change an element
try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)
    # Tuples are immutable, so their elements cannot be changed directly unlike lists.

# v. Unpack tuple using *
first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)