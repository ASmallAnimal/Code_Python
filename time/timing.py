import time
def wait():
    time.sleep(3.3)
wait()
start=time.perf_counter()
end=time.perf_counter()
print(end-start)

