# 测试健康日报管用不管用
# -*- coding: utf8 -*-
import requests

# 爬取的token
msg_token = ""
# 爬取的guest
msg_guest = ""
# "POST": "/v1/trace/Student/dailyreportadd HTTP/1.1",
# "Host": "xg.nyist.vip",
# 分别代表小程序所在域名，小程序APPID
#"Referer": "https://servicewechat.com/wx5d22ba28f10a2e09/48/page-frame.html",
def main():
    # 健康日报打卡
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "cookie": "PHPSESSID=k07k6t23ngttpn6is3s2rp5arb; stoken=2fbf8bb093b76e9d692c70385920da4f",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "referer": "https://servicewechat.com/wx5d22ba28f10a2e09/48/page-frame.html"
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
        "https://xg.nyist.vip/v1/trace/Student/dailyreportadd", headers=headers, json=data
    )
    # print(r.json()['msg'])
    #终端输出结果
    return r.json()['msg']
    
if __name__ == '__main__':
	print(main())

