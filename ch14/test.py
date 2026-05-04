# import re
# pattern = r'\w+'
# text = "Hello, World!"
# print(re.findall(pattern, text))

# import re
# pattern = r'(ab)+'
# text = "ababab"
# match = re.match(pattern, text)
# print(match.group())

# import re
# text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"
# emails = re.findall(r'\b[\w\.-]+-[\w\.-]+-\w+\b', text)
# print(emails)

# import re
# text = "I love Python. Java is also popular. Python is great for AI."
# result = re.findall(r'[^.]*Python[^.]*', text)
# print(result)

# import re
# text = "상품 코드: A123, B456, C789, 가격: 12000원"

# # 문자열에서 숫자만 추출해 리스트로 반환
# number = re.findall(r'\d+', text)
# print(number)

# import re
# text = "NASA is working on AI projects with IBM and Google."
# # 연속된 대문자만 찾아 리스트 반환
# capital = re.findall(r'\b[A-Z]{2,}\b', text)
# print(capital)

# import re
# text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"
# email = re.findall(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", text)
# print(email)

import re
text = input("이메일 형식: ")
email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.fullmatch(email, text):
    print("올바른 이메일 주소! ")
else:
    print("Wrong Email")
