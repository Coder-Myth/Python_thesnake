# kbc : create a program that asks you questions and tells you marks accordingly

questions = ["2+4", "16*2", "4/2"]

answer = []

for i in range(0, len(questions)):
    indexing = questions[i]
    print(indexing)
    answer.append(int(input("Enter Your Answer:")))

 
