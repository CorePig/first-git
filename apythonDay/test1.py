import requests
# 爬取的token
msg_token = ""
# 爬取的guest
msg_guest = ""


def main():
    # 健康日报打卡
    headers = {
        "POST": "/v1/trace/Student/dailyreportadd HTTP/1.1",
        "Host": "xg.nyist.vip",
        "Connection": "keep-alive",
        "Content-Length": "88",
        "appid": "1",
        "content-type": "application/x-www-form-urlencoded",
        "guest": "b2w4YlB2M0osMTkyMTgsTHU0T0FsVnYsMTY2ODMzMjY5MC41MTE2LHpNdmJUdVo3bEJfTSwxZDYzMTQ2MDZkOTZiNWFmMDM5ZmE5Y2ExZWE0MGE3NQ==",
        "token": "03ac80a7-a7b1-4436-a187-8cebc8afd9d1",
        "Referer": "https://servicewechat.com/wx5d22ba28f10a2e09/48/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
    }
        #位置信息
    data = {
        "pcc": "410000,411300,411302",
        "gps": "33.0036,112.5396",
        "location": "2",
        "status": "0",
        "temp": "0",
        "contact": 0,
    }
    #网络请求
    r = requests.post(
        "https://xg.nyist.vip/v1/trace/Student/dailyreportadd", headers=headers, data=data
    )
    # print(r.json()['msg'])
    #终端输出结果
    return r.json()['msg']

if __name__ == '__main__':
        print(main())

