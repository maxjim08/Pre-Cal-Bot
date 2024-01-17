
# Set up
import random
import math
user_input = ''

# Incorrect counter
incorrect_CountP1 = 0
incorrect_CountP2 = 0
incorrect_CountP3 = 0
incorrect_CountP4 = 0

# Question: Express f in Standard form
#  ;Get the polynomial from general form to standard (vertex) form
# Given: f(x) = 2x^2 + 36x + 170
# Answer: f(x) = 2(x+9)^2 + 8
def calculator_problem1():
    coefficient_list = []
    for i in range (3):
        coefficient = int(input(f'What is the coefficient of x^{i}?\n'))
        coefficient_list.append(coefficient)
    coefficient_list.reverse()
    
    a = coefficient_list[0]
    b = coefficient_list[1]
    c = coefficient_list[2]

    d = b/a
    e = ((d**2)/(2**2))

    k = c - (a*(e))
    h = d/2
    if k > 0:
        if h > 0:
            print(f' The correct answer is:')
            print(f'{a}(x + {h})^2 + {k}')
        else: # h < 0
            print(f' The correct answer is:')
            print(f'{a}(x {h})^2 + {k}')
    else: # k < 0
        if h > 0:
            print(f' The correct answer is:')
            print(f'{a}(x + {h})^2 {k}')
        else: # h < 0
            print(f' The correct answer is:')
            print(f'{a}(x {h})^2 {k}')
    

def random_practice_problem1():
    coefficient_list = []

    # potential coefficients for b is assigned to an empty list
    potential_b = []

    pos = random.randint(0,1)
    if pos == 1: # positive 1st coefficient
        coeff1 = random.randint(2,4)

        # to change the number of possible questions, you can modify the number in the middle
        for b in range(2,9,2):
            potential_b.append(coeff1 * b)

        posit = random.randint(0,(len(potential_b)-1))
        coeff2 = potential_b[posit]

        pos2 = random.randint(0,1)
        if pos2 == 1: # positive 3rd coefficient
            coeff3 = random.randint(2,9)
            print(f' Express f(x) in Standard (Vertex) Form:')
            print(f'f(x) = {coeff1}x^2 + {coeff2}x + {coeff3}')

        else: # negative 3rd coefficient
            coeff3 = random.randint(2,9)
            coeff3 = coeff3 * -1
            print(f' Express f(x) in Standard (Vertex) Form:')
            print(f'f(x) = {coeff1}x^2 + {coeff2}x {coeff3}')

    else: # negative 1st coefficient
        coeff1 = random.randint(2,4)
        coeff1 = coeff1 * -1
            
        for b in range(2,9,2):
            potential_b.append(coeff1 * b)

        posit = random.randint(0,(len(potential_b)-1))
        coeff2 = potential_b[posit]

        pos2 = random.randint(0,1)
        if pos2 == 1: # positive 3rd coefficient
            coeff3 = random.randint(2,9)
            print(f' Express f(x) in Standard (Vertex) Form:')
            print(f'f(x) = {coeff1}x^2 {coeff2}x + {coeff3}')

        else: # negative 3rd coefficient
            coeff3 = random.randint(2,9)
            coeff3 = coeff3 * -1
            print(f' Express f(x) in Standard (Vertex) Form:')
            print(f'f(x) = {coeff1}x^2 {coeff2}x {coeff3}')
    
    # Finding the correct answer
    coefficient_list.append(coeff3)
    coefficient_list.append(coeff2)
    coefficient_list.append(coeff1)
    coefficient_list.reverse()
    
    a = coefficient_list[0]
    b = coefficient_list[1]
    c = coefficient_list[2]

    d = b/a
    e = ((d**2)/(2**2))

    k = c - (a*(e))
    h = d/2
    # To account for the formula being (x - h)
    h2 = h * -1

    # Need to prompt the use to enter their answer
    print('Format: f(x) = a(x - h)^2 + k')
    user_a = int(input('What is a?\n'))
    user_h = int(input('What is h?\n'))
    user_k = int(input('What is k?\n'))

    # Need to check if that answer is correct
    if (user_a == int(a)) and (user_h == int(h2)) and (user_k == int(k)):
        print('That is Correct!')
    else:
        print('Incorrect...')
        # Needs to keep track of how many times the user has gotten this question wrong
        incorrect_CountP1 += 1
    
    # Print out what the code things the correct answer is
    if k >= 0:
        if h > 0:
            print(f' The correct answer is:')
            print(f'{a}(x + {int(h)})^2 + {int(k)}')
        else: # h < 0
            print(f' The correct answer is:')
            print(f'{a}(x {int(h)})^2 + {int(k)}')
    else: # k < 0
        if h > 0:
            print(f' The correct answer is:')
            print(f'{a}(x + {int(h)})^2 {int(k)}')
        else: # h < 0
            print(f' The correct answer is:')
            print(f'{a}(x {int(h)})^2 {int(k)}')
            

    # Range of possible coefficients
