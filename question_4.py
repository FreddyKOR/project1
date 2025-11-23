# ************************ HOMEWORK 1 QUESTION 4 ************************
def question_4(input_list):
    ####################
    # WRITE_CODE_HERE


        check_sort = False
        while not check_sort:      #loop to continue running the list
            check_sort = True
            i = 0
            while i+1 < len(input_list):      # run the length of the list
                if input_list[i] > input_list[i+1]:           # if an object is smaller than the object after it we run the loop
                    input_list[i+1],input_list[i] = input_list[i], input_list[i+1]        #swap places
                    check_sort = False
                i = i + 1
        print (input_list)


    # DO NOT EDIT THE CODE AFTER THIS LINE.
    ####################

        return input_list
