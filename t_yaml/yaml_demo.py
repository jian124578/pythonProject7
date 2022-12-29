"""
1、创建yaml格式文件
2、读取这个文件
3、输入这个文件
"""
#2、读取这个文件
    #1）导入yaml包
import yaml
    #2）打开文件
with open("./data.yml","r") as f:
    #3）使用yaml读取文件
    r=yaml.safe_load(f)
#3、输出这个文件内容
    print(r)

