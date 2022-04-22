from datetime import datetime

productProfiles = [
        {
            'timestamp': datetime(2022, 1, 15, 23, 55, 59, 342380).timestamp(),
            'product_id': 1,
            'product_serial': 50001000,
            'name': 'maggi',
            'MFD': '16-04-2022',
            'Best before in days': 6*30,
            'Reputation': 100,
            'digital signature': 'approved',
            'flagged': 'N',
            'amount':1500
        },
        {
            'timestamp': datetime(2021, 11, 15, 23, 55, 59, 342380).timestamp(),
            'product_id': 2,
            'product_serial': 50002000,
            'name': 'Biscuit',
            'MFD': '11-02-2021',
            'Best before in days': 9*30,
            'Reputation': 0,
            'digital signature': 'Rejected',
            'flagged': 'Y',
            'amount':2500
        },

    ]