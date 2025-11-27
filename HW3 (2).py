def enlist_songs(song_list):
    """
    :param song_list:  a list of songs
    :return:    return a dictionary with empty values
    """
    song_dictionary = {item: {} for item in song_list}    #creates a new dictionary that puts the song name of "song_list" as keys and creates an empty dictionary for each value
    return song_dictionary



def sign_users(user_ratings, song_ratings):         #take user_rating and build a new dictionary
    """
    :param user_ratings:  dictionary of rating for songs keys are  user names
    :param song_ratings:    dictionary of rating for songs keys are songs names
    :return:    update values from user_ratings to song_ratings
    """
    for user, ratings in user_ratings.items():     #user gets the keys value of user_rating , rating gets the values of user_rating whice is a dictionary by itself
         for song, score in ratings.items():        #break down the rating dictionary into a key and value
                if song not in song_ratings:         # add any songs names that are missing
                    song_ratings[song] = {}           #create a new dictionary with songs names
                song_ratings[song][user] = score       #create the final dictionary taking "song" whice is an empty dictionary and putting "user" as key and "score" as value
    return(song_ratings)



def build_vector(song_name, user_list, song_ratings):    #func to give a list of rating from a list of users given to a given song
    """
    :param song_name: name of song
    :param user_list:  list of users
    :param song_ratings:  dictionary of rating for songs keys are  user names
    :return:   build a vector that represents the songs ratings
    """
    song_vector = []
    for i in user_list:
        if i  in  song_ratings[song_name]  :         #we check if the user rated the song and if he did we add the rating
                song_vector.append(song_ratings[song_name][i])
        else:
                song_vector.append(50)              #if the user did not rate the song we add 50 to the rating
    return song_vector




def calculate_euclidian_distance(song_vector, centroid_vector):       #func to measure the distance between a given vector and a centroid vector via a build in math function
    """
    :param song_vector:     song vector
    :param centroid_vector:  center vector
    :return: calculate their euclidian distance via dist func in math
    """
    import math
    distance = math.dist(song_vector, centroid_vector)
    return distance




def calculate_average(song_group, song_ratings, user_list):
    """
    :param song_group:   list of songs
    :param song_ratings:   dictionary of rating for songs keys are  user names
    :param user_list:   list of users in the app
    :return:   return the average rating for each user
    """

    average_vector = [0] * len(user_list)       # create "space" for each user
    songs_length = len(song_group)
    for song in song_group:
        new_vector = build_vector(song, user_list, song_ratings)  #create a vector of each song
        for i in range(len(user_list)):
            average_vector[i] +=  new_vector[i]          #asign the vector
    total_average = []
    for total in average_vector:
        total_average.append(total/songs_length)          #calculate average
    return tuple(total_average)


def k_means(k , user_list , song_ratings, max_iterations):
    """
    :param k:   value of the k_means function
    :param user_list:  list of users
    :param song_ratings:  dictionary of rating for songs keys are  user names
    :param max_iterations:  maximum number of iterations for the algoritem
    :return:         return a dictionary with keys as tuples for the center vectors and values are songs lists for each vector
    """
    import math
    center = []
    songs_list = list(song_ratings.keys())  # crate a list of all songs
    songs_list.sort()
    for i in range(k):               #choose k songs
        song_name = songs_list[i]
        vec = tuple(build_vector(song_name, user_list, song_ratings))      #use func to create a vector and convert to tuple
        center.append(vec)

    for item in range(max_iterations):             #run for the number of iterations given
        clusters = {i: [] for i in range(k)}       #create empty spaces

        for song in songs_list:                  # work trough every song
            song_vec = build_vector(song, user_list, song_ratings)
            best_center = 0
            min_dist = 100000                #we have to define the object so we give it a large value for its to change in the find iteration
            for i in range(k):               #check distance from center
                current_center = center[i]
                d = calculate_euclidian_distance(song_vec, current_center)    #calculate distance
                if d < min_dist:                          # find close center
                    min_dist = d
                    best_center = i

                clusters[best_center].append(song)         # add the song to the center found
            new_centers = []
            for i in range(k):                                # calculate new center
                songs_in_group = clusters[i]

                if len(songs_in_group) > 0:
                    new_center = calculate_average(songs_in_group, song_ratings, user_list)        #calculate average
                    new_centers.append(new_center)
                else:
                    new_centers.append(center[i])
            center = new_centers                              #uptade for next run
        genres_result = {}
        for i in range(k):
            center_tuple = center[i]
            song_list = clusters[i]
            genres_result[center_tuple] = song_list              # crate result
        return genres_result


