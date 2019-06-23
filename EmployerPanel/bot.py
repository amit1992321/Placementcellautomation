import urllib3

http = urllib3.PoolManager()


def handle(msg):
    TOKEN = '752389576:AAEDX-z6ezfS6nPFyC05Yyh3-WCuGbmA6ls'
    chatid = '-391138285'
    full_url = 'https://api.telegram.org/bot' + TOKEN + \
        'sendMessage?chat_id=' + chatid + '&text=' + msg + '/'
    RESPONSE = http.request('GET', full_url)