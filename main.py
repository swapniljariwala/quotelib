# -*- coding: utf-8 -*-
from quotelib import icici
q = icici.get_market_depth('LARTOU')
print (q[0].symbol)
print (q[0].ask_q)

