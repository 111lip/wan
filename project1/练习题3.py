# 1. 使用列表推导式生成1-100的整数并输出偶数
numbers = [x for x in range(1, 101)]
even_numbers = [x for x in numbers if x % 2 == 0]
print("1-100中的偶数:", even_numbers)

# 2. 删除列表中的重复元素并保持顺序
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print("去重后的列表:", unique_list)

# 3. 合并两个列表为字典
keys = ["a", "b", "c"]
values = [1, 2, 3]
merged_dict = dict(zip(keys, values))
print("合并后的字典:", merged_dict)

# 4. 定义元组并解包
student_info = ("张三", 20, 90)
name, age, score = student_info
print(f"学生姓名: {name}, 年龄: {age}, 成绩: {score}")