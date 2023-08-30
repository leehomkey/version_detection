# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import configparser
import wxpusher
import json

### 检测windows主版本 ###
def windows_version():
    try:
        global windows_detection
        # 先读取当前的windows11版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        # windows11主版本
        windows_version_old = config.get('windows_version','windows11')
        # windows11子版本
        windows_version_osm = config.get('windows_version','win11subversion')
        # 爬取最新的windows11版本
        url = "https://learn.microsoft.com/zh-cn/windows/release-health/windows11-release-information"
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        windows_version_new = soup.find('strong').text
        # 获取windows系统内部版本
        os_build = windows_version_new[-6:][:5]
        # 获取最新windows系统内部版本的子版本
        windows_version_nsm = soup.find_all(string=re.compile(os_build))[0]
        # 保存最新windows11版本到txt文件
        config.set('windows_version','windows11',windows_version_new)
        with open('version.ini','w') as configfile1:
            config.write(configfile1)
        # 保存最新的windows11子版本到txt文件
        config.set('windows_version','win11subversion',windows_version_nsm)
        with open('version.ini','w') as configfile2:
            config.write(configfile2)
        if windows_version_new == windows_version_old:   
            if windows_version_nsm == windows_version_osm:
                print('Windows 11系统主版本和子版本均未更新')
                windows_detection =  '<p>Windows 11系统主版本和子版本均未更新</p>'
            else:
                # 获取子版本更新连接说明
                headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",}
                links = soup.find_all('tr')[4]
                link_element = links.find("a",{'data-linktype': 'external'})
                link = link_element['href']
                # response_zbb = requests.get(link,headers=headers)
                # html_content_zbb = response_zbb.content
                # soup_zbb =  BeautifulSoup(html_content_zbb, "html.parser")
                # # 获取子版本更新的重要信息
                # update_info_1 = soup_zbb.find('h2',text='重要信息').parent
                # paragraphs_1 = update_info_1.find_all('p')
                # for paragraph_zyxx in paragraphs_1:
                #     print(paragraph_zyxx.get_text(strip=True))
                # # 获取子版本更新的改进项
                # update_info_2 = soup_zbb.find('h2',text='改进').parent
                # paragraphs_2 = update_info_2.find_all('p')
                # for paragraph_gj in paragraphs_2:
                #     print(paragraph_gj.get_text(strip=True))
                print('Windows 11系统主版本未更新,子版本有更新,请关注子版本更新特性；最新子版本：Win11 '+ windows_version_nsm)
                windows_detection = '<p style="color: red;">Windows 11系统主版本未更新,子版本有更新,最新子版本：Win11 '+ windows_version_nsm +'</p>'+'<p>请关注系统更新特性<a href='+link+'>点击查看系统更新详情</a></p>'
        else:
            print('Windows 11系统主版本有更新，请及时测试最新版本；最新版本：Win11 '+ windows_version_new)
            windows_detection = '<p style="color: red;">Windows 11系统主版本有更新，请及时测试最新版本；最新版本：Win11 '+ windows_version_new +'</p>'
    except Exception as e:
        print(e)
        windows_detection = '<p style="color: red;">Windows 系统更新检测失败，请及时检查相关更新脚本和网络信息</p>'
### 检测chrome浏览器版本
def chrome_version():
    try:
        global chrome_detection
        # 先读取当前的chrome版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        chrome_version_old = config.get('browser_version','Chrome')
        response = requests.get("https://www.whatismybrowser.com/guides/the-latest-version/chrome")
        content = response.content
        soup_chrome = BeautifulSoup(content, "html.parser")
        chrome_version_new = soup_chrome.find('strong',string='Windows').parent.find_next_sibling('td').text
        update_date = soup_chrome.find('strong',string='Windows').parent.find_next_sibling('td').find_next_sibling('td').text
        if chrome_version_new == chrome_version_old:
            print('Chrome浏览器版本号未更新，版本号为：'+chrome_version_new+' 发布日期：'+update_date)
            chrome_detection = '<p>Chrome浏览器版本号未更新，版本号为：'+chrome_version_new+' 发布日期：'+update_date+'</p>'
        else:
            config.set('browser_version','Chrome',chrome_version_new)
            with open('version.ini','w') as configfile:
                config.write(configfile)
            print('Chrome浏览器版本号已更新，请及时测试最新版本；版本号是：'+chrome_version_new+' 发布日期：'+update_date)
            chrome_detection = '<p style="color: red;">Chrome浏览器版本号已更新，请及时测试最新版本；版本号是：'+chrome_version_new+' 发布日期：'+update_date+'</p>'
    except Exception as e:
        print(e)
        chrome_detection = '<p style="color: red;">Chrome浏览器更新检测失败，请及时检查相关更新脚本和网络信息</p>'
