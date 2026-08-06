# excercise 4solution

task = input("1. Code \n\n2. Decode\n\nENTER YOUR CHOICE>>>>>>>>>>>")

if not task.isdigit():
    raise ValueError("Invalid input")

elif task.isdigit():
    task = int(task)
    try:
        if task == 1:
            pass
        elif(task ==2):
            print(
                "1. word less than 3 words reversed\n\n 2. atleast or more than three words \n (a)fisrt word at the last and three random modules present at the end ans well as front "
            )
    except:
        print("Enter 1 or 2 as your integer:")
