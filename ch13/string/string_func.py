# string_func.py

# 함수 사용 시 확인할 내용
# 1. 기능 / 동작
# 2. 매개변수
# 3. 반환값

# 문자열.split()
# 1. 기능 / 동작: 구분자 기준 분리
# 2. 매개변수: 구분자
# 3. 반환값: 구분된 문자열 -> list

my_string = "Python is a popular language"
# split_list = my_string.split(" ")
split_list = my_string.split()
print(split_list)
print(split_list[4])

# 이스케이프 코드: 사전 정의된 문자 조합
# "\n": new line = LF(line feed)
# "\t": tab
# "\b": backspace
# "\'": 작은 따옴표
# "\"": 큰 따옴표
# "\\": 역슬래쉬 표시
# "\r": CR(carriage return) 커서를 현재 줄 가장 앞으로 이동

print("hello\t \"greet\" wordl!", end = "\n")
print("abcde\bthanks!", end = "\r")
print("hi")

print('------------------------------')

# "구분자".strip(문자열집합)
# 1. 기능 / 동작: 문자열 양 끝 공백문자를 제거
# 2. 매개변수: 제거할 문자(생략 시 공백)
# 3. 반환값: 수정된 문자열 -> str

my_string = "\t Python is awesome!  \n "
print(my_string)
stripped_string = my_string.strip()
print(stripped_string)

print('------------------------------')

# "문자열".join()
# 1. 기능 / 동작: iterable 의 요소들을 문자열로 연결
# 2. 매개변수: iterable(문자열 요소 집합)
# 3. 반환값: 연결된 문자열 -> str

my_list = ["apple", "banana", "cherry"]
joined_string = " - ".join(my_list)
print(joined_string)