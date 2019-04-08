


#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
#BONUS: account for any edge cases (eg. min > max, max < 0)


import random
def randInt (min= 0, max= 100):
    adjustment = False
    if max < 1:
        max =1
        adjustment= True
    if min >max:
        min = max -1
        adjustment = True
    num = random.random() * (max-min) + min
    num = round(num)

    if (adjustment):
        return str(num) + " note adjustment was made for out of bound parameters"
    return num

y = randInt() #passed
y = randInt(max = 50) # passed
y = randInt(min = 50) # passed
y = randInt(min=50, max =500) #passed
y = randInt (min =50, max =40 )

print(y)