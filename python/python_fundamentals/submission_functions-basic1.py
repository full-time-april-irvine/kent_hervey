#1
def a1():
    return 5
print (a1())
#predicted output:  5
# check
print("/n----spacer")
#2
def a2():
    return 5
print (a2() +a2())
#Analysis  print....(5 + 5)>>>  output is 10
#check
print("/n----spacer")
#3
def a3():
    return 5
    return 10
print (a3())
#analysis  a function only returns one thing, so in this case, it only returns 5, so output>>>5
print("/n----spacer....#4")
#4
def a4():
    return 5
    print(10)
print(a4())
#analysis  The function stops after any return, so print(10) never happens
#.........output:  5
#check
print("/n----spacer....#5")
#5
def a5():
    print(5)
x = a5()
print(x)
#analysis   x calls the function which prints 5, but there is no return statement, so print(x) does nothing
#check, but Python saw it as an error and printed None which is like null

print("/n----spacer....#6")
#6
def a6(b,c):
    print (b+c)
#print (a6(1,2) + a6(2,3))
#analysis:  again, there is no return statement, so the print statement that calls does not do what is probably expected
#the calling print statement calls the function twice and the function prints both times:
# first b=1 and c=2, so function prints 3
# second b =2 and c = 3, so function prints 5
#  output>>>  3  5
# checked, but again the interpreter complained that we tried to return something that does not exist

print("/n----spacer....#7")
#7
def a7(b,c):
    return str(b)+ str(c)
print (a7(2,5))
#analysis  function returns the concatenation of the string versions of passed in 2 and 5
#output:  25

print("/n----spacer....#8")
#8
def a8():
    b = 100
    print(b)
    if b<10:
        return 5
    else:
        return 10
    return 7
print (a8())
#analysis print calls the function and prints the return...so whatever is returned is the output
#function starts with b =100  b is not less than 10, so it falls to the else and returns 10.  note the "return 7 never happens in any case
# >>>output:  10
#check

print("/n----spacer....#9")
#9

def a9(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print (a9(2,3))
print (a9(5,3))
print (a9(2,3) + a9(5,3))
#analysis:  the function has no output, but it is called in three print statements and has return.  In the third statement is is called twice, so for the first two, the rsult is the return.  In the third case, the result is the sum of the returns
#first print:  b is 2; c is 3 so b is less than c and so return =7
#second print:  b is 5; c is 3 so b is not less than c an dso return= 14
#third print:  first call:  a=2; c=3, so ret=7...second call:  a=5;b=3, so ret=14, so print is 21
#output:  7 14 21
#check

print("/n----spacer....#10")
#10
def a10(b,c):
    return b+c
    return 10
print(a10(3,5))
#analysis  note that return never happens.  print is result of 3 + 5
#output:  8
#check

print("/n----spacer....#11")
#11
b = 500
print(b)
def a11():
    b =300
    print (b)
print(b)
a11()
print(b)
#analysis:  the trick in this there are two b variables...inside the function and outside
#flow is b=500 and print it, then print b again, then call the function which prints 300, then print the outside b which is still 500
#output:  500 500 300 500
#check

print("/n----spacer....#12")
#12
b=500
print(b)
def a12():
    b = 300 
    print (b)
    return b
print (b)
a12()
print(b)
#analysis:  flow:  b=500, then print b......print b again which is still 500
#......................call the function which prints a differnt b of 300 and returns 300, but to nowhere
#...........................print the outside b again which is still 500
#output:  500, 500, 300 500
#check

print("/n----spacer....#13")
#13
b = 500
print (b)
def a13():
    b = 300
    print (b)
    return b
print (b)
b=a13()
print(b) 
#analysis  prints outside b of 500, then prints it again 500 then b= calls the fucntion which prints inside b of 300 then print b prints the returned 300
#output 500 500 300 300
#check

print("/n----spacer....#14")
#14

def a14():
    print(1)
    b() 
    print(2)
def b():
    print(3)
a14()
#analysis  first thing that happens is calling of a14 which prints >> 1 <<  then calls b which prints >> 3 <<
#........then a14 prints >> 2  <<
#output  1 3 2
#check