def represent_user(user, user_ratings, song_ratings,user_list):
    """
    :param user:  name of a user
    :param user_ratings:  dictionary of rating for songs keys are  user names
    :param song_ratings:  dictionary of rating for songs keys are  songs names
    :param user_list:  list of users
    :return:  return a vector that represent the user ratings
    """
    my_ratings = user_ratings[user]       #get rating for the user
    factor = 0
    for score in my_ratings.values():       #calculate distance from 50
        factor += abs(score - 50)
    result_vector = [0] * len(user_list)     #create an empty result vector
    if factor == 0:             #if the user did not rate the song return
        return result_vector
    for song_name , score in my_ratings.items():   #work trough every song and its rating for the user
            song_vector1 = build_vector(song_name, user_list, song_ratings)
            song_vector2 = song_vector1[:]               # create a new object so we do not change the original
            if score < 50:                          # if the score is negative we switch its value
                for i in range(len(song_vector2)):
                    song_vector2[i] = 100 - song_vector2[i]
            a = abs(score - 50) / factor           # calculate via the given functions

            for i in range (len(result_vector)):        #return the new calculated vector
                result_vector[i] += a*song_vector2[i]
    return result_vector

def rate_genres(user, user_ratings, song_ratings, genres):
    """
    :param user:  name of a user
    :param user_ratings:  dictionary of rating for songs keys are  user names
    :param song_ratings:  dictionary of rating for songs keys are  songs names
    :param genres:  dictionary of vectors of the same genre
    :return: return a list of genres that are the closest to the users vector
    """
    user_list = list(user_ratings.keys())
    user_rate = represent_user(user, user_ratings, song_ratings, user_list) #use represent_user to get the user song ratings
    index = []
    for item in genres.keys():
            dist =  calculate_euclidian_distance(user_rate,item)    #calculate the distance between the users vector and each song vector from "genres"
            index.append([dist,genres[item]])    # create a list with the distance and name of the song
    index = sorted(index)     # sort the list from the lowest distance to the largest from the users vector
    final_result = []
    for i in index:        #create a new list with only the song names, that are sorted by order
        name = i[1]
        final_result.append(name)
    return final_result


def recommend_songs(user, user_ratings, song_ratings, user_list,  k):
    """
    :param user:  name of a user
    :param user_ratings:  dictionary of rating for songs keys are  user names
    :param song_ratings:  dictionary of rating for songs keys are  songs names
    :param user_list:  list of users
    :param k:  number of songs to recommend
    :return:   recommend unrated songs for a user given
    """
    index = []
    user_rate = represent_user(user, user_ratings, song_ratings, user_list)  #crete a vector for the users ratings
    if user in user_ratings:
        rated_songs = list(user_ratings[user].keys())     #find out the rated songs
    else:
        rated_songs = []
    for song_name in song_ratings:

        if song_name in rated_songs:       #if the songs is rated already - ignore it
            continue
        vector = build_vector(song_name, user_list, song_ratings)    #use the build vector function to build a vector for the song
        dist = calculate_euclidian_distance(user_rate, vector)
        index.append([dist, song_name])       # create a list of distance is songs name pairs
    result = sorted(index)[:k]           # sort the list from the closest to the farest songs and take only k songs
    final_result = []
    for i in result:
        name = i[1]
        final_result.append(name)       #add only the songs names by order from closest to a final result list
    return final_result

