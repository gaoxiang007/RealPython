import sys
import pdb
from random import choice

random1 = [1,2,3,4,5,6,7,8,9,10,11,12]
random2 = [1,2,3,4,5,6,7,8,9,10,11,12]


while True:
    print "To exit this game type 'exit'"
    #pdb.set_trace()
    num1 = choice(random2)
    num2 = choice(random1)
    answer = raw_input("What is {} time {}?".format(num1, num2))
    # exit
    if answer == "exit":
        print "Now exiting game!"
        sys.exit()


    # determine if number is correct
    elif int(answer) == num1 * num2:
        print "Correct!"
        break
    else:
        print "Wrong!"
