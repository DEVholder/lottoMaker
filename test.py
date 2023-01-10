import requests
from bs4 import BeautifulSoup


url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
req = requests.post(url)

soup = BeautifulSoup(req.text, 'html.parser')
getTo = soup.find('div', attrs=('select','dwrNoList')) 