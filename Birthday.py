import datetime

year = input("테어난 해는 언제인가요?")
month = input("테어난 달은 언제인가요?")
day = input("테어난 날은 언제인가요?")

year = int(year)
month = int(month)
day = int(day)

bday = datetime.datetime(year,month,day)

if bday.weekday() == 6:
    dow = "일"
elif bday.weekday() == 5:
    dow = "토"
elif bday.weekday() == 4:
    dow = "금"
elif bday.weekday() == 3:
    dow = "목"
elif bday.weekday() == 2:    
    dow = "수"
elif bday.weekday() == 1:
    dow = "화"
elif bday.weekday() == 0:
    dow = "월"

print("태어난 날은",dow,"요일이군요.")   