'''
@author: amayamunoz
'''

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subtract_two_numbers(num1,num2):

    differenceOfTwoNumbers = num2 - num1

    return differenceOfTwoNumbers

x = subtract_two_numbers(40,70) 

print(x)
#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def divide_multiply_add(num, num1, num2, num3):
 divideMultiplyAdd = num / num1 * num2 + num3
return divideMultiplyAdd
x = divide_multiply_add(13, 1, 68, 4000)

print(x)
#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def equal_to(numb1, numb2):

    if(numb1 == numb2):

        return True

    else:

        return False



e = equal_to(7, 7)

print(e)



t = equal_to(6, 7)

print(t)
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def large_number(num, num1):

    if (num > num1):

        return num 

    elif (num == num1):

        return num

    else:

        return num1

    

l = large_number(10, 30)

print(l)



r = large_number(40, 20)

print(r)
#5) Define a function that takes in two words and returns a string that contains both words combined.
def two_words(wor1, wor2):

    twoWords = wor1 + wor2

    return twoWords



w = two_words("Merry", "Christmas")

print(w)
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def three_numbers(num1, num2, num3):

    if(num1 == (num2 or num3)):

        return True

    else:

        return False



tn = three_numbers(6, 6, 4)

print(tn)



nt = three_numbers(7, 7, 5)

print(nt)
#7) Define a function that prints your name.
def name(nam1, nam2, nam3):

    name = nam1 + nam2 + nam3

    return name



n = name("Victor", "Cameron", "Masayesva")

print(n)
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def color(str1, str2):

    if(str1 == str2):

        print("That's my favorite color")

    else:

        print("That is not my favorite color")



c = color("blue", "blue")

print(c)



s = color("blue", "red")

print(s)
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def equal_zero(num1):

    if(num1 == 0):

        print(0)

    elif(num1 > 0):

        print(num1 - 1)

        



z = equal_zero(1)

print(z)
'''YOUR OWN FUNCTION'''

#10) Create your own function that solves any problem you can think of.
def virus(c1, num9):
virus = c1 + num9
return virus
v = virus("COVID", "19")
print(v)