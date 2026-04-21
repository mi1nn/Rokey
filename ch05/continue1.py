# continue1.py

count = 0
while count < 3:
    count += 1
    if count == 2:
        continue
    print(count)
print('while 문 종료')

print('-------------------------')

# 필터링 예제
users = ['admin', 'user', 'guest', '', None]

for user in users:
    if not user:
        continue
    print(user)
print('종료')  # 빈 값과 None은 안 나오고 유효한 데이터만 처리됨