import requests
import json
from config.comment import GetCookier



class RunMain:
    def __init__(self, method=None, url=None, headers=None, data=None):
        self.method = method
        self.url = url
        self.headers = headers
        self.data = data
        self.get = GetCookier
        self.rq = requests.session()

    def run_get(self, method, url, headers=None):
        res = self.rq.request(method, url, headers=headers)
        return res.json()

    def run_post(self, method, url, data):
        res = self.rq.request(method, url, data=data)
        return res.json()

    def run_main(self, method, url, headers=None, data=None):
        res = None
        if method == 'post':
            res = self.run_post(method, url, data)
        else:
            res = self.run_get(method, url, headers)
        return json.dumps(res,sort_keys=True,ensure_ascii=False)

# if __name__ == '__main__':
    # from config.comment import RelyData
    # url = "http://127.0.0.1:3000/api/user/login"
    # payload = {
    #     "email": "admin@admi.com",
    #     "password": "admin"
    # }
    # headers = {
    #     'Content-Type': 'application/json',
    #     'Cookie': '_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjE5LCJpYXQiOjE2MTg1NDIyMTgsImV4cCI6MTYxOTE0NzAxOH0.PFRb3pZw0smjyklFFT4iPbv92hvH_n935PX7YSv4zhA; _yapi_uid=19'
    # }
    # merhod = 'post'
    #
    # tun = RunMain()
    # # tun.run_get()
    # # tun.run_post()
    # koo = requests.session()
    # ss = requests.request(merhod,url, data=payload).json()
    # print(ss)
    # setattr(RelyData,'project_id',ss.get('data')['username'])
    # print(RelyData.project_id)
    # u = 'http://127.0.0.1:3000/api/group/get?id=11'
    # da = {
    #     # "id":RelyData,'project_id',ss.get('data')['username'],
    # }
    # met = 'get'
    # ls = tun.run_main(met,u)
    # print(ls)
    #
