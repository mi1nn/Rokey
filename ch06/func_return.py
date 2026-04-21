# function_return.py

def plus(arg):
    if arg > 0:
        return "plus"
    elif arg < 0:
        return "minus"
    else:
        return 0
    
stra = plus(0)
print(stra)  # None

print('---------------------------')

