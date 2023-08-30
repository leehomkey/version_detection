import wxpusher
import windows_detection
import os

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 设置脚本工作目录
os.chdir(script_dir)
# 获取windows终端推送消息
windows_message=windows_detection.main()
# print(windows_message)
# 推送windows更新消息
wxpusher.windows_wxpusher(topic='windows',message=windows_message)