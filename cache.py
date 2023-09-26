import redis
from datetime import timedelta
import numpy as np

r = redis.Redis()

cache_hit = 0

min = 1
max = 100
n = 100000

keys = np.random.randint(min, max, n)

print(keys)

for i, key in enumerate(keys):
    if r.get(int(key)):
        cache_hit += 1
    else:
        r.setex(int(key), timedelta(minutes=1), value="cached")
    if i % 100 == 0:
        print(i, cache_hit/(i+1))

