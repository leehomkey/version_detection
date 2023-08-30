# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import configparser
import json
import os
def main():
    try:
        global office_365_detection
        # 先读取当前的office_365版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        office_365_version_old = config.get('work_softwore','office_365')
        response = requests.get("https://learn.microsoft.com/zh-cn/officeupdates/update-history-microsoft365-apps-by-date")
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        with open('info1.txt','w',encoding='utf-8') as file:
            file.write(str(soup))
        office_365_version = soup.find('strong',string='当前频道').parent.parent.parent.parent.find('td',string=re.compile('内部版本')).text
        office_365_version_new = office_365_version.split()[1]+ ' ' + office_365_version.split()[3].split(')')[0]
        print(office_365_version_new)
        if office_365_version_new == office_365_version_old:
            print('Office 365版本号未更新；版本号为：'+office_365_version_new)
            office_365_detection = '<p>Office 365版本号未更新；版本号为：'+office_365_version_new+'</p>'
        else:
            config.set('work_softwore','office_365',office_365_version_new)
            with open('version.ini','w') as configfile:
                config.write(configfile)
            print('Office 365版本号已更新，请及时测试最新版本；版本号为：'+office_365_version_new)
            office_365_detection = '<p style="color: red;">Office 365版本号已更新，请及时测试最新版本；版本号为：'+office_365_version_new+'</p>'
    except Exception as e:
        print(e)
        office_365_detection = '<p style="color: red;">Office 365更新检测失败，请及时检查相关更新脚本和网络信息</p>'
    return office_365_detection
if __name__ == "__main__":
    message=main()
    print(message)