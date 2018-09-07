#coding:utf8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

mail_info = {
    "from": "921885228@qq.com",
    "to": "chengjl16@163.com",
    "hostname": "smtp.qq.com",
    "username": "921885228@qq.com",
    "password": "nczxzreafgwmbbbh",
    "mail_subject": "test",
    "mail_text": "Hello, I just want to test the feasibility of this module...",
    "mail_encoding": "utf-8"
}

if __name__ == '__main__':
    #这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(mail_info["hostname"])
    smtp.set_debuglevel(1)
    
    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])

    msg = MIMEText(mail_info["mail_text"], "plain", 
					mail_info["mail_encoding"])
    msg["Subject"] = Header(mail_info["mail_subject"], 
							mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

    smtp.quit()