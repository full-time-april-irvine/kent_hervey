#Problem 1, Update Values in Dictionaries and Lists

#A, given:  x = [ [5,2,3], [10,8,9] ] 
#.....Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 
print("before change x is:  ", x)
x[1][0]=15
print("after change x is:  ", x)

print("\n----spacer....#1B")

#1B  given: students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

#  Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}]
#This is a list of two dictionaires
#students[0]['last_name']="Bryant"
print(students)

print("\n----spacer....#1C")

#1C  In the sports_directory, change 'Messi' to 'Andres'
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(sports_directory['soccer'][0])
sports_directory['soccer'][0]="Andres"
print(sports_directory['soccer'][0])
print(sports_directory)

print("\n----spacer....#1D")

#1D Change the value 20 in z to 30
# z = [ {'x': 10, 'y': 20} ]

z = [ {'x': 10, 'y': 20} ]

print(z[0]['y'])
z[0]['y']=30
print(z[0]['y'])

print("\n----spacer....#2")
#2 Iterate Through a List of Dictionaries

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for dictionary in some_list:
        print("first_name - " + dictionary['first_name'] + " - last_name - " + dictionary['last_name'])

iterateDictionary(students)

print("\n----spacer....better way")
#That worked, but better to have it work even if we don't know the key names or the length
def iterate_list_of_dictionaries(list_of_dicts):
    for dictionary in list_of_dicts:
        result =""
        for key in dictionary.keys():
            result += str(key) + " - " + str(dictionary[key]) + ", "
        print(result[0:-2])
iterate_list_of_dictionaries(students)


print("\n----spacer....#3")
#3 Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel


def iterateDictionary2(key_name, list_of_dicts):
    for dictionary in list_of_dicts:
        print(dictionary[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

print("\n----spacer....#4")
#4 Get Values From a List of Dictionaries
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict.keys():
        print(str(len(some_dict[key])) + " " + key.upper() )
        for value in some_dict[key]:
            print (value)
        print("\n")

printInfo(dojo)