##    for a in range (2,5):
##    for b in range(2,9,2):
##        for c in range(-8,-1):
##            print(f'{a} {a*b} {c + (2 * ((b**2)/(2**2)))} {c}')
##        for c in range(2,9):
##            print(f'{a} {a*b} {c + (2 * ((b**2)/(2**2)))} {c}')

    # Another solution
##    for a in range (2,5):
##    for b in range(2,9):
##        for c in range(-8,-1):
##            if ((c + (2 * ((b**2)/(2**2)))) % 1) == 0: # Ensures that the constant is an integer
##                print(f'{a} {a*b} {c + (2 * ((b**2)/(2**2)))}')
##        for c in range(2,9):
##            if ((c + (2 * ((b**2)/(2**2)))) % 1) == 0:
##                print(f'{a} {a*b} {c + (2 * ((b**2)/(2**2)))}')

    # First solution, but also including a negative first coefficient
##    for x in range(0,1):
##    for a in range (-4,-1):
##        for b in range(2,9,2):
##            for c in range(-8,-1):
##                print(f'{a} {a*b} {c + (2 * ((b**2)/(2**2)))} {c}')
##            for c in range(2,9):
##                print(f'{a} {a*b} {c + (2 * ((b**2)/(2**2)))} {c}')
##    for a in range (2,5):
##        for b in range(2,9,2):
##            for c in range(-8,-1):
##                print(f'{a} {a*b} {c + (2 * ((b**2)/(2**2)))} {c}')
##            for c in range(2,9):
##                print(f'{a} {a*b} {c + (2 * ((b**2)/(2**2)))} {c}')


def walkthrough_problem1():
    # Defining the problem to the user
    print(' The goal of this problem is to get from general form to standard (vertex) form.')
    print('The reason it is known as vertex form is because in the form:')
    print('    f(x) = a(x - h)^2 + k ; when h and k are aranged in a ordered pair,')
    print('that is the vertex of the parabula at the point (h,k)\n')

    # Important note about h
    print(' It is important to note that the formula is specifically (x - h),')
    print('so when asked for h, it will appear as though its sign has been swaped from when it is in the fromula.\n')

    # Step by step solution with example problem
    print(' Given: f(x) = 2x^2 + 36x + 170   -->   Answer: f(x) = 2(x+9)^2 + 8')
    print('1) Identify a, b, and c')
    print('   a is equal to the coefficient of x^2')
    print('   b is equal to the coefficient of x^1')
    print('   c is equal to the coefficient of x^0; also known as the constant')
    print(' So in this example a = 2, b = 36, and c = 170')
    input('Press "enter" to continue to the next step')

    print('2) If a is not one, then factor out the common number between a and b')
    print('   because a is 2 and b is 36, both of those numbers are divisible by 2')
    print('   you should be left with something like this')
    print('   -->   2 (x^2 + 18x) + 170')
    input('Press "enter" to continue to the next step')

    print('3) Our next step will be to create a perfect square by adding (b/2)^2')
    print('   To ensure that the equation does not change, we will also have to subtract (b/2)^2')
    print('   and multiply it by what was factored out, leaving you with this')
    print('   -->   2 (x^2 + 18x + (b/2)^2) + 170 - (2 * (b/2)^2)')
    print('   -->   2 (x^2 + 18x + (18/2)^2) + 170 - (2 * (18/2)^2)')
    input('Press "enter" to continue to the next step')

    print('4) The next step will be to solve for (b/2)^2')
    print('   you solve paranthesis first')
    print('   18/2 = 9; so you are left with (9)^2')
    print('   (9)^2 = 81; you can now plug this number in your equation')
    print('   -->   2 (x^2 + 18x + 81) + 170 - (2 * 81)')
    input('Press "enter" to continue to the next step')

    print('5) The second to last step will be to factor (x^2 + 18x + 81)')
    print('   you need two numbers that multiply to equal 81,')
    print('   but add up to equal 18; of course this is the numbers 9 and 9.')
    print('   9 * 9 = 81 and 9 + 9 = 18; when you substitute the factored form it should look like this')
    print('   -->   2 (x + 9)^2 + 170 - (2 * 81)')
    input('Press "enter" to continue to the next step')

    print('6) The final step would be to simplify (2 * 81) and subtract it from c')
    print('   (2 * 81) = 162 and 170 - 162 = 8')
    print('   -->   2 (x + 9)^2 + 8')
    print(' This is your final answer in standard (vertex) form\n')


