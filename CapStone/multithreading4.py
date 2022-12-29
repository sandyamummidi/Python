#concurrency
import concurrent.futures
import time
start=time.perf_counter()
def calculateTime(seconds):
    print(f"sleep for {seconds} second\n")
    time.sleep(seconds)
    print(f"Completed{seconds} sleep\n")
with concurrent.futures.ThreadPoolExecutor() as executor:
    l =[1,2,3,4,5]
    results=[executor.submit(calculateTime,i) for i in l]


    for r in concurrent.futures.as_completed(results):
        print(r)
        print(r.result())

finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')