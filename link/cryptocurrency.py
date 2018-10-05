from django.contrib.auth.models import User, Group
from .models import Cryptocurrency

import krakenex

def getBalance(handle):
    k = krakenex.API()
    k.load_key('kraken.key')

    print(k.query_private('Balance'))
