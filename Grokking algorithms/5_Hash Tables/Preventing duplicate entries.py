# Suppose you’re running a voting booth. 
# Naturally, every person can vote just once. 
# How do you make sure they haven’t voted before? 
# When someone comes in to vote, you ask for their full name. 
# Then you check it against the list of people who have voted.
# If their name is on the list, this person has already voted—kick them out! 
# Otherwise, you add their name to the list and let them vote. 

# make a hash to keep track of the people who have voted:
voted = {}
# When someone new comes in to vote, 
# check if they’re already in the hash:

def check_voter(name):
    if voted.get(name):
        print("kick them out !")
    else:
        voted[name] = True
        print("let them vote!")


check_voter("Quang")
print(voted)
check_voter("Mr.H")
print(voted)
check_voter("Mr.D")
print(voted)
check_voter("Quang")