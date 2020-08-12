a, b, c, d = [int(i) for i in input().split(' ')]
M = a * b
P = c * d
if M > P:
    print("M")
elif M < P:
    print('P')
else:
    print('E')