def edge_version():
    try:
        global edge_detection
        # 先读取当前的EDGE版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        edge_version_old = config.get('browser_version','Edge')
        response = requests.get("https://www.whatismybrowser.com/guides/the-latest-version/edge")
        content = response.content
        soup_edge = BeautifulSoup(content, "html.parser")
        edge_version_new = soup_edge.find('strong',string='Windows').parent.find_next_sibling('td').text
        update_date = soup_edge.find('strong',string='Windows').parent.find_next_sibling('td').find_next_sibling('td').text
        if edge_version_new == edge_version_old:
            print('Edge浏览器版本号未更新，版本号为：'+edge_version_new+' 发布日期：'+update_date)
            edge_detection = '<p>Edge浏览器版本号未更新，版本号为：'+edge_version_new+' 发布日期：'+update_date+'</p>'
        else:
            config.set('browser_version','Edge',edge_version_new)
            with open('version.ini','w') as configfile:
                config.write(configfile)
            print('Edge浏览器版本号已更新，请及时测试最新版本；版本号是：'+edge_version_new+' 发布日期：'+update_date)
            edge_detection = '<p style="color: red;">Edge浏览器版本号已更新，请及时测试最新版本；版本号是：'+edge_version_new+' 发布日期：'+update_date+'</p>'
    except Exception as e:
        print(e)
        edge_detection = '<p style="color: red;">Edge浏览器更新检测失败，请及时检查相关更新脚本和网络信息</p>'
def firefox_version():
    try:
        global firefox_detection
        # 先读取当前的Firefox版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        firefox_version_old = config.get('browser_version','Firefox')
        response = requests.get("https://www.whatismybrowser.com/guides/the-latest-version/firefox")
        content = response.content
        soup_firefox = BeautifulSoup(content, "html.parser")
        firefox_version_new = soup_firefox.find('strong',string='Standard Release').parent.find_next_sibling('td').find_next_sibling('td').text
        update_date = soup_firefox.find('strong',string='Standard Release').parent.find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
        if firefox_version_new == firefox_version_old:
            print('Firefox浏览器版本号未更新，版本号为：'+firefox_version_new+' 发布日期：'+update_date)
            firefox_detection = '<p>Firefox浏览器版本号未更新，版本号为：'+firefox_version_new+' 发布日期：'+update_date+'</p>'
        else:
            config.set('browser_version','Firefox',firefox_version_new)
            with open('version.ini','w') as configfile:
                config.write(configfile)
            print('Firefox浏览器版本号已更新，请及时测试最新版本；版本号是：'+firefox_version_new+' 发布日期：'+update_date)
            firefox_detection = '<p style="color: red;">Firefox浏览器版本号已更新，请及时测试最新版本；版本号是：'+firefox_version_new+' 发布日期：'+update_date+'</p>'
    except Exception as e:
        print(e)
        firefox_detection = '<p style="color: red;">Firefox浏览器更新检测失败，请及时检查相关更新脚本和网络信息</p>'
def se360_version():
    try:
        global se360_detection
        # 先读取当前的se360版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        se360_version_old = config.get('browser_version','se360')
        response = requests.get("https://browser.360.cn/se")
        content = response.content
        soup_se360 = BeautifulSoup(content, "html.parser")
        se360_version_new = soup_se360.find('em',string=re.compile('版本：')).text.split('：')[1].split()[0]
        if se360_version_new == se360_version_old:
            print('360安全浏览器版本号未更新;版本号为：'+se360_version_new)
            se360_detection = '<p>360安全浏览器版本号未更新；版本号为：'+se360_version_new+'</p>'
        else:
            config.set('browser_version','se360',se360_version_new)
            with open('version.ini','w') as configfile:
                config.write(configfile)
            print('360安全浏览器版本号已更新，请及时测试最新版本；最新版本号为：'+se360_version_new)
            se360_detection = '<p style="color: red;">360安全浏览器版本号已更新，请及时测试最新版本；最新版本号为：'+se360_version_new+'</p>'
    except Exception as e:
        print(e)
        se360_detection = '<p style="color: red;">360安全浏览器更新检测失败，请及时检查相关更新脚本和网络信息</p>'
