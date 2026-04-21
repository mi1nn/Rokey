# week.py

week = input("월요일부터 일요일 중 영어로 번역하고 싶은 요일을 입력하세요")

# if "월" in week  가능
# if week == ("월요일" or "월")  불가능


if week == '월요일':
    week = 'Monday'
    print(week)
elif week == '화요일':
    week = 'Tuesday'
    print(week)
elif week == '수요일':
    week = 'Wednesday'
    print(week)
elif week == '목요일':
    week = 'Thursday'
    print(week)
elif week == '금요일':
    week = 'Friday'
    print(week)
elif week == '토요일':
    week = 'Saturday'
    print(week)
elif week == '일요일':
    week = 'Sunday'
    print(week)
else:
    print('요일을 잘못 입력함')
print('if 문 끝')


# in -> 포함되어 있는 지 확인
# 값 in 자료항 -> True or False
