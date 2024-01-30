import redis


r = redis.Redis(host='10.0.220.30', port=6379, db=0, password='wj@2022')

if __name__ == '__main__':

    # 检查键的数据类型
    key = "crm:talent:tt:topic:"
    key_type = r.type(key)

    print(f"The type of the key '{key}' is: {key_type}")

    # 获取集合中的一个元素
    element = r.spop(key)

    # 获取集合中的所有元素
    all_elements = r.smembers(key)

    # 打印结果
    print("Popped element:", element)
    print("All elements in the set:", all_elements)