# Similar to the random practice problem, but it doesn't tell you if you got it right or wrong instantly
def random_test_problem1():
    coefficient_list = []
    x = 0

    # potential coefficients for b is assigned to an empty list
    potential_b = []

    pos = random.randint(0,1)
    if pos == 1: # positive 1st coefficient
        coeff1 = random.randint(2,4)

        # to change the number of possible questions, you can modify the number in the middle
        for b in range(2,9,2):
            potential_b.append(coeff1 * b)

        posit = random.randint(0,(len(potential_b)-1))
        coeff2 = potential_b[posit]

        pos2 = random.randint(0,1)
        if pos2 == 1: # positive 3rd coefficient
            coeff3 = random.randint(2,9)
            print(f' Express f(x) in Standard (Vertex) Form:')
            print(f'f(x) = {coeff1}x^2 + {coeff2}x + {coeff3}')

        else: # negative 3rd coefficient
            coeff3 = random.randint(2,9)
            coeff3 = coeff3 * -1
            print(f' Express f(x) in Standard (Vertex) Form:')
            print(f'f(x) = {coeff1}x^2 + {coeff2}x {coeff3}')

    else: # negative 1st coefficient
        coeff1 = random.randint(2,4)
        coeff1 = coeff1 * -1
            
        for b in range(2,9,2):
            potential_b.append(coeff1 * b)

        posit = random.randint(0,(len(potential_b)-1))
        coeff2 = potential_b[posit]

        pos2 = random.randint(0,1)
        if pos2 == 1: # positive 3rd coefficient
            coeff3 = random.randint(2,9)
            print(f' Express f(x) in Standard (Vertex) Form:')
            print(f'f(x) = {coeff1}x^2 {coeff2}x + {coeff3}')

        else: # negative 3rd coefficient
            coeff3 = random.randint(2,9)
            coeff3 = coeff3 * -1
            print(f' Express f(x) in Standard (Vertex) Form:')
            print(f'f(x) = {coeff1}x^2 {coeff2}x {coeff3}')
    
    # Finding the correct answer
    coefficient_list.append(coeff3)
    coefficient_list.append(coeff2)
    coefficient_list.append(coeff1)
    coefficient_list.reverse()
    
    a = coefficient_list[0]
    b = coefficient_list[1]
    c = coefficient_list[2]

    d = b/a
    e = ((d**2)/(2**2))

    k = c - (a*(e))
    h = d/2
    # To account for the formula being (x - h)
    h2 = h * -1

    # Need to prompt the use to enter their answer
    print('Format: f(x) = a(x - h)^2 + k')
    user_a = int(input('What is a?\n'))
    user_h = int(input('What is h?\n'))
    user_k = int(input('What is k?\n'))

    # Need to check if that answer is correct
    if (user_a == int(a)) and (user_h == int(h2)) and (user_k == int(k)):
        x = 1
    return x


# Question: Find the Net Chage from x = a to x = b, where b > a
# Formula: f(b) - f(a)
# Given: f(x)= 3x^2 - 2x + 1; from x = 1 to x = 3
# Answer: 20
def calculator_problem2():

    coefficient_list = []
    for i in range (3):
        coefficient = int(input(f'What is the coefficient of x^{i}?\n'))
        coefficient_list.append(coefficient)
    coefficient_list.reverse()

    x1 = int(input('What is a?\n'))
    x2 = int(input('What is b?\n'))

    a = coefficient_list[0]
    b = coefficient_list[1]
    c = coefficient_list[2]

    fb = (a * (x2**2)) + (b * (x2)) + c
    fa = (a * (x1**2)) + (b * (x1)) + c
    ans = fb - fa
    
    print(f'The answer is: {ans}\n')
        

def random_practice_problem2():

    #set up
    count = 0
    coefficient_list = []
    coefficient_list2 = []
    coefficient_list3 = []
    
    for i in range (3):
        # Coinflip to determine if term is pos or neg
        pos = random.randint(0,1)
        if pos == 1: # positive term
            coeff = random.randint(2,16)

            coefficient_list.append(coeff)

        else: # negative term
            coeff1 = random.randint(2,16)
            coeff = coeff1 * -1

            coefficient_list.append(coeff)


    for coeff in coefficient_list:
        if (coeff > 0) and (count != 0): #if the coefficient is positive, the added condition ensures that the first coefficient isn't unecessarilly given a plus sign
            string = '+ ' + str(coeff)
            coefficient_list2.append(string)

        else: # the coefficient is negative
            coefficient_list2.append(str(coeff))

        count += 1


    count -= 1 # subtract 1 from count to ensure the last term's x is raised to the 0th power
    for coeff in coefficient_list2:

        if count == 0:
            coefficient_list3.append(coeff)
            break
        
        string2 = coeff + 'x^' + str(count)
        coefficient_list3.append(string2)

        count -= 1

    # Print out the randomly generated polynomial
    print('   f(x) = ', end='')
    for term in coefficient_list3:
        print(term, end=' ')
    

    # Randomly generate a and b
    a = random.randint(1,4)
    # Difference between a and b
    c = random.randint(1,4)

    b = a + c
    print(f'; Find the net change from x = {a} to x = {b}')

    # Promt the user to answer the question
    user_input = int(input())

    x = coefficient_list[0]
    x2 = coefficient_list[1]
    x3 = coefficient_list[2]

    fb = (x * (b**2)) + (x2 * (b)) + x3
    fa = (x * (a**2)) + (x2 * (a)) + x3
    ans = fb - fa

    # If true, then user got question right
    if user_input == ans:
        print('Correct')
    else: # User got the question wrong
        print('Incorrect')


