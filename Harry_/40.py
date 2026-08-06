# excercise 4solution

task = input("1. Code \n\n2. Decode\n\nENTER YOUR CHOICE>>>>>>>>>>>")

if not task.isdigit():
    raise ValueError("Invalid input")

elif task.isdigit():
    task = int(task)
    try:
        if task == 1:
            pass
 