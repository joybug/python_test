#1부터 10까지 루프
print("----------------1부터 10까지 루프")
for i in range(1,11):
    print(i)

#구구단
print("----------------구구단")
for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)




userInput = input("멈추려면 STOP를 입력하세요 : ").upper().strip()

while userInput != "STOP":
    userInput = input("멈추려면 STOP를 입력하세요 : ").upper().strip()
