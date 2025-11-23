# ************************ HOMEWORK 1 QUESTION 3 ************************
def question_3(input_list, z):
    spectacular = False
    ####################
    # WRITE_CODE_HERE
    dividable = 0                   # create objects to count and sum of the dividable and not dividable numbers by in z from the list
    not_dividable = 0
    for sum_num in input_list:     #create sum_num object that checks every number on the list "input_list" in the loop
        if sum_num % z == 0:         # if the number is dividable by z we sum the number to the counter object "dividable"
            dividable += sum_num
        elif  sum_num % z != 0:      # if the number is not dividable by z we sum the number to the counter object "not_dividable"
            not_dividable += sum_num
    if dividable == not_dividable:   #compare the two objects to see  if the list is spectacular or not
        spectacular = True
        print(spectacular)
    else:
        spectacular = False
        print(spectacular)


    # DO NOT EDIT THE CODE AFTER THIS LINE.
    ####################
    return spectacular



