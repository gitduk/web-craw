from tools.web_crawler import WebC

url = 'https://cn.bing.com/images/search?q=3D%e9%ab%98%e6%b8%85%e7%94%b5%e8%84%91%e6%a1%8c%e9%9d%a2%e5%a3%81%e7%ba%b8&FORM=RESTAB'

wc = WebC(url)

print(wc.soup)
