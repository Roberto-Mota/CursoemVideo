# Desafio 114 -> Crie um código que teste se um site está acessível pelo computador usado.

import urllib
from urllib import request
try:
    url = 'https://habitica.com/'
    request.urlopen(url)
except:
    print('O site não está acessível')
else:
    print('O site está acessível')


# Jeito do professor

