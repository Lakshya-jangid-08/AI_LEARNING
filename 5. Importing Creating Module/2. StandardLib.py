import array 

arr = array.array('i', [1, 2, 3, 4, 5]) ## i means here 'signed int'
print(arr)

# High lvl of  operations on file and collection of files
import shutil

import os
print(os.getcwd())

from random import *
print(randint(1,1000))
print(choice(["apple", "banana", "cherry"]))

import json
data = {
    'name' : 'John Doe',
    'age' : 30,
    'city' : 'New York'
}
json_data = json.dumps(data)
print(json_data)
print(type(json_data))

parsed_data = json.loads(json_data)
print(parsed_data)
print(type(parsed_data))    

import datetime

now = datetime.datetime.now() 
print("Current date and time:", now)

yesterday = now - datetime.timedelta(days=1)
print("Yesterday's date and time:", yesterday)

from time import *

currTime = time()
print("Current time in seconds since epoch:", currTime)
sleep(2)  # Sleep for 2 seconds
print("Time after sleeping for 2 seconds:", time())