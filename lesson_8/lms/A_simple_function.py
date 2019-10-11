# Create a simple function called favourite_movie, which takes a string
# containing the name of your favourite movie. The function should then
# print “My favourite movie is name”.

def favourite_movie(name):
    print(f'My favourite movie is {name}.')

user = input('Enter the name of your favourite movie: ')

favourite_movie(user)