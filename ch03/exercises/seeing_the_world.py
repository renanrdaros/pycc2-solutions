# Exercise 3-8. Seeing the World

# store the locations in a list
places = ["Santorini", "Ibiza", "Grand Canyon", "Cambodia", "Japan", "Amalfi Coast", "Acapulco"]

# print the list in its original order
print(places)

# print the list in alphabetical order (without modifying it)
print(sorted(places))

# show that the list is still in its original order
print(places)

# print the list in reverse alphabetical order (without modifying it)
print(sorted(places, reverse=True))

# show that the list is still in its original order
print(places)

# reverse the list and show that its order has changed
places.reverse()
print(places)

# reverse the list again and show that it is back to its original order
places.reverse()
print(places)

# sort the list and show that its order has changed
places.sort()
print(places)

# reverse sort the list and show that its order has changed again
places.sort(reverse=True)
print(places)
