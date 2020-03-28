import time
#插入数据
result = {}
for i in range(10000):
      result[i] = i
      #检索数据
time_start = time.time()
for i in range(10000):
       temp = result[i]
time_end=time.time()
print('检索时间',time_end-time_start)