def walkthrough_problem2():
    # Defining the problem to the user
    print(' The goal of this problem is to find the net change from the first input to the second')
    print('An important thing to note is that you need to make sure that b > a.')
    input('Press "enter" to continue to the next step')

    # Step by step solution with example problem
    print(' Given: f(x)= 3x^2 - 2x + 1; from x = 1 to x = 3   -->   Answer: 20')
    print('1) Identify your a and b')
    print(' Because 3 > 1, you know that b = 3 and a = 1')
    input('Press "enter" to continue to the next step')

    print('2) Calculate f(b)')
    print(' All this means is that you need to plug in 3 into the equation.')
    print(' 3(3)^2 - 2(3) + 1, which simplifies to 22.')
    input('Press "enter" to continue to the next step')

    print('3) Calculate f(a)')
    print(' Now do the same but with 1.')
    print(' 3(3)^2 - 2(3) + 1, which simplifies to 2.')
    input('Press "enter" to continue to the next step')

    print('4) Finally you need to solve f(b) - f(a)')
    print(' 22 - 2 = 20.')

def random_test_problem2():

    #set up
    count = 0
    coefficient_list = []
    coefficient_list2 = []
    coefficient_list3 = []
    score = 0
    
    for i in range (3):
        # Coinflip to determine if term is pos or neg
        pos = random.randint(0,1)
        if pos == 1: # positive term
            coeff = random.randint(2,16)

            coefficient_list.append(coeff)

        else: # negative term
            coeff1 = random.randint(2,16)
            coeff = coeff1 * -1

            coefficient_list.append(coeff)


    for coeff in coefficient_list:
        if (coeff > 0) and (count != 0): #if the coefficient is positive, the added condition ensures that the first coefficient isn't unecessarilly given a plus sign
            string = '+ ' + str(coeff)
            coefficient_list2.append(string)

        else: # the coefficient is negative
            coefficient_list2.append(str(coeff))

        count += 1


    count -= 1 # subtract 1 from count to ensure the last term's x is raised to the 0th power
    for coeff in coefficient_list2:

        if count == 0:
            coefficient_list3.append(coeff)
            break
        
        string2 = coeff + 'x^' + str(count)
        coefficient_list3.append(string2)

        count -= 1

    # Print out the randomly generated polynomial
    print('   f(x) = ', end='')
    for term in coefficient_list3:
        print(term, end=' ')
    

    # Randomly generate a and b
    a = random.randint(1,4)
    # Difference between a and b
    c = random.randint(1,4)

    b = a + c
    print(f'; Find the net change from x = {a} to x = {b}')

    # Promt the user to answer the question
    user_input = int(input())

    x = coefficient_list[0]
    x2 = coefficient_list[1]
    x3 = coefficient_list[2]

    fb = (x * (b**2)) + (x2 * (b)) + x3
    fa = (x * (a**2)) + (x2 * (a)) + x3
    ans = fb - fa

    # If true, then user got question right
    if user_input == ans:
        score += 1
    else: # User got the question wrong
        score = 0

    return score


# Question: Find the Average Rate of Chage from x = a to x = b, where b > a
# Formula: (f(b) - f(a)) / (b - a)
# Given: f(x)= 3x^2 - 2x + 1; from x = 1 to x = 3
# Answer: 10
def calculator_problem3():
    
    coefficient_list = []
    for i in range (3):
        coefficient = int(input(f'What is the coefficient of x^{i}?\n'))
        coefficient_list.append(coefficient)
    coefficient_list.reverse()

    x1 = int(input('What is a?\n'))
    x2 = int(input('What is b?\n'))

    a = coefficient_list[0]
    b = coefficient_list[1]
    c = coefficient_list[2]

    fb = (a * (x2**2)) + (b * (x2)) + c
    fa = (a * (x1**2)) + (b * (x1)) + c
    netcha = fb - fa
    ans = netcha / (x2 - x1)

    print(f'The answer is: {ans}\n')

