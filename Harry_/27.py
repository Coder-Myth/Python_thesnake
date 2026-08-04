# kbc : create a program that asks you questions and tells you marks accordingly

questions = ["2+4", "16*2", "4/2"]

answer = []

for i in range(0, len(questions)):
    indexing = questions[i]
    print(indexing)
    answer.append(int(input("Enter Your Answer:")))

 
score = []

for j in range(0, len(answer)):
    check_answer = answer[j]
    if j == 0 and check_answer == 6:
        score.append(1)
            elif j == 1 and check_answer == 32:
        score.append(1)
    elif j == 2 and check_answer == 2:
        score.append(1)
    else:
        score.append(0)
    # print(check_answer)
 
 
