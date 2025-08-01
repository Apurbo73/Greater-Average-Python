n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    d = (a + b) / 2
    if d > c:
        print("Yes")
    else:
        print("no")
