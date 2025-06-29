# 1. 输出1到100之间的所有素数
print("1到100之间的素数有:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# 2. 计算斐波那契数列的前20项
fibonacci = [0, 1]
while len(fibonacci) < 20:
    next_term = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_term)
print("斐波那契数列的前20项是:")
print(fibonacci)

# 3. 计算符合条件的数的和
sum_result = 0
num = 1
while num <= 10000:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        sum_result += num
    num += 1
print("1-10000之间符合条件的数的和是:", sum_result)