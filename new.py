students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

dogs = [
    {'breed': 'chihuahua', 'age': '7 years old'},
    {'breed': 'pomeranian', 'age': '5 years old'},
]
# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)copy
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. 

def iterateDictionary(some_list):
    print(some_list)
    for diction in some_list: 
        print(diction)
        for key, val in diction.items():
            print(key, "-", val)

iterateDictionary(students)