def random_practice_problem3():

    #set up
    count = 0
    coefficient_list = []
    coefficient_list2 = []
    coefficient_list3 = []
    
    for i in range (3):
        # Coinflip to determine if term is pos or neg
        pos = random.randint(0,1)
        if pos == 1: # positive term
            coeff = random.randint(2,16)

            coefficient_list.append(coeff)

        else: # negative term
            coeff1 = random.randint(2,16)
            coeff = coeff1 * -1

            coefficient_list.append(coeff)


    for coeff in coefficient_list:
        if (coeff > 0) and (count != 0): #if the coefficient is positive, the added condition ensures that the first coefficient isn't unecessarilly given a plus sign
            string = '+ ' + str(coeff)
            coefficient_list2.append(string)

        else: # the coefficient is negative
            coefficient_list2.append(str(coeff))

        count += 1


    count -= 1 # subtract 1 from count to ensure the last term's x is raised to the 0th power
    for coeff in coefficient_list2:

        if count == 0:
            coefficient_list3.append(coeff)
            break
        
        string2 = coeff + 'x^' + str(count)
        coefficient_list3.append(string2)

        count -= 1

    # Print out the randomly generated polynomial
    print('   f(x) = ', end='')
    for term in coefficient_list3:
        print(term, end=' ')
    

    # Randomly generate a and b
    a = random.randint(1,4)
    # Difference between a and b
    c = random.randint(1,4)

    b = a + c
    print(f'; Find the average rate of change from x = {a} to x = {b}')

    # Promt the user to answer the question
    user_input = int(input())

    x = coefficient_list[0]
    x2 = coefficient_list[1]
    x3 = coefficient_list[2]

    fb = (x * (b**2)) + (x2 * (b)) + x3
    fa = (x * (a**2)) + (x2 * (a)) + x3
    netcha = fb - fa
    ans = netcha / (b - a)

    # If true, then user got question right
    if user_input == ans:
        print('Correct')
    else: # User got the question wrong
        print('Incorrect')
    

def walkthrough_problem3():
    # Defining the problem to the user
    print(' The goal of this problem is to find the average rate of change from the first input to the second')
    print('This is very similar to finding the net change, but with an added step.')
    print('An important thing to note is that you need to make sure that b > a.')
    input('Press "enter" to continue to the next step')

    # Step by step solution with example problem
    print(' Given: f(x)= 3x^2 - 2x + 1; from x = 1 to x = 3   -->   Answer: 10')
    print('1) Identify your a and b')
    print(' Because 3 > 1, you know that b = 3 and a = 1')
    input('Press "enter" to continue to the next step')

    print('2) Calculate f(b)')
    print(' All this means is that you need to plug in 3 into the equation.')
    print(' 3(3)^2 - 2(3) + 1, which simplifies to 22.')
    input('Press "enter" to continue to the next step')

    print('3) Calculate f(a)')
    print(' Now do the same but with 1.')
    print(' 3(3)^2 - 2(3) + 1, which simplifies to 2.')
    input('Press "enter" to continue to the next step')

    print('4) Solve f(b) - f(a)')
    print(' 22 - 2 = 20, This results in the netchange.')
    input('Press "enter" to continue to the next step')
    
    print('5) Take the net change and divide it by (b - a).')
    print(' 20 / (3 - 1) --> 20 / 2 --> 10')

def random_test_problem3():

    #set up
    count = 0
    coefficient_list = []
    coefficient_list2 = []
    coefficient_list3 = []
    score = 0
    
    for i in range (3):
        # Coinflip to determine if term is pos or neg
        pos = random.randint(0,1)
        if pos == 1: # positive term
            coeff = random.randint(2,16)

            coefficient_list.append(coeff)

        else: # negative term
            coeff1 = random.randint(2,16)
            coeff = coeff1 * -1

            coefficient_list.append(coeff)


    for coeff in coefficient_list:
        if (coeff > 0) and (count != 0): #if the coefficient is positive, the added condition ensures that the first coefficient isn't unecessarilly given a plus sign
            string = '+ ' + str(coeff)
            coefficient_list2.append(string)

        else: # the coefficient is negative
            coefficient_list2.append(str(coeff))

        count += 1


    count -= 1 # subtract 1 from count to ensure the last term's x is raised to the 0th power
    for coeff in coefficient_list2:

        if count == 0:
            coefficient_list3.append(coeff)
            break
        
        string2 = coeff + 'x^' + str(count)
        coefficient_list3.append(string2)

        count -= 1

    # Print out the randomly generated polynomial
    print('   f(x) = ', end='')
    for term in coefficient_list3:
        print(term, end=' ')
    

    # Randomly generate a and b
    a = random.randint(1,4)
    # Difference between a and b
    c = random.randint(1,4)

    b = a + c
    print(f'; Find the average rate of change from x = {a} to x = {b}')

    # Promt the user to answer the question
    user_input = int(input())

    x = coefficient_list[0]
    x2 = coefficient_list[1]
    x3 = coefficient_list[2]

    fb = (x * (b**2)) + (x2 * (b)) + x3
    fa = (x * (a**2)) + (x2 * (a)) + x3
    netcha = fb - fa
    ans = netcha / (b - a)

    # If true, then user got question right
    if user_input == ans:
        score += 1
    else: # User got the question wrong
        score = 0

    return score    


