# generator2_1.py

import time

def longtime_job():
    print("job start")
    time.sleep(1)   # 1초 지연
    return "done"

gen_job = (longtime_job() for i in range(5))
print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))
print(gen_job)   # generator object

print('__iter__' in dir(gen_job))   # True -> iterable
print('__next__' in dir(gen_job))   # True -> iterator