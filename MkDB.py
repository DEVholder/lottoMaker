import pprint
import requests
from bs4 import BeautifulSoup
import csv

def lottery_resust(fr, to):
    lottery_list = []
    for n in range(fr, to +1):
        url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
        payload = {'drwNo': n, 'dwrNoList': n}
        req = requests.post(url, data=payload)

        lotto_list = []
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, 'html.parser')
            win_res = soup.find('div', attrs=('class','win_result'))
            lot_num = [lot.text for lot in win_res.select('div > div.num.win > p > span.ball_645')]
            lot_num.insert(0,n)
            lot_bonus = win_res.select_one('div > div.num.bonus > p > span').text
            lot_num.append(lot_bonus)
            lottery_list.append(lot_num)
            print( n, "\t/\t", to)
        else:
            print("false...")
    #pprint.pprint(lottery_list)

    #xls_name = f'lotto_{fr}_{to}.csv'
    xls_name = f'test_lotto.csv'
    with open(xls_name, 'w', newline='') as f:
        csv_obj = csv.writer(f)
        header = ['round', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Bonus']
        csv_obj.writerow(header)

        for num in lottery_list:
            csv_obj.writerow(num)
        
    f.close()
    print('complete!')

lottery_resust(1000, 1049)

