from time import sleep, time

for i in range(10):
    print(i, str(time()))
    sleep(0.5)

print("Time is over")