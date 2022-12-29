import requests

#get方法封装
# 1、创建封装get方法
def requests_get(url,headers):
# 2、发送get方法请求
    r = requests.get(url,headers=headers)
# 3、获取结果相应内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text

# 4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
# 5、字典返回
    return res

#post方法封装
# 1、创建封装post方法
def requests_post(url, json=None, headers=None):
# 2、发送post方法请求
    r = requests.get(url, json=json, headers=headers)
# 3、获取结果相应内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text

# 4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
# 5、字典返回
    return res

# 重构
#1、创建类
class Request:
    def requests_api(self,url,json=None,data=None,cookies=None,headers=None,method="get"):
        if method == "get":
            # 发送get方法请求
            r = requests.get(url, data=data,headers=headers,cookies=cookies)
        elif method == "post":
            # 发送post请求
            r = requests.get(url,data=data,headers=headers,cookies=cookies)

            # 获取结果相应内容
            code = r.status_code
            try:
                body = r.json()
            except Exception as e:
                body = r.text

            # 内容存到字典
            res = dict()
            res["code"] = code
            res["body"] = body
            # 字典返回
            return res


# 3、重构get/post方法
    #get
    #1、定义方法
    def get(self,url,**kwargs):
    #2、定义参数
        #url,json,headers,cookies,mehtod
    #3、调用公共方法
        return self.requests_api(url,method="get",**kwargs)

    # post
    # 1、定义方法
    def post(self, url, **kwargs):
        # 2、定义参数
        # url,json,headers,cookies,mehtod
        # 3、调用公共方法
        return self.requests_api(url, method="post", **kwargs)