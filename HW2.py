def print_schedule(schedules, train_directions):
    """Pretty-print a schedule matrix of (arrival, departure) tuples with train directions."""
    if not schedules:
        print("Empty schedule matrix.")
        return

    if train_directions is None:
        train_directions = ['ltr'] * len(schedules)

    print("Train Schedules:")
    for i, train in enumerate(schedules):
        direction = train_directions[i]
        row = []
        for arr, dep in train:
            if arr < 0:
                row.append("(-,-)")
            else:
                row.append(f"({arr},{dep})")
        print(f"Train {i} [{direction}]: " + "  ".join(row))
    print()


def add_train_station(schedules, station_index):       #func to check i the station index is valid and add a new station
    '''

    :param schedules:  time schedule of the trains
    :param station_index: represent the number of the new station we want to add
    :return:  check if the station_index is valid and if it is add a new station it the number it represents
    '''
    num_of_stations = len(schedules[0])
    if station_index  <0 or station_index >= (num_of_stations):
        pass
    else:
        for station in schedules:
            station.insert(station_index,(-1,-1))
        print (schedules)
        pass
#add_train_station(([(0, 5), (10, 15), (20, 25)],
    #[(2, 7), (12, 17), (22, 27)],[(22,55)]), 0)



def remove_train_station(schedules, station_index):     #func to check if the station index ix valid and remove a station at the index it represents
    """

    :param schedules:    time schedule of the trains
    :param station_index:  represent the number of the new station we want to add
    :return:    check is the station_index is valid and if it is remove the station at the number it represents
    """
    num_of_stations = len(schedules[0])
    if station_index < 0 or station_index >= (num_of_stations):
        pass
    else:
        for station in schedules:
            station.pop(station_index)
        print (schedules)
        pass
#remove_train_station(([(0, 5), (10, 15), (20, 25)],
    #[(2, 7), (12, 17), (22, 27)],[(22,55)]), 0)


def split_schedule(schedules, train_directions, train_index, split_station):  #func to split a station into 2 at a given station index and train index
    """
    :param schedules:    time schedule of the trains
    :param train_directions:  direction of the train ordered by index
    :param train_index:    train index to split into two
    :param split_station:  station of index where we split
    :return: check is the train index and split station values are valid and return a list after we split the station into 2 and the split station index
    """
    if train_index >= len(schedules) or train_index < 0:
        return
    if  split_station >= len(schedules[train_index]) or split_station <= 0:
        return
    else:
        start_schedule = schedules[train_index]
        first_part = start_schedule[:split_station] + [(-1, -1)] * (len(start_schedule) - split_station)
        second_part = [(-1, -1)] * split_station + start_schedule[split_station:]
        schedules[train_index] = first_part
        schedules.insert(train_index + 1, second_part)
        train_directions.insert(train_index + 1,train_directions[train_index])
    print (schedules)
    print (train_directions)
    pass
#split_schedule([[(0, 5), (10, 15), (20, 25)], [(2, 7), (12, 17), (22, 27)]], ['ltr', 'rtl'],0,2)


def reverse_train(schedules, train_directions, train_index=0):    #func to reverse the station order and direction at a given index
    """
    :param schedules:  time schedule of the trains
    :param train_directions: direction of the train ordered by index
    :param train_index:   train index to reverse the stations
    :return:   check if train index valid and reverse the stations order at the intended index, also reverse the train direction at the corresponding index
    """
    if train_index >= len(schedules) or train_index < 0:
        return
    else:
        schedules[train_index] = schedules[train_index][::-1]
        if train_directions[train_index] == 'ltr':
            train_directions[train_index] = "rtl"
        elif train_directions[train_index] == 'rtl':
            train_directions[train_index] = "ltr"
    print(schedules)
    print(train_directions)
    pass
#reverse_train([[(0, 5), (10, 15), (20, 25)], [(2, 7), (12, 17), (22, 27)]], ['ltr', 'rtl'])



def find_conflicts(schedules):
    """
    :param schedules:  time schedule of the trains
    :return:  check if any train arrives to a station before another train leaves the station and if so add the index of each train and the station
    of the crash to a new object - conflicts
    """
    conflicts = []
    for train_index_a in range(len(schedules)):
        for train_index_b in range(train_index_a + 1,len(schedules)):
            train_a = schedules[train_index_a]
            train_b = schedules[train_index_b]
            for station_index in range(len(train_a)):       # split the stations tupls into a start and an end
                a_start, a_end = train_a[station_index]
                b_start, b_end = train_b[station_index]

                if not(a_end < b_start or b_end < a_start):    #check if a train arrive to a station before another train leaves
                    conflicts.append((train_index_a, train_index_b, station_index))
    return conflicts
    print (conflicts)
#find_conflicts ([[(0, 5), (10, 15), (20, 25)], [(2, 7), (12, 17), (22, 27)], [(0, 3), (16, 18), (30, 35)]])

def delay_train(train_schedule, start_station, delay, direction='ltr'):
    """"
    :param train_schedule: time schedule of the trains
    :param start_station:  station of index from where we want to start delaying
    :param delay: time delay
    :param direction:  direction of delay
    :return:  return the train schedule after delay from the start_station index in the direction given
    """
    if direction == 'ltr':      # check if the delay if from right to left or left to right
            for station in range(start_station ,len(train_schedule)):
                arrival, departure = train_schedule[station]
                train_schedule[station] = (arrival + delay, departure + delay)     #add the delay to each object in the station tuple

            #print (train_schedule)
    pass
    if direction == 'rtl':
            for station in range(start_station,-1,-1):
                arrival, departure = train_schedule[station]
                train_schedule[station] = (arrival + delay, departure + delay)

            #print (train_schedule)
    return train_schedule
#delay_train([(2, 7), (17, 22), (27, 32)],2,3,"rtl")


def resolve_conflicts(schedules, train_directions, delay=5):
    """
    :param schedules: time schedule of the trains
    :param train_directions:  direction of the train ordered by index
    :param delay:  delay time
    :return: the func used "conflicts" function to look at the crashing train and uses "delay_train" to delay the train arrivale times
    the func runs until "conflicts" indicates there are no more crashing trains and returns i new train schedule list ,
     we also get a count down of the number of delays we add to apple via the "total_fixed" object
    """
    total_fixed = 0
    conflicts = find_conflicts(schedules)     # check if we get conflicts before we start running
    while  len(conflicts) > 0:              #we want to run as long as we have crashing trains
        minimal_conflict = conflicts[0]              #run from the first station by order
        for min1 in conflicts[1:]:
            if min1 < minimal_conflict:
                minimal_conflict = min1

        total_fixed += 1                       # count with each delay we make
        a_index, b_index, station = minimal_conflict
        delay_train(schedules[a_index], station, delay, train_directions[a_index])
        conflicts = find_conflicts(schedules)
    print (schedules)
    print (total_fixed)
    return schedules , total_fixed
#resolve_conflicts([[(0, 5), (10, 15), (20, 25)], [(22, 27), (12, 17), (2, 7)], [(30, 35), (16, 18), (0, 3)]]
#,['ltr', 'rtl', 'rtl'] ,5)



