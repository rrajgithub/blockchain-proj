import json
from datetime import datetime
import data as db

m = db.manufacturer
t = db.transportation
r = db.retailer

di = {}
good = []
bad = []
mtot = 0
for i in m['transactions']:
    di[i['product_id']] = i['amount']
    if i['flagged'] == 'N':
        mtot += i['amount']


ttot = 0
for i in t['transactions']:
    if i['flagged'] == 'N':
        ttot += di[i['product_id']]
    #     good.append(i['product_id'])
    # else:
    #     bad.append(i['product_id'])


rtot = 0
for i in r['transactions']:
    if i['flagged'] == 'N':
        rtot += di[i['product_id']]
        good.append(i['product_id'])
    else:
        bad.append(i['product_id'])


# print("manufacturer total : Rs.", mtot)
# print("transportation total : Rs.", ttot)
# print("retailer total : Rs.", rtot)
