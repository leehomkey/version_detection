地址：https://github.com/leehomkey/version_detection
一、结构：
---main.py                     ###入口，每天9点定时执行
------windows_detection.py     ###windows终端相关系统、软件版本爬取解析实现（其他端可参考复用）
------wxpusher.py              ###微信推送实现，支持单独windows终端推送（'windows'）、移动端推送（'mobile'）、信创&MAC端推送（'mac_linux'），以及全部推送（'all'）
------version.ini              ###各个系统、软件版本的配置文件
二、规范：
1.每个端自行维护爬取脚本（例如windows端的windows_detection.py），生成需要推送的消息，使用HTML格式
2.调用微信推送时，可以选择单独windows终端推送（'windows'）、移动端推送（'mobile'）、信创&MAC端推送（'mac_linux'），以及全部推送（'all'）
3.各端的系统以及软件版本共用一个version.ini （各端软件版本号不同，要区分）

三、获取微信消息推送：
1.使用微信点击以下网址进行订阅即可获取消息推送
windows终端：https://wxpusher.zjiecode.com/wxuser/?type=2&id=11516#/follow
移动端：https://wxpusher.zjiecode.com/wxuser/?type=2&id=11780#/follow
信创&MAC端：https://wxpusher.zjiecode.com/wxuser/?type=2&id=11781#/follow