# Question: Determine the end behavior of the polynomial; express your answer in arrow notation
# Formula: 
# Given: f(x) = -x^4 + 4x^3 - 5x^2 + 2x + 3
# Asnwer: x -> infinity, y -> -infinity
#         x -> -infinity, y -> -infinity
def calculator_problem4():
    lt_pow = int(input('To what power is the leading term being raised to?\n'))
    lt_coef = input("Is the leading term's coefficient positive or negative? p/n\n")

    #Check if the power is even or odd
    if lt_pow % 2 == 0: # even
        if lt_coef == 'p': # positive
            print('x -> inf, y -> inf')
            print('x -> -inf, y -> inf')
        else: # negative
            print('x -> inf, y -> -inf')
            print('x -> -inf, y -> -inf')

    else: # odd
        if lt_coef == 'p': # positive
            print('x -> inf, y -> inf')
            print('x -> -inf, y -> -inf')
        else: # negative
            print('x -> inf, y -> -inf')
            print('x -> -inf, y -> inf')


def random_practice_problem4():

    # Set up
    coefficient_list = []
    coefficient_list2 = []
    coefficient_list3 = []
    num_items = random.randint(2,6)
    count = 0
    
    # Repeat x s times for every item in the polynomial
    for i in range(num_items):
        
        # Coinflip to determine if term is pos or neg
        pos = random.randint(0,1)
        if pos == 1: # positive term
            coeff = random.randint(2,16)

            coefficient_list.append(coeff)

        else: # negative term
            coeff1 = random.randint(2,16)
            coeff = coeff1 * -1

            coefficient_list.append(coeff)

    for coeff in coefficient_list:
        if (coeff > 0) and (count != 0): #if the coefficient is positive, the added condition ensures that the first coefficient isn't unecessarilly given a plus sign
            string = '+ ' + str(coeff)
            coefficient_list2.append(string)

        else: # the coefficient is negative
            coefficient_list2.append(str(coeff))

        count += 1

    count -= 1 # subtract 1 from count to ensure the last term's x is raised to the 0th power
    highest_power = count # the leading terms highest power is equal to count at this moment
    for coeff in coefficient_list2:

        if count == 0:
            coefficient_list3.append(coeff)
            break
        
        string2 = coeff + 'x^' + str(count)
        coefficient_list3.append(string2)

        count -= 1

    # Prompt the user to answer the randomly generated question
    print('   Determine the end behavior of the polynomial;\nexpress your answer in arrow notation:')
    print('Ex: x -> inf, y -> inf \n    x -> -inf, y -> -inf')
    print('   f(x) = ', end='')
    for term in coefficient_list3:
        print(term, end=' ')
    print()

    user_input = input('x -> inf, y -> ')
    user_input2 = input('x -> -inf, y -> ')

    if highest_power % 2 == 0: # even
        if coefficient_list[0] > 0: # pos
            # Check if user is correct
            if user_input == 'inf' and user_input2 == 'inf':
                print('Correct')
            else:
                print('Incorrect')
                
        else: # neg
            if user_input == '-inf' and user_input2 == '-inf':
                print('Correct')
            else:
                print('Incorrect')

    else: # odd
        if coefficient_list[0] > 0: # pos
            # Check if user is correct
            if user_input == 'inf' and user_input2 == '-inf':
                print('Correct')
            else:
                print('Incorrect')

        else: # neg
            if user_input == '-inf' and user_input2 == 'inf':
                print('Correct')
            else:
                print('Incorrect')


