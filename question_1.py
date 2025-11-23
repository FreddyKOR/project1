# ************************ HOMEWORK 1 QUESTION 1 ************************
def question_1(a, x):
    y = 3.141414
    ####################
    # WRITE_CODE_HERE


    y = a**2 + x**2     # we break the formula into 3 parts and calculate the value of y after each step
    y = y /((x%4)+1)
    y = y*(a**(x%5))

    y=round(y,2)          #we get the result of y from the formula and round the number to 2 digits after the dot, before we print and return the result
    print (y)









    # DO NOT EDIT THE CODE AFTER THIS LINE.
    ####################
    return y

