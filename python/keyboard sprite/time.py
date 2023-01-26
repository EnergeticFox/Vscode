import time
def sleeptime(sec):
	return  sec
second = sleeptime(2)
repeat=0
repeat_time=5
while repeat<repeat_time:
    time.sleep(second)
    print (repeat)
    repeat+=1

