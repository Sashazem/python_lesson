n = int(input())
k1 = 1
k2 = 2
k3 = 3
n3 = (n // 10 ** k1) % 10
n2 = (n // 10 ** k2) % 10
n1 = (n // 10 ** k3) % 10
n4 = (n % 10 ** k1)
if n1 == n4 and n2 == n3:
    print(1)
else:
    print(2)
