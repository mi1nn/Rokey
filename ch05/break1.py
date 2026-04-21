# break1.py

count = 0
while count < 3:
    # count = count + 3
    count += 3
    if count == 2: 
        break
    print(count)

print('------------------------')

# 원하는 값을 찾으면 종료하는 예제
users = ['Kim', 'lee', 'park']

for user in users:
    if user == 'lee':
        print('Found')
        break
print('Finished')

# 찾으면 탐색 중지 -> 성능 절약
while True: 
    cmd = input('프롬프트> ')
    if cmd == 'pythone':
        print('파이썬 프로그램 실행')
    elif cmd == 'exit':
        print('터미널 종료')
        break

