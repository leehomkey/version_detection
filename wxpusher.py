import requests

def windows_wxpusher(topic,message):
    # windows终端推送
    if topic == 'windows':
        topicid = '11516'
    # mac和信创终端推送
    if topicid == "mac_linux":
        topic = '11781'
    # 移动端推送
    if topic == "mobile":
        topicid = '11780' 
    # 推送全部
    if topic == 'all':
        topicid ='11516,11780,11781'   
    url = 'https://wxpusher.zjiecode.com/api/send/message'
    data = {
    "appToken":"AT_YLfSsq72BSv1qjb7p7vu3wCrvXWaqfqw",
    "content":message,
    "summary":"版本更新通知",
    "contentType":2,
    "topicIds":[topicid],
    "uids":[],
    "url":" ",
    "verifyPay":False}
    response = requests.post(url,json=data)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    message = "<body><h1>系统和浏览器信息</h1><p>Windows 11系统主版本和子版本均未更新</p><p>Chrome浏览器版本号未更新，版本号为：116.0.5845.110 发布日期：2023-08-23</p></body>"
    windows_wxpusher(message)