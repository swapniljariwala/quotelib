# quotelib
Library for fetching quotes from NSE/BSE, the Indian stock exchanges

# Using quotelib
```python
from quotelib import icici
md = icici.get_market_depth(sym)
q = icici.get_quote(sym)
print q[0]
print q[0].price
print md[0].ask_q
prnint md[0].bid_q
```
