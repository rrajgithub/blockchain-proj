from datetime import datetime

manufacturer = {
    'transactions':
    [
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 1,
            'product_serial': 50001000,
            'name': 'cotton pants',
            'from': 'Manufacturer X',
            'to': 'Transportation X',
            'message': 'This product is in good order',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount':1500
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 2,
            'product_serial': 50002000,
            'name': 'cotton shirt',
            'from': 'Manufacturer X',
            'to': 'Transportation X',
            'message': 'This product is in good order',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount':2500
        }
    ]
}
transportation = {
    'transactions':
    [
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 1,
            'product_serial': 50001000,
            'name': 'cotton shirt',
            'from': 'Transportation X',
            'to': 'Retailer X',
            'shopping_id': 101,
            'message': 'Product in good order. Shipped',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount':1500
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 2,
            'product_serial': 50002000,
            'name': 'cotton shirt',
            'from': 'Transportation X',
            'to': 'Retailer X',
            'shopping_id': 102,
            'message': 'Product damaged',
            'digital signature': 'retailer review',
            'flagged': 'Y',
            'amount':2500
        }
    ]
}

retailer = {
    'transactions':
    [
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 1,
            'product_serial': 50001000,
            'name': 'cotton shirt',
            'from': 'Retailer X',
            'to': 'Retail shelf',
            'receiving_id': 400,
            'message': 'Product in good order. Received',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount':1500
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 2,
            'product_serial': 50002000,
            'name': 'cotton shirt',
            'from': 'Retailer X',
            'to': 'Retail shelf',
            'receiving_id': 400,
            'message': 'Product damaged',
            'digital signature': 'Not approved',
            'flagged': 'Y',
            'amount':2500
        },
        # {
        #     'timestamp': datetime.now().timestamp(),
        #     'product_id': 2,
        #     'product_serial': 50002001,
        #     'name': 'cotton shirt',
        #     'from': 'Retailer X',
        #     'to': 'RTV',
        #     'receiving_id': 401,
        #     'message': 'Box damaged',
        #     'digital signature': 'rejected',
        #     'flagged': 'Y',
        #     'amount':0
        # }
    ]
}

product_profile = {
    'transactions':
    [
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 1,
            'product_serial': 50001000,
            'name': 'cotton shirt',
            'MFD': '16-04-2022',
            'message': 'Best before 6 months',
            'Reputation': '100',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount':1500
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 1,
            'product_serial': 50002000,
            'name': 'cotton pant',
            'MFD': '11-02-2021',
            'message': 'Best before 9 months',
            'Reputation': '0',
            'digital signature': 'Rejected',
            'flagged': 'Y',
            'amount':2500
        },

    ]
}
agent = {
    'transactions':
    [
        {
            'timestamp': datetime.now().timestamp(),
            'name': 'Ramesh Kumar',
            'agent_id': 1,
            'member since': '16-04-2022',
            'Supervisor': 'Kishan Raj',
            'Good delivery': 180,
            'Bad delivery': 70,
            'Reputation': ((180)/(180+70))*100,
            'digital signature': 'approved',
            'flagged': 'N'
        },
        {
            'timestamp': datetime.now().timestamp(),
            'name': 'Suresh Kumar',
            'agent_id': 2,
            'member since': '16-04-2022',
            'Supervisor': 'Paresh Raj',
            'Good delivery': 40,
            'Bad delivery': 50,
            'Reputation': ((40)/(40+50))*100,
            'digital signature': 'Not approved',
            'flagged': 'Y'
        },

    ]
}
