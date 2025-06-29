# 1. 判断一个数是否为回文数
def is_palindrome(num):
    """判断一个数是否为回文数"""
    return str(num) == str(num)[::-1]

# 2. 计算任意数量参数的平均值
def average(*args):
    """计算任意数量参数的平均值"""
    if not args:
        return 0
    return sum(args) / len(args)

# 3. 返回最长的字符串
def longest_string(*strings):
    """返回最长的字符串"""
    if not strings:
        return ""
    return max(strings, key=len)

# 4. 矩形计算模块（直接在同一文件中定义）
def rectangle_area(length, width):
    """计算矩形面积"""
    return length * width

def rectangle_perimeter(length, width):
    """计算矩形周长"""
    return 2 * (length + width)

# 测试代码
if __name__ == "__main__":
    # 测试回文数函数
    print(f"12321 是回文数: {is_palindrome(12321)}")  # 输出 True
    print(f"12345 是回文数: {is_palindrome(12345)}")  # 输出 False

    # 测试平均值函数
    print(f"平均值计算结果: {average(1, 2, 3, 4, 5)}")  # 输出 3.0

    # 测试最长字符串函数
    print(f"最长字符串: {longest_string('apple', 'banana', 'cherry')}")  # 输出 banana

    # 测试矩形计算函数
    length, width = 5, 3
    print(f"矩形面积: {rectangle_area(length, width)}")  # 输出 15
    print(f"矩形周长: {rectangle_perimeter(length, width)}")  # 输出 16