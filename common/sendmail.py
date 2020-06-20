import sys
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
# 邮箱配置
SMTP_CONFIG = {
    "mail_host" : "smtp.163.com",      	 # qq邮件服务器
    "mail_user" : "woshiyouyouchen@163.com",    	 # 用户名
    "mail_pass" : "MCMJCENUAIYPSIIF",       	 # 授权码,上面开通qqSTMP服务的授权码
    "sender" : "woshiyouyouchen@163.com",     	 # 发送邮箱
    "receivers" : ['woshiyouyouchen@163.com']   # 接收邮箱,可多个任意邮箱
}
class SendMsg():
    def send_email(self, subject, content,attachment_file):
       # 第三方 SMTP 服务
        try:
            html_text="<html><h1>this is stock info</h1><body>check for attached details</body></html>"
            content = MIMEText(html_text, _subtype='html', _charset='utf-8')
            message = MIMEMultipart()
            message.attach(content)
            #message = MIMEText(content, 'plain', 'utf-8')  # 发送内容
            message['Subject'] = Header(subject, 'utf-8')	# 发送标题
            message['From'] =  SMTP_CONFIG["sender"]		# 发送人
            message['To'] =  SMTP_CONFIG["receivers"][0]	# 接收人
            attachments = MIMEApplication(open(attachment_file, 'rb').read())
            attachments["Content-Type"] = 'application/octet-stream'
            attachments.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_file))
            message.attach(attachments)
            smtp = smtplib.SMTP_SSL(host=SMTP_CONFIG["mail_host"], port=465)  # 465是邮件ssl端口
            smtp.login(SMTP_CONFIG["mail_user"] ,SMTP_CONFIG["mail_pass"])    # 服务器登录  
            smtp.sendmail(SMTP_CONFIG["sender"], SMTP_CONFIG["receivers"], message.as_string())
            smtp.close()
            print("mail send success")
        except smtplib.SMTPException:
            print("mail send fail")
	            
if __name__ == "__main__":
    get_input = sys.argv
    attachment_file = get_input[1]
    print("the file need to send is:%s"%attachment_file)
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    subject = "stock"+now
    content = "this is the mail content"
    SendMsg().send_email(subject,content,attachment_file)
