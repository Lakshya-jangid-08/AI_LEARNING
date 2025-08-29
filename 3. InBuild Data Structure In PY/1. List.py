# ordered and mutable collection of items

lst = [1, 2, 3, 4, 5]
print("List:", lst)
print("Type:", type(lst))

mixed_list = [1, "two", 3.0, True]
print("Mixed List:", mixed_list)

# Accessing elements
fruits = ["apple", "banana", "cherry", "guava"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

print("Slicing fruits:", fruits[1:3])  # Slicing from index 1 to 2
print("Slicing 1 to end:", fruits[1:])  # Slicing from index 1 to end
print("Slicing start to 2:", fruits[::2])  # Slicing from start to index 1


# list operations
# appending elements
fruits.append("orange")
print("After appending 'orange':", fruits)

# inserting elements
fruits.insert(0, "kiwi")
print("After inserting 'kiwi' at index 0:", fruits)

fruits.insert(2, "banana")
print("After inserting 'banana' at index 2:", fruits)

# removing elements
fruits.remove("banana") # Removes the first occurrence of 'banana'
print("After removing 'banana':", fruits)

removed_items = fruits.pop()  # Removes the last element and return removed last element
print("After popping last element:", fruits)
print("Removed last element:", removed_items)

fruits.index("cherry")  # Returns the index of 'cherry'
print("Index of 'cherry':", fruits.index("cherry"))

# Counting occurrences
print("Count of 'apple':", fruits.count("apple"))  # Count occurrences of 'apple'

# Sorting the list
fruits.sort()  # Sorts the list in ascending order
print("Sorted fruits:", fruits)

# Reversing the list
fruits.reverse()  # Reverses the order of the list
print("Reversed fruits:", fruits)

new_LIST = fruits[1:5]
print("Sliced new list from index 1 to 4:", new_LIST)
# :: means all elements from start to end   fruits[::]
# fruits[::k] means all elements from start to end with step k

## iteraating over the list
for fruit in fruits :
    print("Fruit: ", fruit)

#if i want to iterating index based then i have to use enumerate
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)

#list comprehension
fruit_lengths = []
for fruit in fruits:
    fruit_lengths.append(len(fruit))

fruit_lengths = [len(fruit) for fruit in fruits]
# list comprehension FOR [what will output  Kind of operation]
print("Fruit lengths:", fruit_lengths)

## Basic list comprehension syntex              [output_wants kind_of_operation]
## conditional logic list comprehension syntex  [output_wants kind_of_operation if_condition]
## nested list comprehension syntex            [output_wants for1_item_in_itr for2_item_in_iterable]

nums = [num**2 for num in range(10)]
print("Squared numbers:", nums)  # Squares of numbers from 0 to 9
nums = [num**2 for num in range(10) if num % 2 == 0]  # Only even numbers squared
print("Squared even numbers:", nums)

nums = [1 , 2, 3, 4]

nums = [nums1 * nums2 for nums1 in nums for nums2 in nums]
print("Cartesian product of nums with itself:", nums)
fruits.clear()  # Clears the list