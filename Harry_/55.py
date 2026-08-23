# rock paper scissor:

try:
    while True:
        user_inp = input(
            "Enter \n\n1 for Rock \t\n\n2 for scissor\t\n\n3 for paper\t\n\n4 for Exiting\t\n\nEnter Your Choice>>>>>>>>>\n"
        )
        if user_inp.isdigit():
            b = int(user_inp)
            if b == 1 or b == 2 or b == 3:
                print("COde till here work")
            elif b == 4:
                print("<<<<<<<<<<<<<See You Next Time>>>>>>>>>>>>>")
                break
            elif b > 4:
                print("Enter Integer as\t\n\n 1 , 2 , 3\t")
except:
    print("<----Restart the Game--->\t")
