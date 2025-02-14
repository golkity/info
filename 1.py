def ok(n):
    s = n ** 2
    return str(s).endswith(str(n))

def f(N):
    for i in range(1, N+1):
        if ok(i):
            print(i)

n = int(input())
f(n)
