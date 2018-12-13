'''
Created on Apr 10, 2017

@author: Bhavin Soni
partner: Aaron John

pledge: I pledge my honor that I have abided by the Stevens Honor System
'''
TXT_FILE = "musicrecplus.txt"

def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

def getPreferences(userName, userMap):
    ''' Returns a list of the uesr's preferred artists.
        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("Welcome back ", userName,'! \n We see you have used this system before.')
        print("Your music preferences are the following:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you like.")
        newPref = input("Press Enter once you are done: ")
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: " )
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        newPref = input("like, or just press Enter: ")
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

def currentPreferences(userName, userMap):
    '''prints out the current preferences of the user'''
    if userName in userMap:
        preferences = userMap[userName] #Lists the preferences for the current user
    else:
        preferences = [] 
        print("ERROR : Sorry this user was not found in our data.") #if preferences are empty or if user name is not in user map then return error
    return preferences

def getRecommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations

def recommend(userName, prefs, userMap):
    '''recommendation function that helps display the recommendations for that user'''
    recommendation = getRecommendations(userName, prefs, userMap) #since getRecommendations is a list we will just assign it to recommend 
    if len(recommendation) == 0: # if there are no recommendations then print message
        print('We do NOT have any recommendations for you at the moment. Sorry! \n Once we get more users we will hook you up.')
    else:
        print('By analyzing our current users, we believe you may also like these artists: ')
        for artist in recommendation: #if there are artists by other artists print the artists to recommend
            print(artist)
    
    print('For your convenience we will save the artists you prefer.') #saved it in the main function below
    saveUserPreferences(userName, prefs, userMap, TXT_FILE)

def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, "w") 
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                    "\n"
        file.write(toSave)
    file.close()
    
def show_most_popular():
    """displays the most popular artist amongst the users"""
    Dict = {}
    userMap = loadUsers(TXT_FILE) #userMap is the users saved in the file
    most_likes = 0 #initialize the most likes as 0
    z = "" #the artist name
    for i in userMap: #for every user i in the dictionary 
        prefs = userMap[i]
        for j in prefs: #for every preference j associated with the user i  
            Dict[j] = 0 #initialize the preference dictionary at 0. it will be used as the counter for most popular 
    
    for i in userMap:
        prefs = userMap[i]
        for j in prefs:
            Dict[j] = Dict[j] + 1 #same thing as above but now counts the similar artists up by 1
    
    for k in Dict:
        if Dict[k] > most_likes:
            most_likes = Dict[k] #for every k artists in the dictionary counted is greater than the most like then that value becomes the new dict[k]
            z = k #now the most popular artist is the z
    print("Most Popular Artist: " + z) 
    for k in Dict:
        if Dict[k] == most_likes and k != z: #if there is another popular artist, and its not the same as z then print that one as well
            print("Other Popular Artists:  " + k)

def how_popular_is_popular():
    '''displays how popular is the most popular'''
    Dict = {}
    userMap = loadUsers(TXT_FILE)
    popular = 0
    x = ''
    #literally the same code as above with same explanations but this just prints the number
    for i in userMap:
        prefs = userMap[i]
        for j in prefs:
            Dict[j] = 0
    for i in userMap:
        prefs = userMap[i]
        for j in prefs:
            Dict[j] += 1
    for k in Dict:
        if Dict[k] > popular:
            popular = Dict[k] #popular = the maximum number of likes
            x = k 
    print('Artist with most popular likes is: ', x ,'with ', str(popular), 'likes.')#str(popular) because popular is a number so make it into a string 
    

def most_user_likes():
    """Prints the user with the most likes with the number of likes"""
    Dict = {} #initialize empty dictionary
    likes = 0 #initialize likes as 0
    user = "" #initialize user as empty string
    userMap = loadUsers(TXT_FILE) #all the users saved
    for i in userMap: #for all users i in usermap
        prefs = userMap[i] #preferences for the users i
        Dict[i] = len(prefs) #takes the length of the artists that each user likes - integer 
    for j in Dict: #for artists by user j in the dict
        if Dict[j] > likes and j[-1] != "$": #for the user with most likes that is greater than 0 and does not have $ at the end of its name likes is the new user with most likes and set that equal to j
            likes = Dict[j] 
            user = j
    print("User with most likes is " + user + " and has " + str(likes) + " likes.")
    print("This user's preferences are: ")
    print(currentPreferences(user, userMap))
    print('The total amount of preferences this user has is: ')
    print(len(currentPreferences(user, userMap)))

    for j in Dict:
        if Dict[j] == likes and j != user and user[-1] != "$": 
            print("Another user with the most likes is " + user + " with " + str(likes) + " likes")
            
def main():
    '''displays the menu and lets the user choose option.'''
    x = True
    
    userMap = loadUsers(TXT_FILE)
    print("Welcome to the Music Recommender system!")

    userName = input("Please enter your name. If you would like to opt-out of the program \n please enter a '$' at the end of your name \n so that your name and preferences are not saved: ")
    
    print ('Hello', userName)
    
    while(x):
        menu = "Please enter a letter to choose an option:\n\
            e - enter preferences\n\
            r - get recommendations\n\
            p - show most popular artists\n\
            h - how popular is the most popular\n\
            m - which user has the most likes\n\
            q - save and quit\n"
       
        y = input(menu) #prints menu and lets user choose option

        if y =="e":
            prefs = getPreferences(userName, userMap) #prints preferences if saved previously
            saveUserPreferences(userName, prefs, userMap, TXT_FILE)
        
        elif y =="r":
            prefs = currentPreferences(userName, userMap) #prints current preferences if saved before
            recommend(userName, prefs, userMap)
            
        elif y =="p":
            show_most_popular() #shows most popular artist
        elif y =="h":
            how_popular_is_popular() #shows how popular the most popular artist is
        elif y =="m":
            most_user_likes() #shows which user has the most likes
        elif y =="q":
            print("Saving...Peace")
            x = False
        else:
            print("ERROR: Invalid Option. Please choose one of the options in the menu.")

            
if __name__ == "__main__": 
    main()
