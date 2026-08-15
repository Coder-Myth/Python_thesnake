"""
# excercise 2 ( code with harry )
# excercise 4solution

# code decode : instructions given
# length word = less than 3 than print word
# more than 3 word append first alphabet at the last


task = input("1. Code \n\n2. Decode\n\nENTER YOUR CHOICE>>>>>>>>>>>")

if not task.isdigit():
    raise ValueError("Invalid input")

elif task.isdigit():
    task = int(task)

    try:
        if task == 1:
            word = input("Enter Your Message:")
            if len(word) < 3:
                print(word)
            else:
                first_alphabet=word[0]
                for i in range(1, len(word)):
                    # store this word into list each word in list then append then first word at last and then gain we will print output
                        print(word[i],end="")
                print(first_alphabet)

        elif task == 2:
            print(
                "1. word less than 3 words reversed\n\n 2. atleast or more than three words \n (a)fisrt word at the last and three random modules present at the end ans well as front "
            )

    except:
        print("Enter 1 or 2 as your integer:")

"""

# another method  :

task = int(input("1. Code \n\n2. Decode\n\nENTER YOUR CHOICE>>>>>>>>>>>"))

if task == 1:
        message = input("Enter Your Message :")
    for words in message.split(): 
