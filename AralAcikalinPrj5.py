import time
seed=time.time()
m=2**32
a=918239
c=98123892398
for i in range(40):
    seed=(a*seed+c)%m

    random=seed/m
    print(random)