import time

def random_number(minimum,maximum):
    now = str(time.perf_counter())
    rnd = float(now[::-1][:3:])/1000
    return minimum + rnd*(maximum-minimum)
i=0

print(random_number(0,100))
