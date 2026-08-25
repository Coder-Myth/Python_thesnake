# rock paper scissor:
import random

try:
    while True:
        user_inp = input(
            "Enter \n1 for Rock \t\n2 for scissor\t\n3 for paper\t\n4 for Exiting\t\nEnter Your Choice>>>>>>>>>\n"
        )
        if user_inp.isdigit():
            b = int(user_inp)
            if b == 1 or b == 2 or b == 3:
                r = random.randint(1, 3)
                # for rock as input
                if r == 1 and b == 1:
                    print("Draw\n\n")
                elif r == 1 and b == 2:
                    print("Win\n\n")
                elif r == 1 and b == 3:
                    print("Lose\n\n")
                # for scissor as input
                if r == 2 and b == 1:
                    print("Lose\n\n")
                elif r == 2 and b == 2:
                    print("Win\n\n")
                elif r == 2 and b == 3:
                    print("Draw\n\n")
                # for paper as input
                if r == 3 and b == 1:
                    print("Win\n\n")
                elif r == 3 and b == 2:
                    print("Lose\n\n")
                elif r == 3 and b == 3:
                    print("Draw\n\n")
            elif b == 4:
                print("<<<<<<<<<<<<<See You Next Time>>>>>>>>>>>>>")
                break
            elif b > 4:
                print("Enter Integer as\t\n\n 1 , 2 , 3\t")

except:
    print("<----Restart the Game--->\t")


# input      1  2   3
# rock    1  D  W   L
# scissor 2  L  D   W
# paper   3  W  L   D


# the cleaner way for this is to make logic instead of the using numbers just like b==r i.e. draw then the three case in which i win keep them in or and use else to get other outputs

#  give your output to ai and then see what are the mistake if it could be the professional generate the code by youself first
