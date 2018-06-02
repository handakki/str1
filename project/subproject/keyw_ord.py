import time
print (time.time())
print (time.asctime())
print(time.localtime())
t1 = (2018,5,28,15,8,50,12,12,0)
print (time.asctime(t1))
t2 = time.localtime()
year = t2[7]
print (year)
for i in range(1,5):
    print (i)
    time.sleep(0.5)