#블러오기
import datetime

#오늘 날짜 가져오기
today = datetime.datetime.now()



#출력하기
if today.weekday() in [5,6]:
    print("주말이므로 회사에 가지 않습니다.")

else:
    print("자~ 일어나서 회사 갑시다.")    
