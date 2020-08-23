''':arg
answer1
'''

n, k = 25, 5
result = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        result += 1
        n = n // k
    else:
        n -= 1
        result += 1

print(result)

''':arg
answer2
'''

n, k = 17, 4
result = 0
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
while n > 1:
    n -= 1
    result += 1
print(result)

''':arg
answer3
'''

n, k = 17, 4
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k
result += (n - 1)
print(result)
