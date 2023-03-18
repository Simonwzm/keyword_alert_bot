#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import base64
# import asyncio


# 4-6位英数验证码识别
def get_captcha(img):

    url = "http://1.15.133.252:5000/muggle_ocr/captcha"
    for i in range(10):
        # img = '10.jpg'
        # print(img)
        r = requests.post(url,data=base64.b64encode(open(img,'rb').read()).decode())
        print(r.text)
        return r.text
# 印刷字ocr识别 
# url = "http://1.15.133.252:5000/muggle_ocr/ocr"
# for i in range(10):
#     img = '2.png'
#     r = requests.post(url,data=base64.b64encode(open(img,'rb').read()).decode())
#     print(r.text)

