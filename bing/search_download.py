from tools.web_crawler import WebC

url = u'https://cn.bing.com/images/async?q=%e9%a3%8e%e6%99%af&first=41&count=35&relp=35&cw=1117&ch=649&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased_Landscape&mmasync=1&dgState=x*127_y*1396_h*167_c*1_i*36_r*9&IG=0ACC09901F3F4E8A8F816454B1581006&SFX=2&iid=images.5645'

wc = WebC(url=url)

print(wc.soup)
