# my_list = [1, 2, 3, 4, 5]
# mixed_list = [1, "apple", 3.14, True]

my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # Output: apple

# Use negative indexing to access items from the end.
print(my_list[-1])  # Output: cherry

#  .append() adds an item to the end.
my_list.append("orange")

# .insert(index, item) adds an item at the specified position.
my_list.insert(1, "blueberry")

# .remove(item) removes the first matching item.
my_list.remove("apple")

# Use del keyword or .pop() to remove an item at a specific index.
del my_list[0]  # Deletes the first item
my_list.pop(1)  # Removes and returns the item at index 1

# Slicing allows us to access a subset of items in a list.
my_list = [1, 2, 3, 4, 5, 6]
subset = my_list[1:4]  # [2, 3, 4]

# Omit the start or end index to slice from the beginning or to the end.
print(my_list[:3])  # [1, 2, 3]
print(my_list[3:])  # [4, 5, 6]

list_of_fruits = ["apple", "banana", "cherry", "date"]
print(list_of_fruits[0])
print(list_of_fruits[-1])
list_of_fruits.append("elderberry")
print(list_of_fruits)
list_of_fruits.insert(1,"blueberry")
print(list_of_fruits)
list_of_fruits.remove("banana")
print(list_of_fruits)

del list_of_fruits[0]
print(list_of_fruits)
print(list_of_fruits[1:3])
