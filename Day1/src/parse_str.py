import parse3

# 示例字符串
log_string = '192.168.0.1 - - [05/Feb/2024:12:30:45 +0800] "GET /index.html HTTP/1.1" 200 1234'

# 定义解析模式
pattern = '{ip} - - [{timestamp}] "{method} {url}" {status_code} {response_size}'



if __name__ == '__main__':

    # 解析字符串
    result = parse3.regex(pattern, log_string)

    # 输出解析结果
    if result:
        print("IP:", result['ip'])
        print("Timestamp:", result['timestamp'])
        print("Method:", result['method'])
        print("URL:", result['url'])
        print("Status Code:", result['status_code'])
        print("Response Size:", result['response_size'])
    else:
        print("匹配失败")