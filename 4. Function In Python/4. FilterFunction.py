#filter function used for take filtered element  from list
# filter(function_name, iterable)

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)


people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

def is_Adult(person):
    return person["age"] >= 18

adult_people = list(filter(is_Adult, people))
print("Adult people:", adult_people)