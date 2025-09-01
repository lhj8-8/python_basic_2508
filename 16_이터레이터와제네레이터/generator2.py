#generator2.py

import time

def longtime_job():
    print('job start')
    time.sleep(1)
    return "done"

# list_job=[longtime_job() for i in range(5)]
list_job=(longtime_job() for i in range(5))  #제네레이터 표현식
print(next(list_job))          #5번 작업하는 걸로 돼있는데, 맨 앞에 한 번만 출력하고 끝
