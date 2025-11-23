# ************************ HOMEWORK 1 QUESTION 2 ************************
def question_2(room_number, elevator_side, room_size):
    ice_cream_per_hour = -1
    ####################
    # WRITE_CODE_HERE
    room_number = int(room_number)
    ice_cream_per_hour = 0
    if room_size == "small":      #we start by checking if the room size is small because a small room gives 0 ice cream
        ice_cream_per_hour = 0
        print (ice_cream_per_hour)
    elif room_number > 400 :           #we check the room number and add the ice cream pace
        ice_cream_per_hour = 1

    elif room_number < 100 :
        ice_cream_per_hour = 0.1

    else:                           # else means the room size is between 100 and 400
        ice_cream_per_hour = 2.25




    if room_size == "medium" :      # in case the room is medium we continue to check the other conditions
        if room_number % 2 == 1:
            ice_cream_per_hour = ice_cream_per_hour + 0
            print(ice_cream_per_hour)
        elif elevator_side == "right":
            ice_cream_per_hour = ice_cream_per_hour + 2
            print(ice_cream_per_hour)
        elif  elevator_side == "left" and room_number % 2 == 0:     # check is the room number is even
            ice_cream_per_hour = ice_cream_per_hour +1
            print(ice_cream_per_hour)
    if room_size == "large":      #in case the room is large we continue to check the other conditions
        if elevator_side == "right":
            ice_cream_per_hour = ice_cream_per_hour +1
            print(ice_cream_per_hour)
        elif elevator_side == "left" and room_number % 2 == 1:       # check if the room number is odd
            ice_cream_per_hour = ice_cream_per_hour + 0.1
            print(ice_cream_per_hour)
        elif elevator_side == "left" and room_number % 2 == 0:       #check if the room number is even
            ice_cream_per_hour = ice_cream_per_hour +0.25
            print(ice_cream_per_hour)

    # DO NOT EDIT THE CODE AFTER THIS LINE.
    ####################
    return ice_cream_per_hour







