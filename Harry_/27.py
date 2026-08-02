#kbc : create a program that asks you questions and tells you marks accordingly

questions= ["2+4", "If time is 12:00PM will it morning or afternoon", "4/2"]

for i in range(0, len(questions)):
    indexing=questions[i]
    print(indexing)
    ans1=input("Enter Your Answer:")
    final_score=0
    if(ans1==6):
        final_score+=1
    else:
        final_score=0
     