import random
from tqdm import tqdm

def evaluate(l):
    a = set()

    for i in range(len(l)-4):
        s = l[i:i+4]
        if len(set(s)) == 4:
            a.add(''.join(map(str, s)))

    return len(a)


sz = 15
it = 1000000
mx = -1
res = None

for i in tqdm(range(it)):
    l = [0, 1, 2, 3]

    for i in range(sz - 4):
        l.append(random.randrange(0, 4))
    
    e = evaluate(l)
    if e > mx:
        mx = e
        res = l

print(mx, res)