def walkthrough_problem4():
    # Defining the problem to the user
    print(' The goal of this problem is to identify the endbehavior of the given polynomial.')
    print('This is actually quite simple, all you need to do is look at the leading coefficient,')
    print('or the term that has the highest degree of x, and determine if it is positive or negative,')
    print('as well as if the its degree is even or odd.')
    input('Press "enter" to continue to the next step')

    # Step by step solution with example problem
    print(' Given: f(x) = -x^4 + 4x^3 - 5x^2 + 2x + 3   \n-->   Answer: x -> inf, y -> -inf; x -> -inf, y -> -inf')
    print('1) Identify the leading term')
    print(' In this example the leading term is -x^4)')
    print(' We know this because it is both the farthest left, and has the highest degree of four')
    input('Press "enter" to continue to the next step')

    print("2) Determine whether the leading term's degree is even or odd")
    print(' We know the degree to be 4, and 4 is even, so the degree is even.')
    print(' We also know that the simplest even degree polynomial is a parabula,')
    print('where both sides point upward.')
    input('Press "enter" to continue to the next step')

    print('3) Determine whether the leading term is positive or negative')
    print(' If the leading term happend to be positive, and even, then we would know')
    print('that the end behavior would go up to infinity on both the left and right sides.')
    print(' This is similar to how the most basic parabula works, but in our example')
    print('the leading term is negative, so the end behavior is fliped upside down.')
    print(' Where as x approaches infinity, y approaches -infinity, and')
    print('as x approaches -infinity, y approaches -infinity.')
    input('Press "enter" to continue to the next step')

    print("4) Express your answer in arrow notation")
    print(' x -> inf, y -> -inf')
    print(' x -> -inf, y -> -inf')
    input('Press "enter" to continue to the next step')

    # Important note about the other possibility
    print("It is also important to consider to posibility that the leading term's power was odd")
    print(' If it was odd, then the simplest degree polynomial would be the cubic curve')
    print('otherwise known as the shape that the graph y = x^3 makes.')
    print(' Where the right of the function goes to infinity, and the left of the function')
    print('goes to negative infinity')
    print(' And of course, if the leading term was negative, then it would be fliped upsidedown')


def random_test_problem4():

    # Set up
    coefficient_list = []
    coefficient_list2 = []
    coefficient_list3 = []
    num_items = random.randint(2,6)
    count = 0
    score = 0
    
    # Repeat x s times for every item in the polynomial
    for i in range(num_items):
        
        # Coinflip to determine if term is pos or neg
        pos = random.randint(0,1)
        if pos == 1: # positive term
            coeff = random.randint(2,16)

            coefficient_list.append(coeff)

        else: # negative term
            coeff1 = random.randint(2,16)
            coeff = coeff1 * -1

            coefficient_list.append(coeff)

    for coeff in coefficient_list:
        if (coeff > 0) and (count != 0): #if the coefficient is positive, the added condition ensures that the first coefficient isn't unecessarilly given a plus sign
            string = '+ ' + str(coeff)
            coefficient_list2.append(string)

        else: # the coefficient is negative
            coefficient_list2.append(str(coeff))

        count += 1

    count -= 1 # subtract 1 from count to ensure the last term's x is raised to the 0th power
    highest_power = count # the leading terms highest power is equal to count at this moment
    for coeff in coefficient_list2:

        if count == 0:
            coefficient_list3.append(coeff)
            break
        
        string2 = coeff + 'x^' + str(count)
        coefficient_list3.append(string2)

        count -= 1

    # Prompt the user to answer the randomly generated question
    print('   Determine the end behavior of the polynomial;\nexpress your answer in arrow notation:')
    print('Ex: x -> inf, y -> inf \n    x -> -inf, y -> -inf\n')
    print('   f(x) = ', end='')
    for term in coefficient_list3:
        print(term, end=' ')
    print()

    user_input = input('x -> inf, y -> ')
    user_input2 = input('x -> -inf, y -> ')

    if highest_power % 2 == 0: # even
        if coefficient_list[0] > 0: # pos
            # Check if user is correct
            if user_input == 'inf' and user_input2 == 'inf':
                score += 1
            else:
                score = 0
                
        else: # neg
            if user_input == '-inf' and user_input2 == '-inf':
                score += 1
            else:
                score = 0

    else: # odd
        if coefficient_list[0] > 0: # pos
            # Check if user is correct
            if user_input == 'inf' and user_input2 == '-inf':
                score += 1
            else:
                score = 0

        else: # neg
            if user_input == '-inf' and user_input2 == 'inf':
                score += 1
            else:
                score = 0

    return score


# Main Program: (While the user still wants to continue using the program)

