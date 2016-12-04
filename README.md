# quotelib
Library for fetching quotes from NSE/BSE, the Indian stock exchanges.
Currently i've added ICICI and will keep adding more data sources
ICICI is near real time (tested upto frequency of 6 ticks per minutes)
# Using quotelib
```python
from quotelib import icici
# Get market depth
md = icici.get_market_depth('STABAN') # ICICI's stock codes are different from NSE
# Get stock quote
q = icici.get_quote('STABAN')
print q[0]
print q[0].price
print md[0].ask_q
prnint md[0].bid_q
```
