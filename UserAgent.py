class toObj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [toObj(x) if isinstance(
                    x, dict) else x for x in b])
            else:
                setattr(self, a, toObj(b) if isinstance(b, dict) else b)


'''
Android 设备
'''
Android = toObj({
    "Xiaomi": {
        "Id": "Xiaomi",
        "Name": "小米手机",
        "UserAgent": "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn;  MI2 Build/JRO03L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0"
    },
    "Meizu": {
        "Id": "Meizu",
        "Name": "魅族手机",
        "UserAgent": "JUC (Linux; U; 2.3.5; zh-cn; MEIZU MX; 640*960) UCWEB8.5.1.179/145/33232"
    },
    "Nexus7": {
        "Id": "Nexus7",
        "Name": "Nexus 7 (Tablet)",
        "UserAgent": "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19"
    },
    "AndroidGalaxyS3": {
        "Id": "AndroidGalaxyS3",
        "Name": "Samsung Galaxy S3 (Handset)",
        "UserAgent": "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    },
    "AndroidGalaxyTab": {
        "Id": "AndroidGalaxyTab",
        "Name": "Samsung Galaxy Tab (Tablet)",
        "UserAgent": "Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
    }
})
'''
国产浏览器
'''
China = toObj({
    "360se": {
        "Id": "360se",
        "Name": "360安全浏览器",
        "UserAgent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    },
    "360chrome": {
        "Id": "360chrome",
        "Name": "360极速浏览器",
        "UserAgent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360Chrome)"
    },
    "liebao": {
        "Id": "liebao",
        "Name": "猎豹浏览器",
        "UserAgent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36 LBBROWSER"
    },
    "ucpc": {
        "Id": "ucpc",
        "Name": "UC浏览器电脑版",
        "UserAgent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 UBrowser/5.1.2238.18 Safari/537.36"
    },
    "uc": {
        "Id": "uc",
        "Name": "UC浏览器手机版",
        "UserAgent": "UCWEB/2.0 (iOS; U; iPh OS 4_3_2; zh-CN; iPh4) U2/1.0.0 UCBrowser/8.6.0.199 U2/1.0.0 Mobile"
    }, "sougou": {
        "Id": "sougou",
        "Name": "搜狗浏览器",
        "UserAgent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0"
    }, "baidu": {
        "Id": "baidu",
        "Name": "百度浏览器",
        "UserAgent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 BIDUBrowser/7.5 Safari/537.36"
    }, "maxthon": {
        "Id": "maxthon",
        "Name": "遨游浏览器",
        "UserAgent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
    }, "qq": {
        "Id": "qq",
        "Name": "QQ浏览器",
        "UserAgent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36 QQBrowser/9.0.2229.400"
    }, "mqq": {
        "Id": "mqq",
        "Name": "QQ浏览器手机版",
        "UserAgent": "MQQBrowser/3.6/Adr (Linux; U; 4.0.3; zh-cn; HUAWEI U8818 Build/U8818V100R001C17B926;480*800)"
    }, "wechat": {
        "Id": "wechat",
        "Name": "微信内置浏览器",
        "UserAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1"
    }
})

'''
搜索引擎浏览器
'''
Spider = toObj({
    "Baidu": {
        "Id": "Baidu",
        "Name": "百度PC",
        "UserAgent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
    },
    "Baidum": {
        "Id": "Baidum",
        "Name": "百度移动端",
        "UserAgent": "Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
    },
    "BingBot": {
        "Id": "BingBot",
        "Name": "BingBot (Bing's spider)",
        "UserAgent": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    },
    "Googlebot": {
        "Id": "Googlebot",
        "Name": "Googlebot (Google's spider)",
        "UserAgent": "Googlebot/2.1 (+http://www.googlebot.com/bot.html)"
    },
    "Slurp": {
        "Id": "Slurp",
        "Name": "Slurp! (Yahoo's spider)",
        "UserAgent": "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"
    }
})

'''
Mac OS
'''
Safari = toObj({
    "SafariMac": {
        "Id": "SafariMac",
        "Name": "Safari on Mac",
        "UserAgent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
    },
    "SafariWin": {
        "Id": "SafariWin",
        "Name": "Safari on Windows",
        "UserAgent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
    },
    "SafariiPad": {
        "Id": "SafariiPad",
        "Name": "Safari on iPad",
        "UserAgent": "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
    },
    "SafariiPhone": {
        "Id": "SafariiPhone",
        "Name": "Safari on iPhone",
        "UserAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
    }
})

'''
Opera 欧朋
'''
Opera = toObj({
    "OperaMac": {
        "Id": "OperaMac",
        "Name": "Opera on Mac",
        "UserAgent": "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.9.168 Version/11.52"
    },
    "OperaWin": {
        "Id": "OperaWin",
        "Name": "Opera on Windows",
        "UserAgent": "Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62"
    }
})
'''
Chrome
'''
Chrome = toObj({
    "ChromeAndroidMobile": {
        "Id": "ChromeAndroidMobile",
        "Name": "Chrome on Android Mobile",
        "UserAgent": "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
    },
    "ChromeAndroidTablet": {
        "Id": "ChromeAndroidTablet",
        "Name": "Chrome on Android Tablet",
        "UserAgent": "Mozilla/5.0 (Linux; Android 4.1.2; Nexus 7 Build/JZ054K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19"
    },
    "ChromeMac": {
        "Id": "ChromeMac",
        "Name": "Chrome on Mac",
        "UserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
    },
    "ChromeUbuntu": {
        "Id": "ChromeUbuntu",
        "Name": "Chrome on Ubuntu",
        "UserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36"
    },
    "ChromeWin": {
        "Id": "ChromeWin",
        "Name": "Chrome on Windows",
        "UserAgent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
    },
    "ChromeiPhone": {
        "Id": "ChromeiPhone",
        "Name": "Chrome on iPhone",
        "UserAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/27.0.1453.10 Mobile/10B350 Safari/8536.25"
    }
})

'''
IE
'''
IE = toObj({
    "IE10": {
        "Id": "IE10",
        "Name": "Internet Explorer 10",
        "UserAgent": "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)"
    },
    "IE6": {
        "Id": "IE6",
        "Name": "Internet Explorer 6",
        "UserAgent": "Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)"
    },
    "IE7": {
        "Id": "IE7",
        "Name": "Internet Explorer 7",
        "UserAgent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"
    },
    "IE8": {
        "Id": "IE8",
        "Name": "Internet Explorer 8",
        "UserAgent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"
    },
    "IE9": {
        "Id": "IE9",
        "Name": "Internet Explorer 9",
        "UserAgent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    }
})

'''
Firefox
'''
Firefox = toObj({
    "FFAndroidHandset": {
        "Id": "FFAndroidHandset",
        "Name": "Firefox on Android Mobile",
        "UserAgent": "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0"
    },
    "FFAndroidTablet": {
        "Id": "FFAndroidTablet",
        "Name": "Firefox on Android Tablet",
        "UserAgent": "Mozilla/5.0 (Android; Tablet; rv:14.0) Gecko/14.0 Firefox/14.0"
    },
    "FFMac": {
        "Id": "FFMac",
        "Name": "Firefox on Mac",
        "UserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"
    },
    "FFUbuntu": {
        "Id": "FFUbuntu",
        "Name": "Firefox on Ubuntu",
        "UserAgent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0"
    },
    "FFWin": {
        "Id": "FFWin",
        "Name": "Firefox on Windows",
        "UserAgent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0"
    }
})
'''
Windows Phone
'''
WinPhone = toObj({
    "Win7Phone": {
        "Id": "Win7Phone",
        "Name": "Windows Phone 7",
        "UserAgent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; LG; GW910)"
    },
    "Win75Phone": {
        "Id": "Win75Phone",
        "Name": "Windows Phone 7.5",
        "UserAgent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; SGH-i917)"
    },
    "Win8Phone": {
        "Id": "Win8Phone",
        "Name": "Windows Phone 8",
        "UserAgent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920)"
    }
})
'''
iOS
'''
iOS = toObj({
    "iPad": {
        "Id": "iPad",
        "Name": "iPad",
        "UserAgent": "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
    },
    "iPhone": {
        "Id": "iPhone",
        "Name": "iPhone",
        "UserAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
    },
    "iPod": {
        "Id": "iPod",
        "Name": "iPod",
        "UserAgent": "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3"
    }
})

Other = toObj({
    "BlackBerry": {
        "Id": "BlackBerry",
        "Name": "BlackBerry - Playbook 2.1",
        "UserAgent": "Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML, like Gecko) Version/7.2.1.0 Safari/536.2+"
    },
    "MeeGo": {
        "Id": "MeeGo",
        "Name": "MeeGo - Nokia N9",
        "UserAgent": "Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13"
    }
})

Default = Chrome.ChromeWin.UserAgent