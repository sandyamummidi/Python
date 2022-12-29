
import threading
import time
start=time.perf_counter()
def calculateTime(seconds):
    print("sleep for 5 seconds")
    time.sleep(seconds)
    print("completed sleep\n")
threads=[]

for _ in range(5):
    thread = threading.Thread(target=calculateTime,args=[3])
    thread.start()
    threads.append(thread)


for t in threads:
    t.join()

finish=time.perf_counter()
print(f'Finished in {finish-start} seconds')