# 1、导入requsets包
import requests
# 2、发送get请求
r = requests.get("http://116.62.48.54:8081/wyh-api/api/article/13")
# 3、打印结果
print(r.json())
print('11221')