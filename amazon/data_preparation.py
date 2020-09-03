import random

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
cookie_str = 'session-id=136-4442170-9754248; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:HK"; ubid-main=133-6984056-8330028; lc-main=en_US; x-amz-captcha-1=1599049883463427; x-amz-captcha-2=3Jt1shN5WhR2F7B6JfIOUw==; session-token=VFAmUzgIrvRONaRRiWI+0ff0gc8QPbtVjMyi+xLB7ALLfbj4pOi6A8P9ApKB80PkKohHXNLwSBofFV2fZPUueHwPPZObgBMtgUVI9lHIBQOtxzFjcJclSlcC/U5VuDQyryy8atmEr5NDVLatiqjMRWAIuQG37TOL2C6gjdwitazOXGY7kuB8KZRZPcp/j/Es; csm-hit=tb:6X6TGJPW5RVKJGGJFMH7+s-6X6TGJPW5RVKJGGJFMH7|1599102942573&t:1599102942573&adb:adblk_no'
cookie = cookies(cookie_str)

# header
alphabet = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()'
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
key = random.choice(alphabet)
value = random.choice(Alphabet)

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    key: value
}

# proxy
proxy_json_url = "http://121.37.19.221:7079/ygvps/api/api/v1/proxy_list/9a29f93356283d6701309b0ec831ad29?group=5819&ttl=60&sort=ttl&prot=4"
resp = requests.get(proxy_json_url)
proxy_list = resp.json()["list"]
