
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendmail(system, message):
    msg_from = '136352086@qq.com'  # 发送方邮箱
    passwd = 'qlftzbcyjtwhbide'  # 填入发送方邮箱的授权码(填入自己的授权码，相当于邮箱密码)
    msg_to = ['136352086@qq.com']  # 收件人邮箱
    # msg_to = ['136352086@qq.com', '410657528@qq.com', '317554872@qq.com', '290221161@qq.com', '1055413398@qq.com', 'xiaoxiaobing@sangfor.com.cn']  # 收件人邮箱
    if system == "iOS":
        subject = "苹果系统更新提醒"  # 主题
    elif system == "Android":
        subject = "Android系统更新提醒"  # 主题
    elif system == "chrome":
        subject = "Chrome版本更新提醒"  # 主题
    elif system == "error":
        subject = "系统更新检查代码出现异常"  # 主题

    # 生成一个MIMEText对象（还有一些其它参数）
    msg = MIMEText(message)
    # 放入邮件主题
    msg['Subject'] = subject
    # 也可以这样传参
    # msg['Subject'] = Header(subject, 'utf-8')
    # 放入发件人
    msg['From'] = msg_from
    # 放入收件人

    try:
        # 通过ssl方式发送，服务器地址，端口
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录到邮箱
        s.login(msg_from, passwd)
        # 发送邮件：发送方，收件方，要发送的消息
        s.sendmail(msg_from, msg_to, msg.as_string())
        print('成功')
    except s.SMTPException as e:
        print(e)
    finally:
        s.quit()

def sendmailerror(system, message):
    msg_from = '136352086@qq.com'  # 发送方邮箱
    passwd = 'qlftzbcyjtwhbide'  # 填入发送方邮箱的授权码(填入自己的授权码，相当于邮箱密码)
    msg_to = ['136352086@qq.com'] 
    # msg_to = ['136352086@qq.com', '1055413398@qq.com', 'xiaoxiaobing@sangfor.com.cn']  # 收件人邮箱
    #msg_to = ['136352086@qq.com', '410657528@qq.com', '317554872@qq.com', '290221161@qq.com']  # 收件人邮箱
    if system == "iOS":
        subject = "苹果系统更新提醒"  # 主题
    elif system == "Android":
        subject = "Android系统更新提醒"  # 主题
    elif system == "error":
        subject = "系统更新检查代码出现异常"  # 主题
    elif system == "andno":
        subject = "and系统无更新"  # 主题
    elif system == "iosno":
        subject = "ios系统无更新"  # 主题
    elif system == "browserno":
        subject = "browser版本无更新"  # 主题
    # 生成一个MIMEText对象（还有一些其它参数）
    msg = MIMEText(message)
    # 放入邮件主题
    msg['Subject'] = subject
    # 也可以这样传参
    # msg['Subject'] = Header(subject, 'utf-8')
    # 放入发件人
    msg['From'] = msg_from
    # 放入收件人

    try:
        # 通过ssl方式发送，服务器地址，端口
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录到邮箱
        s.login(msg_from, passwd)
        # 发送邮件：发送方，收件方，要发送的消息
        s.sendmail(msg_from, msg_to, msg.as_string())
        print('成功')
    except s.SMTPException as e:
        print(e)
    finally:
        s.quit()
