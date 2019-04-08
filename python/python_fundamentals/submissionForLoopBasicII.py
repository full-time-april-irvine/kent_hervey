# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

print("/n----spacer....#1")

def biggie_size(in_list):
    for i in range(0, len(in_list)):
        if in_list[i]>0:
            in_list[i]="big"
    return in_list
y = biggie_size([-1, 3, 5, -5])
print(y)

print("/n----spacer....#2")
#2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(in_list):
    count=0 
    for i in range(0, len(in_list)):
        if in_list[i]>0:
            count +=1
    in_list[len(in_list)-1]=count
    return in_list
#y = count_positives([1,6,-4,-2,-7,-2])
y=count_positives([-1,1,1,1])
print(y)

print("/n----spacer....#3")
# 3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(in_list):
    sum=0
    for i in range(0, len(in_list)):
        sum +=in_list[i]
    return sum
# y = sum_total([1,2,3,4])
y = sum_total([6,3,-2])
print(y)

print("/n----spacer....#4")
#4 Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(in_list):
    sum = 0
    for i in range(0, len(in_list)):
        sum += in_list[i]
    return sum/len(in_list)
y = average([1,2,3,4])
print(y)

print("/n----spacer....#5")
#5 Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(in_list):
    length_of =0
    for i in range(0,len(in_list)):
        length_of += 1
    return length_of
y = length([37,2,1,-9])
y = length([])

print(y)

print("/n----spacer....#6")
#6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(in_list):
    if len(in_list)==0:
        return False
    min_found = in_list[0]
    for i in range(0,len(in_list)):
        if in_list[i]<min_found:
            min_found = in_list[i]
    return min_found
y = minimum([37,2,1,-9])
y = minimum([])
print(y)

print("/n----spacer....#7")
#7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(in_list):
    if len(in_list)==0:
        return False
    max_found = in_list[0]
    for i in range(0,len(in_list)):
        if in_list[i]>max_found:
            max_found = in_list[i]
    return max_found
y = maximum([37,2,1,-9])
#y = maximum([])
print(y)

print("/n----spacer....#8")
#8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(in_list):
    sumTotal = 0
    minimum = in_list[0]
    maximum = in_list[0]
    length = 0
    for i in range(0,len(in_list)):
        length += 1
        sumTotal +=in_list[i]
        if in_list[i]>maximum:
            maximum = in_list[i]
        if in_list[i]<minimum:
            minimum = in_list[i]
    return { 'sumTotal': sumTotal, 'average': sumTotal/len(in_list), 'minimum': minimum, 'maximum': maximum, 'length': length}
y = ultimate_analysis([37,2,1,-9])
print(y)

print("/n----spacer....#9")
#9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(in_list):
    half_list = int(len(in_list)/2)
    for i in range(0, half_list):
        temp = in_list[i]
        in_list[i] = in_list[len(in_list)-1-i]
        in_list[len(in_list)-1-i]=temp
    return in_list 
y = reverse_list([37,2,1,-9])
print(y)



































