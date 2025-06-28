# 1. 判断变量数据类型
x = 10
y = "10"
z = True

print(f"变量 x 的类型是: {type(x)}")
print(f"变量 y 的类型是: {type(y)}")
print(f"变量 z 的类型是: {type(z)}")

# 2. 计算圆的面积
radius = float(input("请输入圆的半径: "))
pi = 3.14
area = pi * (radius ** 2)
print(f"圆的面积是: {area}")

# 3. 数据类型转换
str_num = "3.14"
float_num = float(str_num)
int_num = int(float_num)

print(f"字符串 '3.14' 转换为浮点数是: {float_num}")
print(f"浮点数 {float_num} 转换为整数是: {int_num}")