#lambda function to used as function which have only one expression

def is_even_func(num):
    return num % 2 == 0

is_even = lambda num: num % 2 == 0   ## lambda parameter : return val
is_even(103434)
print("Is 103434 even?", is_even(103434))

is_adult_and_male = lambda person: person["age"] > 18 and person["gender"] == "male"

people = [
    {"name": "Alice", "age": 30, "gender": "female"},
    {"name": "Bob", "age": 25, "gender": "male"},
    {"name": "Charlie", "age": 35, "gender": "male"}
]

adult_male_names = list(map(lambda person: person["name"], filter(is_adult_and_male, people)))
print("Adult male names:", adult_male_names)
