# string1.py

muna = "python"
print(muna[0])
print(muna[1])
print(muna[2])
print(type(muna))

try:
    muna[0] = 'k'   # TypeError
except TypeError as e:
    print(type(e), e)
    
munb = ["python"]
print(munb[0])
print(type(munb))

munc = ["p", "y", "t", "h", "o", "n"]
print(munc[0])
print(munc[1])
print(munc[2])
print(type(munc))
munc[0] = 'k'
print(munc)

print('----------------------')
for i in range(0, 6, 1):
    print(munc[i], end = " ")
    
length = len(munc)
print(length)
for i in range(0, len(munc), 1):
    print(munc[i], end = " ")
print()

print('----------------------')
print(ord("A"))  # 인코딩
print(ord("a"))  # 아스키코드 숫자로 반환
print(chr(67))   # 디코딩
print(chr(99))

print(ord("가"))
print(chr(44033))

print('----------------------')
ma = "ChatGPT" + "를 활용한 Python"
print(ma)
print(type(ma))

# 기본 형식
name = '홍길동'
age = 52
print("name: ", name, "age: ", age)

# 1. % 연산자 사용 방식
# %s: 문자열, %d: 정수, %f: 실수
print("이름: %s 나이: %d"%(name, age))

# 2. format() 메서드 사용법
print("이름: {} 나이: {}".format(name, age))

# 3. f-string 사용 방식
print(f"이름: {name} 나이: {age}")

# 소수점 자리수 맞추기
pi = 3.141592
print(f"파이: {pi}")
print(f"파이: {pi:.2f}")

print('----------------------')
# 슬라이싱
# 변수명[시장인덱스:끝인덱스-1:건너뛰기]
muna = "python"
print(muna[0:6])
print(muna[:])
print(muna[0:])
print(muna[:6])

print(muna[-3:])  # hon
print(muna[2:-2])  # th