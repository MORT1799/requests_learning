import requests


class Res(object):
    def __init__(self, url0):
        self.url0 = url0

    def run(self, method, url, params=None, data=None, json=None, headers=None):
        url1 = self.url0 + url
        if method == 'get':
            try:
                response = requests.get(url1, params=params, headers=headers)
                response.encoding = 'utf8'
                print('\n', response.text, '\n')
                return response
            except BaseException as e:
                print("请求失败！", e)

        else:
            if method == 'post':
                try:
                    response = requests.post(url1, data=data, json=json, headers=headers)
                    response.encoding = 'utf8'
                    print('\n', response.text, '\n')
                    if url == '/login':
                        token = response.json().get('data').get('token')
                        return response, token
                    else:
                        if url == '/inspirer/new':
                            inspirerid = response.json().get('data').get('inspirerid')
                            return response, inspirerid
                        else:
                            return response
                except BaseException as e:
                    print("请求失败！", e)


'''
    def get(self, url, params=None, headers=None):
        try:
            url1 = self.url0+url
            response = requests.get(url1, params=params, headers=headers)
            return response
        except BaseException as e:
            print("请求失败！", e)

    def post(self, url, data=None, json=None, headers=None):
        url1 = self.url0+url
        try:
            response = requests.get(url1, data=data, json=json, headers=headers)
            if url == '/login':
                token = response.json().get('data').get('token')
                return response, token
            else:
                if url == '/inspirer/new':
                    inspirerid = response.json().get('data').get('inspirerid')
                    return response, inspirerid
                else:
                    return response
        except BaseException as e:
            print("请求失败！", e)
'''

if __name__ == '__main__':
    url_ori = 'http://118.24.105.78:2333'
    url_dict = {'show_version': '/showversion',
                'register': '/regist',
                'login': '/login',
                'launch_inspire': '/inspirer/new',
                'get_inspire': '/get/inspirer'}
    headers0 = {'Content-Type': 'application/json'}

    # 实例化
    res = Res(url_ori)

    # show_version
    res.run(method='get', url=url_dict['show_version'])

    # register
    register_data = {"username": "zhangxingfu",
                     "password": "a1234567",
                     "phone": "18212300834",
                     "email": "hhhjd@163.com"}
    r_register = res.run(method='post', url=url_dict['register'], json=register_data, headers=headers0)

    # login
    login_data = {"username": "zhangxingfu",
                  "password": "a1234567"}
    r_login, token0 = res.run(method='post', url=url_dict['login'], json=login_data, headers=headers0)

    # launch inspire
    url_data = {"content": "这是YK的灵感~"}
    headers1 = headers0
    headers1.update({'token': token0})
    r_inspire, inspirer_id = res.run(method='post', url=url_dict['launch_inspire'], json=url_data, headers=headers1)

    # get inspire
    param = {'iid': inspirer_id}
    res.run(method='get', url=url_dict['get_inspire'], params=param, headers=headers0)
