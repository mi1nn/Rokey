# generator2.py

import time

def longtime_job():
    print("job start")
    time.sleep(1)   # 1초 지연
    return "done"

list_job = [longtime_job() for i in range(5)]
print(list_job)
print(list_job[0])

print(dir(list_job))

print('__iter__' in dir(list_job))   # True -> iterable
print('__next__' in dir(list_job))   # False -> not iterator