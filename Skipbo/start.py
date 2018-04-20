import sys

prompt = '>>'
count = 5

decksize = 0

skipbonum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]
skipsize = len(skipbonum)
skipsize = skipsize - 1
firstuserhand = []
firstsize = len(firstuserhand)
firstsize = firstsize - 1
seconduserhand = []
secondsize = len(seconduserhand)
secondsize = secondsize - 1
firstuserdeck = []
firstdsize = len(firstuserdeck)
firstdsize = firstdsize - 1
seconduserdeck = []
seconddsize = len(seconduserdeck)
seconddsize = seconddsize - 1

print "Welcome to the game of Skipbo"
print len(skipbonum)
print skipsize
print "Ready to play? (yes or no)"
play = raw_input(prompt)

def pull (count, handdeck):
    i = 0
    while i < count:
        from random import randint
        justsex = randint(0, skipsize)
        handdeck.append(skipbonum[justsex])
        varr = int(justsex)
        skipbonum.pop(varr)
        i = i + 1
        
#def hand (count, userhand):
#    count = 5
#    pull(count, userhand)
    

if play == "yes":
    print "You chose to play!"
    print "Dick Size?"
    decksize = raw_input(prompt)
    pull(count, firstuserhand)
    pull(decksize, firstuserdeck)
    pull(decksize, seconduserdeck)
    index = 0
    while i < 6:
        sys.stdout.write(firstuserhand[index])
        index += 1

if play == "no":
    print "You chose not to play!"

for number in firstuserhand:
    print number


#from random import randint
#firstuser.append(randint(0,161))
#for number in firstuser:
#print "Array Number: %d" % number
#print "Card: ", firstuser[0]
