

#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(top_number):
    out_list = []
    for counter in range(top_number, 0-1, -1):
        out_list.append(counter)
    return out_list

y = countdown(5)
print("problem 1, countdown result", y)
print("/n----spacer....#2")

#2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(inList):
    #inlist = [1,2]
    x = inList[0]
    print(x)
    return inList[1]

y = print_and_return([1,2])
print(y)


print("/n----spacer....#3")
#3First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(inList):
    return inList[0] + len(inList)

print(first_plus_length([1,2,3,4,5]))

print("/n----spacer....#4")
#4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(inList):
    new_List = []
    num_greater = 0    
    if len(inList)<2:
        return False
    for i in range(0, len(inList)):
        if inList[i]>inList[1]:
            new_List.append(inList[i])
        num_greater = num_greater+1
    print("asdf", num_greater)
    return new_List

#y = values_greater_than_second([5,2,3,2,1,4])
y = values_greater_than_second([3])
print(y)






