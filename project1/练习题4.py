# 第一部分：处理字符串 s1
s1 = "Python is a powerful programming language"
s2 = " Let's learn together"

# (1) 提取单词 "language"
words = s1.split()
print("提取的单词:", words[-1])

# (2) 连接字符串并重复输出3次
combined = s1 + s2
print("连接并重复3次:", combined * 3)

# (3) 输出以 p 或 P 开头的单词
p_words = [word for word in words if word.lower().startswith('p')]
print("以p或P开头的单词:", p_words)

# 第二部分：处理字符串 s3
s3 = " Hello, World! This is a test string. "

# (1) 去除前后空格
trimmed = s3.strip()
print("去除空格后:", trimmed)

# (2) 转换为大写
uppercase = trimmed.upper()
print("大写形式:", uppercase)

# (3) 查找子串 "test" 的起始下标
index = trimmed.find("test")
print("'test'的起始下标:", index)

# (4) 替换 "test" 为 "practice"
replaced = trimmed.replace("test", "practice")
print("替换后的字符串:", replaced)

# (5) 分割并使用 "-" 连接
joined = "-".join(trimmed.split())
print("连接后的字符串:", joined)