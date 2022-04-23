from datetime import datetime

manufacturer = {
    'transactions':
    [
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 1,
            'product_serial': 50001000,
            'name': 'maggi',
            'manufacturerId': 1,
            'transporterId': 2,
            'message': 'This product is in good order',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 1500,
            'role': 'manufacturer',
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 2,
            'product_serial': 50002000,
            'name': 'Biscuit',
            'manufacturerId': 1,
            'transporterId': 1,
            'message': 'This product is in good order',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 2500,
            'role': 'manufacturer',
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 3,
            'product_serial': 5000239,
            'name': 'table',
            'manufacturerId': 4,
            'transporterId': 2,
            'message': 'Product damaged',
            'digital signature': 'Not approved',
            'flagged': 'Y',
            'amount': 3500,
            'role': 'manufacturer',
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 4,
            'product_serial': 5000240,
            'name': 'Fan',
            'manufacturerId': 4,
            'transporterId': 2,
            'message': 'This product is in good order',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 4000,
            'role': 'manufacturer',
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
            'name': 'maggi',
            'transporterId': 2,
            'retailerId': 3,
            'shopping_id': 101,
            'message': 'Product in good order. Shipped',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 1500,
            'role': 'transporter',
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 2,
            'product_serial': 50002000,
            'name': 'Biscuit',
            'transporterId': 2,
            'retailerId': 3,
            'shopping_id': 102,
            'message': 'Product damaged',
            'digital signature': 'retailer review',
            'flagged': 'Y',
            'amount': 2500,
            'role': 'transporter',
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 4,
            'product_serial': 5000240,
            'name': 'Fan',
            'transporterId': 2,
            'retailerId': 5,
            'shopping_id': 103,
            'message': 'Product in good order. shipped',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 4000,
            'role': 'transporter',
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
            'name': 'maggi',
            'retailerId': 3,
            'from': 'Retailer X',
            'to': 'Retail shelf',
            'receiving_id': 400,
            'message': 'Product in good order. Received',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 1500,
            'role': 'retailer',
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 2,
            'product_serial': 50002000,
            'name': 'Biscuit',
            'retailerId': 3,
            'from': 'Retailer X',
            'to': 'Retail shelf',
            'receiving_id': 400,
            'message': 'Product damaged',
            'digital signature': 'Not approved',
            'flagged': 'Y',
            'amount': 2500,
            'role': 'retailer',
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 4,
            'product_serial': 5000240,
            'name': 'Fan',
            'retailerId': 5,
            'from': 'Retailer X',
            'to': 'Retail shelf',
            'receiving_id': 401,
            'message': 'Product in good order. Received',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 4000,
            'role': 'retailer',
        },

    ]
}
