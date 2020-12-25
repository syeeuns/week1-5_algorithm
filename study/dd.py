import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

url = 'https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc&stt_dt=2020-12-23'
data = requests.get(url, verify=False)
soup = BeautifulSoup(data.text, 'html.parser')
target = soup.select('table')

