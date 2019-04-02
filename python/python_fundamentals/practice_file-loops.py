for x in range(0, 10, 2):
    print(x)
print("space")
for x in range(5,1,-3):
    print(x)
print("space")

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)-1):
    print(i, my_list[i])
print("space")
my_dict = {"name": "Noelle", "language": "Python"} # dict are key-value pairs  iterator is the key
for k in my_dict:
    print(k, " is" , my_dict[k])
print("space")

#capitals = {"Texas": Austin", "NY":Albany"}
for key in my_dict.keys():
    print(key)
print("---------space")
for val in my_dict.values():
    print(val)

for key, val in my_dict.items():
    print(key, " = ", val)

count = 0
while count < 5:
    print("looping - ", count)
    count +=1
print("---------space")
y = 3
while y >0:
    print (y)
    y = y-1
else: 
    print("final")


