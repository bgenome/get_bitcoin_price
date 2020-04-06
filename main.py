import time
import urllib.request
import urllib.error
import json


def get_current():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = '{}'
    try:
        response = urllib.request.urlopen(url).read().decode('utf-8')
    except urllib.error.HTTPError as error:
        print(f'error code: {error.code}')
    except urllib.error.URLError as error:
        print(f'reason: {error.reason}')

    response_parse = json.loads(response)
    current_price = None
    if 'bpi' in response_parse:
        if 'EUR' in response_parse['bpi']:
            if 'rate_float' in response_parse['bpi']['EUR']:
                current_price = response_parse['bpi']['EUR']['rate_float']
    return current_price


def get_average(price_list):
    return sum(price_list) / len(price_list)


if __name__ == "__main__":
    last_ten = []
    count = 1
    while 1:
        current = get_current()
        last_ten.append(current)
        if len(last_ten) > 10:
            last_ten.pop(0)
        if count <= 10:
            print(f'current = {current}')
            count += 1
        else:
            average = get_average(last_ten)
            print(f'average = {average}')
            count = 1
        time.sleep(2)