### 检测360急速浏览器版本
def ee360_version():
    try:
        global ee360_detection
        # 先读取当前的ee360版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        ee360_version_old = config.get('browser_version','ee360')
        response = requests.get("https://browser.360.cn/ee")
        content = response.content
        soup_ee360 = BeautifulSoup(content, "html.parser")
        ee360_version_new = soup_ee360.find('a', string='32位版本')['href'].split('_')[1].split('.exe')[0]
        if ee360_version_new == ee360_version_old:
            print('360极速浏览器版本号未更新；版本号为：'+ee360_version_new)
            ee360_detection = '<p>360极速浏览器版本号未更新；版本号为：'+ee360_version_new+'</p>'
        else:
            config.set('browser_version','ee360',ee360_version_new)
            with open('version.ini','w') as configfile:
                config.write(configfile)
            print('360极速浏览器版本号已更新，请及时测试最新版本；版本号为：'+ee360_version_new)
            ee360_detection = '<p style="color: red;">360极速浏览器版本号已更新，请及时测试最新版本；版本号为：'+ee360_version_new+'</p>'
    except Exception as e:
        print(e)
        ee360_detection = '<p style="color: red;">360极速浏览器更新检测失败，请及时检查相关更新脚本和网络信息</p>'    
def sougou_version():
    try:
        global sougou_detection
        # 先读取当前的sougou版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        sougou_version_old = config.get('browser_version','sougou')
        response = requests.get("https://ie.sogou.com")
        content = response.content
        soup_sougou = BeautifulSoup(content, "html.parser")
        # with open('info.txt','w',encoding='utf-8') as file:
        #     file.write(str(soup_sougou))
        sougou_version_new = soup_sougou.find('a', string='下载')['href'].split('_')[2].split('.exe')[0]
        if sougou_version_new == sougou_version_old:
            print('搜狗浏览器版本号未更新；版本号为：'+sougou_version_new)
            sougou_detection = '<p>搜狗浏览器版本号未更新；版本号为：'+sougou_version_new+'</p>'
        else:
            config.set('browser_version','sougou',sougou_version_new)
            with open('version.ini','w') as configfile:
                config.write(configfile)
            print('搜狗浏览器版本号已更新，请及时测试最新版本；版本号为：'+sougou_version_new)
            sougou_detection = '<p style="color: red;">搜狗浏览器版本号已更新，请及时测试最新版本；版本号为：'+sougou_version_new+'</p>'
    except Exception as e:
        print(e)
        sougou_detection = '<p style="color: red;">搜狗浏览器更新检测失败，请及时检查相关更新脚本和网络信息</p>'
### 检测办公软件
def wps_version():
    try:
        global wps_detection
        # 先读取当前的wps版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        wps_version_old = config.get('work_softwore','wps')
        response = requests.get("https://www.wps.cn/platformUrls")
        content = response.text
        # with open('info1.txt','w',encoding='utf-8') as file:
        #     file.write(str(content))
        wps_version_new=json.loads(content)["productList"][0]["productVcode"]
        if wps_version_new == wps_version_old:
            print('WPS版本号未更新；版本号为：'+wps_version_new)
            wps_detection = '<p>WPS版本号未更新；版本号为：'+wps_version_new+'</p>'
        else:
            config.set('work_softwore','wps',wps_version_new)
            with open('version.ini','w') as configfile:
                config.write(configfile)
            print('WPS版本号已更新，请及时测试最新版本；版本号为：'+wps_version_new)
            wps_detection = '<p style="color: red;">WPS版本号已更新，请及时测试最新版本；版本号为：'+wps_version_new+'</p>'
    except Exception as e:
        print(e)
        wps_detection = '<p style="color: red;">WPS更新检测失败，请及时检查相关更新脚本和网络信息</p>'

def office_365():
    try:
        global office_365_detection
        # 先读取当前的office_365版本
        config = configparser.ConfigParser()
        config.read('version.ini')
        office_365_version_old = config.get('work_softwore','office_365')
        response = requests.get("https://learn.microsoft.com/zh-cn/officeupdates/update-history-microsoft365-apps-by-date")
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        office_365_version = soup.find('strong',string='当前频道').parent.parent.parent.parent.find('td',string=re.compile('内部版本')).text
        office_365_version_new = office_365_version.split()[1]+ ' ' + office_365_version.split()[3].split(')')[0]
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
def main():
    message = ""
    #系统更新
    windows_version()
    #浏览器更新
    chrome_version()
    edge_version()
    firefox_version()
    se360_version()
    ee360_version()
    sougou_version()
    #办公软件更新
    wps_version()
    office_365()
    message = "<body><h1>系统更新</h1><h2>Windows系统</h2>"+windows_detection+"<h1>浏览器更新</h1><h2>Chrome浏览器</h2>"+chrome_detection+"<h2>Edge浏览器</h2>"+edge_detection+"<h2>Firefox浏览器</h2>"+firefox_detection+"<h2>360安全浏览器</h2>"+se360_detection+"<h2>360急速浏览器</h2>"+ee360_detection+"<h2>搜狗浏览器</h2>"+sougou_detection+"<h1>办公软件更新</h1><h2>WPS</h2>"+wps_detection+"<h2>Office 365</h2>"+office_365_detection+"</body>"
    return message
if __name__ == "__main__":
    windows_message=main()
    print(windows_message)
    #wxpusher.wxpusher(windows_message)


