import time as t

print(t.time())     # 1789047005.2387369 (vary)


# Find execution time
start = t.time()
for i in range(10000000):
    pass
end = t.time()

print("Execution time:" ,end - start)   # Execution time: 0.29032468795776367


# example 2 : 
start1 = t.time()
print("Start")

t.sleep(4)

print("end")
end1 = t.time()

print("Execution time:" ,end1 - start1)     # Execution time: 4.000955581665039


print(t.ctime())         # Thu Sep 10 19:00:09 2026
print(t.ctime(0))        # Thu Jan  1 05:30:00 1970
print(t.ctime(999999))   # Mon Jan 12 19:16:39 1970


current_time = t.localtime()
print(current_time)     