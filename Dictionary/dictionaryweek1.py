#ASGN 1
#Design a dictionary whose keys describe what values you'd like to
# learn about your peers in this class. Design the dictionary on paper,
# specifying the data type of the value.


#create an empty list
list=[]

#get the number of people
num=int(input('How many people will do this survey? '))

#loop
for i in range(0,num):
    info = {}
    user_name = input("\n what's your name?")
    info['Name'] =user_name

    movie_name = input("\n what's your favorite movie? ")
    info['Movie'] = str(movie_name)

    movie_genre = input("\n what's the genre of this movie ")
    info['Genre'] = movie_genre

    movie_actor = input("\n what's your favorite actor in this movie")
    info['Actor'] = movie_actor

    #add each person's information to the list
    list.append(info)

#display
print('-------------Movie Survey-------------')
print('There are ',num,' people do this survey')

for x in range (0,len(list)):
    print(list[x])











