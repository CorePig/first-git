# 测试健康日报管用不管用
import requests

url=r"https://xg.nyist.vip/student/passport/qrscan/uuid/9d14e5a3-76cf-49e9-8bb2-bd248061b290-41d5812de86d5aae963ebf70881cd62f.html"
# url=r"https://xg.nyist.vip/student/passport/qrlogin/url/https%3A%2F%2Fxg.nyist.vip%2Faddons%2Fstufile%2Fstudent%2Fmyfiles.html"
def main():
    # 健康日报打卡
    headers = {
        "cookie": "PHPSESSID=8638hevimb41bta26jisihtjl2",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
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
    r = requests.post(url, headers=headers)
    # print(r.json()['msg'])
    #终端输出结果
    print(r.content.decode("utf-8"))
    return r
    
if __name__ == '__main__':
	print(main())

