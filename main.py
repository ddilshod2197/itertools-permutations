import itertools

def permutatsiya(n, r):
    return list(itertools.permutations(range(1, n + 1), r))

def kombinatsiya(n, r):
    return list(itertools.combinations(range(1, n + 1), r))

n = int(input("Permutatsiya va kombinatsiyalarni hisoblash uchun n ni kiriting: "))
r = int(input("Permutatsiya va kombinatsiyalarni hisoblash uchun r ni kiriting: "))

print("Permutatsiya:", permutatsiya(n, r))
print("Kombinatsiya:", kombinatsiya(n, r))
```

```python
import itertools

def permutatsiya(n, r):
    return list(itertools.permutations(range(1, n + 1), r))

def kombinatsiya(n, r):
    return list(itertools.combinations(range(1, n + 1), r))

n = int(input("Permutatsiya va kombinatsiyalarni hisoblash uchun n ni kiriting: "))
r = int(input("Permutatsiya va kombinatsiyalarni hisoblash uchun r ni kiriting: "))

print("Permutatsiya:", permutatsiya(n, r))
print("Kombinatsiya:", kombinatsiya(n, r))
