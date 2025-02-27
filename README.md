# Automation platform for Telegram -- modified from Hootrix/keyword_alert_bot

## Introduction

This is an automation platform for telegram, based on telethon, python 3.7+, and forked from [Hootrix/keyword_alert_bot](https://github.com/Hootrix/keyword_alert_bot/)

Telethon is a pure Python 3 MTProto API Telegram client library, which is used to interact with Telegram's API. It can be used to build Telegram clients, or to perform advanced operations on behalf of a user, thus imaging that you can do anything that the official Telegram clients can do, and more, such as automatic message forwarding, checkin once a day, sending a message after receiving a keyword from a channel, etc.

Thanks to the repo [Hootrix/keyword_alert_bot](https://github.com/Hootrix/keyword_alert_bot/), most of the framework has been completed, and I have made some modifications to the code to make it more suitable for my own needs. You can also understand the framework according to some of my code comments and then add your own features!

**I've add a message sending task in the keyword notification feature, so that for example you can immediately send a sign-in message to a bot right after you receive a registeration open message.**


Telethon是一个纯Python 3 MTProto API Telegram客户端库，用于与Telegram的API互动。它可以用来构建Telegram客户端，或者代表用户进行高级操作，从而让你可以做任何Telegram官方客户端可以做的事情，甚至更多，比如自动转发消息，每天签到一次，在收到一个频道的关键词后发送消息，等等。

感谢repo[Hootrix/keyword_alert_bot](https://github.com/Hootrix/keyword_alert_bot/)的工作，大部分的框架已经完成，我对代码做了一些修改，使其更适合我自己的需要。你也可以按照我的一些注释去理解框架然后自己增加功能！

**我在关键词提醒功能中添加了一个消息发送任务，这样，例如你可以在收到注册开放消息后立即向机器人发送一个开通账户的消息**

> 以下是fork仓库的文档

---

## 🤖Telegram keyword alert bot ⏰


用于提醒 频道/群组 关键字消息

如果想订阅`群组`消息，确保普通TG账户加入该群组不需要验证。

原理：tg命令行客户端来监听消息，使用bot来发送消息给订阅用户。

👉  Features：

- [x] 关键字消息订阅：根据设定的关键字和频道来发送新消息提醒
- [x] 支持正则表达式匹配语法
- [x] 支持多频道订阅 & 多关键字订阅
- [x] 支持订阅群组消息
- [x] 支持私有频道ID/邀请链接的消息订阅 

  1. https://t.me/+B8yv7lgd9FI0Y2M1  
  2. https://t.me/joinchat/B8yv7lgd9FI0Y2M1 
  

👉 Todo:

- [ ] 私有群组订阅和提醒
- [ ] 私有频道消息提醒完整内容预览
- [ ] 多账号支持
- [ ] 扫描退出无用频道/群组

# DEMO

http://t.me/keyword_alert_bot

![image](https://user-images.githubusercontent.com/10736915/171514829-4186d486-e1f4-4303-b3a9-1cfc1b571668.png)


# USAGE

## 普通关键字匹配

```
/subscribe   免费     https://t.me/tianfutong
/subscribe   优惠券   https://t.me/tianfutong

```

## 正则表达式匹配

使用js正则语法规则，用/包裹正则语句，目前可以使用的匹配模式：i,g

```
# 订阅手机型号关键字：iphone x，排除XR，XS等型号，且忽略大小写
/subscribe   /(iphone\s*x)(?:[^sr]|$)/ig  com9ji,xiaobaiup
/subscribe   /(iphone\s*x)(?:[^sr]|$)/ig  https://t.me/com9ji,https://t.me/xiaobaiup

# xx券
/subscribe  /([\S]{2}券)/g  https://t.me/tianfutong

```



## BUILD

### 1. config.yml.default --> config.yml

#### Create Telelgram Account & API

[开通api](https://my.telegram.org/apps) 建议请使用新注册的Telegram账户

#### Create BOT 

https://t.me/BotFather  

### 2. RUN

运行环境 python3.7+

首次运行需要用tg账户接收数字验证码，且输入密码（telegram API触发）

```
$ pipenv install

$ pipenv shell

$ python3 ./main.py
```

### 3. crontab （optional）

 - update telethon

依赖库telethon可能会有旧版本不可用的情况或者其他BUG，请最好是通过定时任务去执行依赖更新。

e.g. 
```
0 0 1 * * cd /home/keyword_alert_bot && pipenv update telethon > /dev/null 2>&1
```

## BUG Q&A

 - 查看日志发现个别群组无法接收消息，软件客户端正常接收
 
 请尝试更新telethon解决问题🤔，我也很无助。

 - 订阅群组消息，机器人没任何反应
 https://github.com/Hootrix/keyword_alert_bot/issues/20

 - ModuleNotFoundError: No module named 'asyncstdlib', No module named '...'

```
$ pipenv  install
```

## BOT HELP

```

目的：根据关键字订阅频道消息

支持多关键字和多频道订阅，使用英文逗号`,`间隔

关键字和频道之间使用空格间隔

主要命令：

/subscribe - 订阅操作： `关键字1,关键字2 https://t.me/tianfutong,https://t.me/xiaobaiup`

/unsubscribe - 取消订阅： `关键字1,关键字2 https://t.me/tianfutong,https://t.me/xiaobaiup`

/unsubscribe_all - 取消所有订阅

/list - 显示所有订阅列表

---

Purpose: Subscribe to channel messages based on keywords

Multi-keyword and multi-channel subscription support, using comma `,` interval.

Use space between keywords and channels

Main command:

/subscribe - Subscription operation: `keyword1,keyword2 https://t.me/tianfutong,https://t.me/xiaobaiup`

/unsubscribe - unsubscribe: `keyword1,keyword2 https://t.me/tianfutong,https://t.me/xiaobaiup`

/unsubscribe_all - cancel all subscriptions

/list - displays a list of all subscriptions
```
