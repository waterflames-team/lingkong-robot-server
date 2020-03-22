
from subprocess import call
import re
import sys
import subprocess
import threading
import urllib.request
import signal
import os
import json
import base64
import time
import random
import requests
import uuid
import logging
from logging import handlers

import lk.player
import shan
from server import server



interrupted = False
player = None
global history
history = None
jineng_s = None
readlog_s = None
logger = None
logger_go = 1


#沙雕取log----------------------------------------------------------------------------------

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)


#沙雕取log----------------------------------------------------------------------------------

read_log_s = None


global log_log
log_log = Logger('all.log',level='debug')

log_log.logger.debug('''

---------------------------------------
        灵空-一个中文语音对话机器人 
        版本号：0.5.7.200316
        by ffxw0720                
        欢迎使用!!!                              
---------------------------------------

''')

f = open("all.log",'r')#1
read_log_s = f.read() 
f.close()
readlog_s = read_log_s

#机器人主体分界线-------------------------------------------------------------------------------------

#web对话
class History():

    def __init__(self):
        self.history = []

    def getHistory(self):
        return self.history

    def appendHistory(self, type, text):
        if type in (0,1) and text != '':
            self.history.append({'type': type, 'text': text, 'uuid': str(uuid.uuid1())})

#web对话
history = History()

class jineng():

    def jineng(rl,j_hua):
    
        global jn_hua
        jn_hua = j_hua
        history.appendHistory(0, jn_hua)
        log_log = Logger('all.log',level='debug')
    

        class yuliao():

            def can():
                if '你会' in jn_hua:
                    log_log.logger.debug('已成功返回答复')
                    log_log.logger.debug("我会的东西可多了，有闲聊、问问题、讲笑话等。想知道更多的就去灵空的github看看吧！")
                    history.appendHistory(1,"我会的东西可多了，有闲聊、问问题、讲笑话等。想知道更多的就去灵空的github看看吧！")
        
            def father():
                if "你爸爸" in jn_hua or "你的爸爸" in jn_hua:
                    log_log.logger.debug('已成功返回答复')
                    log_log.logger.debug("我爸比是非凡小王！")
                    history.appendHistory(1,"我爸比是非凡小王！")

        class xiaohua():
            if '笑话' in jn_hua:
                xh = open(('xh_ku/' + str(random.randint(1, 40)) + '.txt'), mode='r',buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
                xh_jg = xh.read()
                log_log.logger.debug('已成功返回答复')
                log_log.logger.debug(xh_jg)
                history.appendHistory(1,xh_jg)


        class daiban():

            if '待办' in jn_hua or '代办' in jn_hua:

                if '待办' in jn_hua:
                    jn_hua = re.sub(r'待办', '代办', jn_hua)
                elif '代办' in jn_hua:
                    pass
            
                if '进入' in jn_hua:
                    jn_hua = re.sub(r'进入', '记录', jn_hua)

                class daiban(object):#灵空robot代办技能demo

                    def rukou(self,qidong):

                        def daiban(what):
                            db_lj = str(what)
                            log = open(('daiban_log/'+db_lj) , mode='a', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
                            log.write (what + '\n')
                            log.close
                            global th
                            th = what

                        if "添加" in qidong:
                            global jn_hua
                            if '待办' in jn_hua:
                                jn_hua = re.sub(r'待办', '代办', jn_hua)

                            if '进入' in jn_hua:
                                jn_hua = re.sub(r'进入', '添加', jn_hua)
                                
                            thing = re.sub(r'添加代办', ' ', jn_hua)
                            daiban(thing)
                            log_log.logger.debug('已成功返回答复')
                            log_log.logger.debug('完事')
                            history.appendHistory(1,'完事')

                        if "删除" in qidong:
                            if '待办' in jn_hua:
                                jn_hua = re.sub(r'待办', '代办', jn_hua)
                            db_hua = re.sub(r'删除代办', ' ', jn_hua)
                            shan.dele('daiban_log/'+db_hua)
                            log_log.logger.debug('已成功返回答复')
                            log_log.logger.debug('完事')
                            history.appendHistory(1,'完事')



                        elif "查看" in qidong:
                            log_log.logger.debug('已成功返回答复')
                            log_log.logger.debug('对不起，这个功能还未推出')
                            history.appendHistory(1,'对不起，这个功能还未推出')
                    

                a=daiban()
                a.rukou(jn_hua)

        def tuling(t_hua):
        
        

            url='http://openapi.tuling123.com/openapi/api/v2'
            city="福州"#请自行在这里修改城市为自己的城市

            sj = random.randint(1, 5)
            if sj == 1:
                apikey = "197deae9fb5c4fb3bfd970d82917aeb0"
                log_log.logger.debug("tuling_key1选择成功")
                pass
            if sj == 2:
                apikey = "ed984644aa50485ea0106b941de1f521"
                log_log.logger.debug("tuling_key2选择成功")
                pass
            if sj == 3:
                apikey = "22fdeb0cfcc146b0a3acb76241d80eaf"
                log_log.logger.debug("tuling_key3选择成功")
                pass
            if sj == 4:
                apikey = "e9c5c5121ccd4450a559c77fdc934b8a"
                log_log.logger.debug("tuling_key4选择成功")
                pass
            if sj == 5:
                apikey = "3a952ac21d8a4c079e59aedc36791bb2"
                log_log.logger.debug("tuling_key5选择成功")
                pass
        

            '''
            较多人使用同样5个apikey，一天只能调用500次，难免会不够，
            所以有能力的小伙伴我推荐自己去图灵机器人的首页注册一个自己的账号，实名制一下
            然后把机器人管理页面的右上角的账号填到"userId"的冒号后面（在下面的req>"userInfo">"userId"里）
            我这里的apikey只给实在是没能力去实名制使用的人以及灵空机器人的测试员
            '''


            a = t_hua
            log_log.logger.debug('已接入图灵')
            log_log.logger.debug(a)
            req={
                "reqType":0,
                "perception": {
                    "inputText": {
                        "text": a
                    },
                    "inputImage": {
                        "url": "imageUrl"
                    },
                    "selfInfo": {
                        "location": {
                            "city": city,
                        }
                    }
                },
                "userInfo": {
                    "apiKey": apikey,
                    "userId": "450562"#如果你改了apikey，请把这也改了
                }
            }
            req=json.dumps(req).encode('utf8')
            post=requests.post(url,data=req,headers={'content-type': 'application/json'})
            r=post.text
            r=r.encode('utf8')
            r=str(r, 'utf-8')
            r=json.loads(r)
            text=r['results'][0]['values']['text']
            log_log.logger.debug('已成功返回答复')
            log_log.logger.debug(text)
            history.appendHistory(1,text)

        #定义结束，开始执行技能----------------------------------------------------------------------------
        if "你会" in jn_hua:
            yuliao.can()
            next
            pass
        elif "笑话" in jn_hua:
            xiaohua()
            next
            pass
        elif "你爸爸" in jn_hua or "你的爸爸" in jn_hua:
            yuliao.father()
            next
            pass
        elif '待办' in jn_hua or '代办' in jn_hua:
            daiban()
            next
            pass
        else:
            tuling(jn_hua)
            next
            pass

        f = open("all.log",'r')#3
        read_log_s = f.read()   
        f.close()
        readlog_s = read_log_s
        log_log = Logger('all.log',level='debug')

    
jineng_s =jineng()

server.run(jineng_s,history,readlog_s)
