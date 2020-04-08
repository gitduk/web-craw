import requests
from tools.downloader import Download_from_file

dld = Download_from_file('dld.csv', 'videos/')
dld.start(max_thread=2)
print('end')

