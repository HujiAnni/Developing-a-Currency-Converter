"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Jianni Hu
Date:   2020.11.13
"""

import currency

src=input('3-letter code for original currency: ')
dst=input('3-letter code for the new currency: ')
amt=float(input('Amount of the original currency: '))
value=currency.exchange(src,dst,amt)
print('You can exchange '+str(amt)+' '+src+' for '+str(round(value,3))+' '+dst+'.')