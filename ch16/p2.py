# p2.py

# 문제1. 괄호 짝 검사
# 기능: 문자열에 포함된 괄호의 짝이 올바르게 사용되었는지 확인, 스택 사용
# 입력: 문자열
# 반환: True -> 짝 맞음, False -> 짝 안맞음

# 1. 괄호를 담을 빈 스택을 생성
# 2. 문자열 내 문자를 가져옴
# 3. 만약, 문자가 "시작" 괄호라면 스택에 push
# 4. 문자를 순차적으로 확인하다가 "종료" 괄호가 있다면 스택에서 pop
#    4-1. 만약, 스택ㅇ 비었다면(매칭되는 시작괄호 없음) -> False
#    4-2. pop한 관호를 확인했는데 서로 일치하지 않음 -> False
# 5. 동일한 괄호가 새로 매칭되면 스택의 괄호를 제거
# 6. 스택이 더 있다면 True(짝 맞음)

# def check_bracket(text):
    
#     stack = []  # 1. 빈 스택 생성
    
#     for chat in text:   # 2. 문자열 내 문자 가져옴
#         # print(char)
#         # char "("   # 3. "시작" 괄호라면 스택 push
#         # char ")"   # 4. "종료" 괄호라면 스택 pop
        
#         stack.append()
#         top = stack.pop()
        
        
#     if :
#         return False   # 짝이 안맞음
#     return True   # 짝이 맞음

# 함수("(a+b)")

def check_bracket(text):
    stack = []
    
    for char in text:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()

    if (char == ")" and top != "(") or \
        (char == "}" and top != "{") or \
        (char == "]" and top != "["):
        return False   # 짝이 안 맞음
    return len(stack) == 0    # 6. 스택이 비었다면 짝 맞음

print(check_bracket("(a+b)"))
print(check_bracket("(a+b)]}"))
print(check_bracket("[{x + y} + 3] - 4"))
