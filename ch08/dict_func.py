# dict_func.py

a = {
    "mon": "월", 
    "tue": "화", 
    "wed": "수",  
}
print(a)

x = a
print(x)

x["sun"] = "일"
print(x)  # 마찬가지로 dictionary의 메모리 주소 참조
print(a) 

print('---------------------')

def fch(x):
    x[1] = "일"

a = {
    "mon": "월", 
    "tue": "화", 
    "wed": "수",  
}
print(a)

fch(a)
print(a)