from tools.web_crawler import WebC

# url = 'http://cc.taoyin333.info/'
url = 'http://cc.taoyin333.info/forum-63-1.html'

cookie = 'UM_distinctid=17149f7768e0-07e46cd1b694b3-317e0a5e-100200-17149f7769033; imalready18y=OK; slimitenter=y; pDXj_2132_saltkey=nqddS2xQ; pDXj_2132_lastvisit=1586079289; CNZZDATA1255696574=153913332-1586083440-%7C1586082770; pDXj_2132_seccode=6237.4d99781d80a56bc7b9; pDXj_2132_auth=4831dWwENgUca0RYEvRAZyOTcTSKw5meCb%2BDvbYRprWJw%2FIKSWqabiNYITgR0WXKe%2FaKGnPdHeURg9N05%2FY4zqN%2BL%2BIX; pDXj_2132_lastcheckfeed=1008544%7C1586082921; pDXj_2132_lip=43.250.200.5%2C1586082921; pDXj_2132_nofavfid=1; pDXj_2132_atarget=1; pDXj_2132_smile=1D1; pDXj_2132_st_p=1008544%7C1586083498%7C93ac97e569cec4598ba55178a5571fa5; pDXj_2132_viewid=tid_943213; pDXj_2132_lastact=1586083532%09forum.php%09forumdisplay; pDXj_2132_st_t=1008544%7C1586083532%7Ca2ec73bcd63aaafc709afbd52aec32de; pDXj_2132_forum_lastvisit=D_50_1586083059D_63_1586083532; pDXj_2132_ulastactivity=1586083532%7C0'

wc = WebC(url, cookies=cookie)

soup = wc.soup

print(soup)

