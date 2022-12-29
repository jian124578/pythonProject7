import os
import yaml
#1、创建类
class YamlReader:
#2、初始化，文件是否存在
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
#3、yaml文件读取
    def data(self):
        #第一次调用data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf,"rb") as f:
