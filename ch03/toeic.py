# toeic.py

x = 889

if x >= 900:
    print('상위권')
elif x >= 700:
    print('중위권')
else: 
    print('하위권')
print('if문 종료')

print('--------------------------')

if x >= 900:
    print('상위권')
elif x >= 600:
    print('중상위권')
elif x >= 300:
    print('중위권')
else: 
    print('하위권')
print('if문 종료')

print('--------------------------')

x= 950

# if 900 <= x <= 990:
if x <= 990 and x >= 900:
    print('상위권')
elif x >= 600:
    print('중상위권')
elif x >= 300:
    print('중위권')
else: 
    print('하위권')
print('if문 종료')

