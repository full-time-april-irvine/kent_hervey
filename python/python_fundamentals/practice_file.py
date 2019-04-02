is_hungry=True
has_freckles=False

age = 25
weight = 160.57 #float

name = "Joe Blue" #literal string

#Tuples
dog = ('Bruce', 'cocker spaniel', 19, False)
#print(dog[0]) #output: Bruce
#dog[1] = 'anything' makes and error becuase tuples are immutable

#Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
print("begin lists")
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2])
ninjas[0] = 'Francis'
ninjas.append('Michael')
print("\n")
# print(ninjas)
# ninjas.pop()
# print(ninjas)
# ninjas.pop(1)
# print("after pop(1)", ninjas)
#I note that Python allows removal of a value in any positi of a list

dictionary = "Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. "
print(dictionary)
enpty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'  #updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']  #adds a key-value pair if the kye doesn't exist
w = new_person.pop('weight')  # removes the specified key and returns the value
print (w)



#print(new_person)

print("\n")

what_type = "If we're ever unsure of a value or variable's data type, we can use the type function to find out. For example:"
print(what_type)

print(type(2.63))
print(type(new_person))

print(len(new_person))
print(len('Coding Dojo'))

print("\n")
print("\n")

print("Hello " + str(42))
total = 35
user_val = "26"
total = total + int(user_val)
print(total)



















