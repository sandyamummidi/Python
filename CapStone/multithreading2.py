# for loop using
import threading
import time
start=time.perf_counter()
def calculateTime():
    print("sleep for 5 seconds")
    time.sleep(5)
    print("completed sleep\n")
threads=[]

for _ in range(5):
    thread = threading.Thread(target=calculateTime)
    thread.start()
    threads.append(thread)
print(threads)

for t in threads:
    t.join()
    print("threads",t)
finish=time.perf_counter()
print(f'Finished in {finish-start} seconds')