while user_input != 'n':
    # Print out the main menu
    user_input = input('Please select from one of following options and hit Enter:\n 1) User Defined Variable Problems\n 2) Random Practice Problems\n 3) Walkthrough Practice Problems\n 4) Graded Test with a varibale number of questions\n')

    # User picked option 1 (User Defined Variable Problems)
    if user_input == '1':
        user_input = input('Please select from one of the following questions and hit Enter:\n 1) General Form to Standard (Vertext) Form\n 2) Find the Net Change\n 3) Find the Average Rate of Chage\n 4) Determine the End Behavior of the Polynomial Expressed in Arrow Notation\n')
        if user_input == '1':
            print(f' Ex: 2x^2 + 36x + 170\n')
            while user_input != 'n':
                calculator_problem1()
                user_input = input('Would you like to solve another problem?\n')

        elif user_input == '2':
            print(f' Ex: f(x) = 3x^2 - 2x + 1 ; Find the net change from x = 1 to x = 3\n')
            while user_input != 'n':
                calculator_problem2()
                user_input = input('Would you like to solve another problem?\n')

        elif user_input == '3':
            print(f' f(x) = 3x^2 - 2x + 1 ; Find the average rate of change from x = 1 to x = 3')
            while user_input != 'n':
                calculator_problem3()
                user_input = input('Would you like to solve another problem?\n')
                
        elif user_input == '4':
            while user_input != 'n':
                calculator_problem4()
                user_input = input('Would you like to solve another problem?\n')
        
    # User picked option 2 (Random Practice Problems)
    elif user_input == '2':
        user_input = input('Please select from one of the following questions and hit Enter:\n 1) General Form to Standard (Vertext) Form\n 2) Find the Net Change\n 3) Find the Average Rate of Chage\n 4) Determine the End Behavior of the Polynomial Expressed in Arrow Notation\n')
        if user_input == '1':
            while user_input != 'n':
                random_practice_problem1()
                user_input = input('Would you like to try another problem?\n')
            
        elif user_input == '2':
            while user_input != 'n':
                random_practice_problem2()
                user_input = input('Would you like to try another problem?\n')

        elif user_input == '3':
            while user_input != 'n':
                random_practice_problem3()
                user_input = input('Would you like to try another problem?\n')

        elif user_input == '4':
            while user_input != 'n':
                random_practice_problem4()
                user_input = input('Would you like to try another problem?\n')


    # User picked option 3 (Walkthrough Practice Problems)
    elif user_input == '3':
        user_input = input('Please select from one of the following questions and hit Enter:\n 1) General Form to Standard (Vertext) Form\n 2) Find the Net Change\n 3) Find the Average Rate of Chage\n 4) Determine the End Behavior of the Polynomial Expressed in Arrow Notation\n')
        if user_input == '1':
            walkthrough_problem1()
                
        elif user_input == '2':
            walkthrough_problem2()    

        elif user_input == '3':
            walkthrough_problem3()    

        elif user_input == '4':
            walkthrough_problem4()

    # User picked option 4 (Graded Test with a variable number of questions)
    elif user_input == '4':

        # Set up for test
        num_questions = int(input('How many questions would you like in your test?\n'))
        score = 0
        test_question = []
        question_number = 1
        
        #Repeat for however many questions the user specified
        for x in range(num_questions):
            
            #Choose a random question from all possible question
            question_type = random.randint(0,3)

            print(f'Q{question_number}:')
            # Call question type 1
            if question_type == 0:
                # Check if user got question correct
                if random_test_problem1() == 1:
                    score += 1
                    test_question.append(question_number)
                    test_question.append('Correct')
                    

                else: # Assume user got question wrong
                    test_question.append(question_number)
                    test_question.append('Incorrect')
                

            # Call question type 2
            elif question_type == 1:
                if random_test_problem2() == 1:
                    score += 1
                    test_question.append(question_number)
                    test_question.append('Correct')

                else: # Assume user got question wrong
                    test_question.append(question_number)
                    test_question.append('Incorrect')


            # Call question type 3
            elif question_type == 2:
                if random_test_problem3() == 1:
                    score += 1
                    test_question.append(question_number)
                    test_question.append('Correct')

                else: # Assume user got question wrong
                    test_question.append(question_number)
                    test_question.append('Incorrect')
                    
            # Call question type 4
            elif question_type == 3:
                # Check if user got question correct
                if random_test_problem4() == 1:
                    score += 1
                    test_question.append(question_number)
                    test_question.append('Correct')

                else: # Assume user got question wrong
                    test_question.append(question_number)
                    test_question.append('Incorrect')

            # Keep track of the question that the user is on in the test to let them know which questions they got wrong
            question_number += 1

        # Calculate test score
        test_score = (score / num_questions) * 100

        # Show user their overal test score as well as which problems they got wrong, which can be kept track of with the list test_questions
        print(f'Test Score: {test_score:.2f}%')

        # Iterate through test_questions
        count = 0
        count2 = 1
        for x in range (num_questions):
            print(f'Question {test_question[count]}: {test_question[count2]}')
            count += 2
            count2 += 2
        print()