def menu(song_list, user_ratings):
    """
    :param song_list:  list of songs
    :param user_ratings:  dictionary of rating for songs keys are  user names
    :return: acts as a menu that lets the user - add rating , divide to genres , rate genre for a user given , recommend songs for a user given
    """
    song_dic =enlist_songs(song_list)     #calling enlist_songs func
    user_song_ratings = sign_users(user_ratings,song_dic)  #calling sign_users func
    genres_vector = {}

    user_list = list(user_ratings.keys())         # create a list of user names
    choice_str = str("""Choose an option from the following menu:
    (1) Add Rating.
    (2) Divide to Genres.
    (3) Rate Genres for User.
    (4) Recommend Songs for User.
    (5) Exit.
Your choice:
""" )
    while True:
        choice = input(choice_str)      #define a variable for the user input
        if choice == '1':              #if the choice is 1
            add_rating = input("Insert user name, song name and song rating divided by commas:\n")
            add_rating = add_rating.split(',')           #get input and split into a list
            new_user = add_rating[0]                  #save user name into vaible
            new_song = add_rating[1]                 #save song
            new_rating = int(add_rating[2])          # save song rating
            if new_user not in user_ratings:            #add new user if he is not in the list
                user_ratings[new_user] = {}
                user_list.append(new_user)
            user_ratings[new_user][new_song] = new_rating    #update user rating list
            if new_song in user_song_ratings:
                user_song_ratings[new_song][new_user] = new_rating     #update song rating

            pass
        elif choice == '2':
            while True:
                genres_number = int(input("How many Genres would you like to divide the songs to?\n"))     #input for number of genres
                if genres_number >= len(song_list):         #check is the number is valid if not print an error response
                    print("Please insert a number lower than the number of songs on the list." )
                    continue
                genres_vector = k_means(genres_number, user_list, user_song_ratings, 10)     # create genres
                i = 1
                for songs in genres_vector.values():         #print the genres we got
                    print(f"Genre {i}: {songs}")
                    i += 1
                break

        elif choice =='3':
            user_name = input("Insert user name for genre recommendation:\n")     #get user name
            if genres_vector and user_name in user_ratings:
                sorted_genres = rate_genres(user_name, user_ratings, user_song_ratings,genres_vector)    #make sure the genres are calculated and the user is in the list
                i = 1
                for genre in sorted_genres:
                    print(f"#{i}: {genre}")       #print recommendation
                    i += 1

        elif choice == '4':
            rec_song_list = input("Insert user name, and the number of songs divided by commas:\n")    #get the name and number of songs
            rec_song_list = rec_song_list.split(',')
            user_name = rec_song_list[0]         #save name
            k = int(rec_song_list[1])              # save number of songs
            if user_name in user_ratings:      # if user is in the list make song suggestions and print
                rec_list = recommend_songs(user_name, user_ratings, user_song_ratings, user_list,  k)
                print(rec_list)
        elif choice == '5':
            return



if __name__ == "__main__":
    song_list = ['Imagine', 'Hey Jude', 'Bohemian Rhapsody', 'Hotel California', 'Stairway to Heaven']

    user_ratings = {
        'Alice': {'Imagine': 70, 'Hey Jude': 40, 'Stairway to Heaven': 90},
        'Bob': {'Bohemian Rhapsody': 30, 'Hotel California': 60, 'Stairway to Heaven': 75},
        'Charlie': {'Stairway to Heaven': 10, 'Imagine': 100, 'Hey Jude': 40},
        'Diana': {'Hey Jude': 20, 'Bohemian Rhapsody': 40, 'Hotel California': 70},
        'Eve': {'Hotel California': 50, 'Stairway to Heaven': 80, 'Imagine': 20}
    }

    menu(song_list, user_ratings)
