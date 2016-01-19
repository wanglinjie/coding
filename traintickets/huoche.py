#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Create Time  : 20160119
Last Modified: 
查询剩余火车票信息
'''

import requests
import json
import smtplib
import time
from email.mime.text import MIMEText
import chardet


class TrainTickets(object):
    '''
    获得火车票的信息
    '''
    def __init__(self):
        self.headers = {
                    "Accept": "text/html,   \
                    application/xhtml+xml,  \
                    application/xml;",
                    "Accept-Encoding": "gzip, deflate, sdch",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)  \
                    AppleWebKit/537.36 (KHTML, like Gecko)  \
                    Chrome/46.0.2490.80 Safari/537.36"
                  }
    def getTicketsInfo(self, purpose_codes, queryDate, from_station, to_station):
        url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=%s&queryDate=%s&from_station=%s&to_station=%s' %(
               purpose_codes, queryDate, from_station, to_station)
        TicketSession = requests.Session()
        TicketSession.verify = False  # 关闭https验证
        TicketSession.headers = self.headers
        try:
            resp_json = TicketSession.get(url)
            ticketsDatas = json.loads(resp_json.text)["data"]["datas"]
            return ticketsDatas
        except Exception, e:
            print e
            return ""


class Notify(object):
    '''
    通过邮件将火车票的信息反馈给自己
    '''
    def sendEmail(self, smtpserver, sender, receivers,
                  username, password, subject, content):
        msg = MIMEText(content, 'html', 'utf8')
        msg.set_charset('utf8')
        msg['Subject'] = subject
        msg['From'] = sender
        
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        for receiver in receivers:
            msg['To'] = receiver
            smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()


def isZero(num):
    if (num == unicode("--".decode("utf-8"))) or (num == unicode("无".decode("utf-8"))):
        return '0'
    else:
        return num.encode("utf-8")


def main():
    '''
    ***************************
    邮箱配置
    @sender 发送者邮箱账号
    @receiver 收件邮箱账号
    @username 邮箱账号
    @password 邮箱密码
    @subject 邮件主题
    @smtpserver smtp服务器地址
    @content 火车票信息
    @relay 多久发送一次,单位s
    ***************************
    '''
    sender = '123@163.com'
    receiver = ['123@qq.com', '234@qq.com']
    subject = '火车票信息'
    smtpserver = 'smtp.163.com'
    username = '123@163.com'
    password = '123'
    # relay = 120
    relay = 60

    '''
    ***************************
    查询信息配置
    @purpose_codes 票的种类-成人票(ADULT)还是学生票(0X00)
    @queryDate 日期
    @from_station 起始站
    @to_station 目的站
    ***************************
    '''
    purpose_codes = 'ADULT'
    queryDates = ['2016-02-22', '2016-02-23']
    # queryDates = ['2016-01-22']
    from_stations = ['NCG', 'JJG']
    to_stations = ['HBB', 'CCT']

    no_tickets = ["--", "无", "0", "*"]

    '''
    ***************************
    配置结束
    ****************************
    '''
    ticketSprider = TrainTickets()
    notifyme = Notify()

    while True:
        for queryDate in queryDates:
            for from_station in from_stations:
                for to_station in to_stations:
                    res = ticketSprider.getTicketsInfo(purpose_codes, queryDate,
                                                from_station, to_station)
                    if res == "":
                        continue
                    # print json.dumps(res, encoding="UTF-8", ensure_ascii=False)
                    contentlist = []
                    content = ''
                    new_subject = ''
                    for i, ticketInfo in enumerate(res):
                        # print ticketInfo["yw_num"]
                        # str_yw_num = isZero(ticketInfo["yw_num"].decode(chardet.detect(unicode(ticketInfo["yw_num"]))['encoding']))
                        # str_yz_num = isZero(ticketInfo["yz_num"].decode(chardet.detect(unicode(ticketInfo["yw_num"]))['encoding']))
                        str_yw_num = isZero(ticketInfo["yw_num"])
                        str_yz_num = isZero(ticketInfo["yz_num"])
                        if (str_yw_num not in no_tickets) or (str_yz_num not in no_tickets):
                            print ticketInfo["yw_num"], ticketInfo["yz_num"]
                            if (float(str_yw_num) > 0):
                                new_subject = ("%s硬卧火车票" % queryDate) + subject
                            elif (float(str_yz_num) > 0):
                                new_subject = ("%s硬座火车票" % queryDate) + subject
                            # print new_subject

                            contentlist.append("**********************************</br>")
                            contentlist.append(u"车次:%s</br>" %ticketInfo["station_train_code"])
                            contentlist.append(u"起始站:%s</br>" %ticketInfo["start_station_name"])
                            contentlist.append(u"目的地:%s</br>" %ticketInfo["to_station_name"])
                            contentlist.append(u"开车时间:%s</br>" %ticketInfo["start_time"])
                            contentlist.append(u"到达时间:%s</br>" %ticketInfo["arrive_time"])
                            contentlist.append(u"二等座还剩:%s张票</br>" %isZero(ticketInfo["ze_num"]))
                            contentlist.append(u"硬座还剩:%s张票</br>" %isZero(ticketInfo["yz_num"]))
                            contentlist.append(u"硬卧还剩:%s张票</br>" %isZero(ticketInfo["yw_num"]))
                            contentlist.append(u"无座还剩:%s张票</br>" %isZero(ticketInfo["wz_num"]))
                            contentlist.append(u"是否有票:%s</br>" %ticketInfo["canWebBuy"])
                            '''
                            print "**********************************"
                            print u"车次:%s" %ticketInfo["station_train_code"]
                            print u"起始站:%s" %ticketInfo["start_station_name"]
                            print u"目的地:%s" %ticketInfo["to_station_name"]
                            print u"开车时间:%s" %ticketInfo["start_time"]
                            print u"到达时间:%s" %ticketInfo["arrive_time"]
                            print u"二等座还剩:%s张票" %isZero(ticketInfo["ze_num"])
                            print u"硬座还剩:%s张票" %isZero(ticketInfo["yz_num"])
                            print u"硬卧还剩:%s张票" %isZero(ticketInfo["yw_num"])
                            print u"无座还剩:%s张票" %isZero(ticketInfo["wz_num"])
                            print u"是否有票:%s" %ticketInfo["canWebBuy"]
                            '''
                            content = content.join(contentlist)
                    if content:
                        notifyme.sendEmail(smtpserver, sender, receiver,
                                        username, password, new_subject, content)
        # print "relay"
        time.sleep(relay)


if __name__ == '__main__':
    while(True):
        main()