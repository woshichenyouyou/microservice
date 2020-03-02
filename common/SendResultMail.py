#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def mail_message(sender,mailto_list,mailcc_list,subject,html_text,attachment_file):
    print("mail_message start")
    content = MIMEText(html_text, _subtype='html', _charset='utf-8')
    message = MIMEMultipart()
    message.attach(content)
    message['From'] = Header("~HEALTH Xray Reliability", 'utf-8')
    message['To'] = ";".join(mailto_list)
    message['Cc'] = ";".join(mailcc_list)
    message['Subject'] = Header(subject, 'utf-8')
    attachments = MIMEApplication(open(attachment_file, 'rb').read())
    attachments["Content-Type"] = 'application/octet-stream'
    attachments.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_file))
    message.attach(attachments)
    print("mail_message end")
    return message

def send_mail(FROM,TO,msg,SUBJECT):
    print("send_mail start")
    try:                
        HOST = 'smtp.163.com'
        PORT = '25'
        FROM = 'woshiyouyouchen@163.com'
        TO = 'woshichenyouyou@163.com'

        SUBJECT = 'testsubject'
        CONTENT = "this is the mail content"

        smtp_obj = smtplib.SMTP()

        smtp_obj.connect(host=HOST, port=PORT)

        res = smtp_obj.login(user=FROM, password='cyy07110313')
        print('logon result:', res)

        #msg = '\n'.join(['From: {}'.format(FROM), 'To: {}'.format(TO), 'Subject: {}'.format(SUBJECT), '', CONTENT])
        smtp_obj.sendmail(from_addr=FROM, to_addrs=TO, msg=msg.as_string())
        print("Send mail succed!")
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':

    get_input = sys.argv
    sender = 'woshiyouyouchen@163.com'
    mailto_list = ['woshiyouyouchen@163.com']
    mailcc_list = ['woshichenyouyou@163.com']
    receivers = mailto_list+mailcc_list
    #json.loads()
    print(len(get_input))
    if len(get_input) == 7:
        suiteName = get_input[1]
        IP = get_input[2]
        resultPass = get_input[3]
        resultFail = get_input[4]
        resultError = get_input[5]
        attachment_file = get_input[6]
        resultTotal = int(resultPass) + int(resultFail) + int(resultError)
        now=time.strftime("%Y-%m-%d %H:%M:%S")
        subject = '[Auto Test] Report for ' + str(suiteName) + ' on bench ip ' + str(IP) +  ' ' + now
        html_text = """\
<!DOCTYPE html>
<html>
<meta charset="utf-8">
<head>
    <title>Test Summary</title>
</head>
<body>
<div id="container">
    <div id="content">
        <p>

            <p>Test Suite: """ + str(suiteName)  +  """ </p>
            <p>Target (remote ip): """ + str(IP)  +  """ </p>
            <p>Result: </p>
            <table width="800" border="2" bordercolor="black" cellspacing="2">
                <tr>
                    <td><strong>Total</strong></td>
                    <td><strong>Pass</strong></td>
                    <td><strong>Fail</strong></td>
                    <td><strong>Error</strong></td>
                </tr>
                <tr>
                    <td bgcolor="#7D7DFF">""" + str(resultTotal) + """</td>
                    <td bgcolor="#00EC00">""" + str(resultPass) + """</td>
                    <td bgcolor="#FF8040">""" + str(resultFail) + """</td>
                    <td bgcolor="#FF0000">""" + str(resultError) + """</td>
                </tr>
            </table>
        </p>
        <p>

        Please see attacnment fot details.

        </p>
    </div>
</div>
</body>
</html>
                    """
        #attachment_file = '/home/cyy/Test/stockproject/1.txt'


        msg = mail_message(sender,mailto_list,mailcc_list,subject,html_text,attachment_file)

        send_mail(sender,receivers,msg,subject)

    else:
        print("Send mail Fail!")
        pass


