import requests


# tools
def cookies(cookie_str):
    cookies_list = cookie_str.split(';')
    cookie_dict = {}
    for i in cookies_list:
        key, val = i.split('=', 1)
        cookie_dict[key] = val
    return cookie_dict


# cookie
cookie_str = 'session-id=136-4442170-9754248; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:HK"; ubid-main=133-6984056-8330028; lc-main=en_US; session-token=FhoXUBfPlFdLJ/p6eYj4Ef8dYXYETXARO4SuNEyPEVkZQPTBymot1gp9vUs8pID3lnTeM5/NYwJwHj0oWiqlkaDXnhW7mcXl8j2NiyEtUx+aNWEg5h0K1Kf8Caj1i/Ua/+GpnRgk4cQCURXILfpkJjr8XWkZ2hpECrNbPRTNg4FUra3/n6PdJ5Jf9Tv8rgJJ'
cookie = cookies(cookie_str)

# header
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

# proxy
proxy_json_url = "http://121.37.19.221:7079/ygvps/api/api/v1/proxy_list/9a29f93356283d6701309b0ec831ad29?group=3737&ttl=60&sort=ttl&prot=4"
resp = requests.get(proxy_json_url)
proxy_list = resp.json()["list"]
# print(resp.text)
# random_proxy = proxy_list[random.randint(0, len(proxy_list) - 1)]
# proxy = {random_proxy["type"]: random_proxy["addr"]}
