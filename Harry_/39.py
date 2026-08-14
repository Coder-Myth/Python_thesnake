# kbc excercise solution 

# kbc : create a program that asks you questions and tells you marks accordingly

questions = ["2+4", "16*2", "4/2"]

answer = []#stores answer to check 

for i in range(0, len(questions)):
    indexing = questions[i]
    print(indexing)
    answer.append(int(input("Enter Your Answer:")))

score = [] #keeps score for each of the question

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

# print(score)
# print(answer)

# sum of a list
final_score = 0
for k in range(0, len(score)):
    score_for_each = score[k]
    final_score = final_score + score_for_each

#final score
print(f"Your Final Score is : {final_score}")
