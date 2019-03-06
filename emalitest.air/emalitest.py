# -*- encoding=utf8 -*-
__author__ = "v-wutaotao"
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
def emalitest():
    #if __name__ == '__main__':
    fromaddr = '157366763@qq.com'
    password = 'ngtgepcvfpyobjjh'
    # toaddrs = ['745560207@qq.com', '137xxxx@qq.com']
    toaddrs = ['157366763@qq.com']

    content = '火柴人自动化冒烟测试测试结果'
    textApart = MIMEText(content)

    # imageFile = '1.png'
    # imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    # imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

    pdfFile = 'D:\\乱斗火柴人测试结果.html'
    pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)

    # zipFile = '算法设计与分析基础第3版PDF.zip'
    # zipApart = MIMEApplication(open(zipFile, 'rb').read())
    # zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    m = MIMEMultipart()
    m.attach(textApart)
    #m.attach(imageApart)
    m.attach(pdfApart)
    #m.attach(zipApart)
    m['Subject'] = '火柴人自动化测试结果'  # 填写发件人

    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('邮件发送成功')
        server.quit()

    except smtplib.SMTPException as e:
        print('发送失败:', e)  # 打印错误
