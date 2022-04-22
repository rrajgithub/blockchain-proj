from datetime import datetime
import agent_profiles as ap
import product_profiles as pp

manufacturer = {
    'transactions':
    [
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 0,
            'product_serial': 50001000,
            'name': 'maggi',
            'manufacturerId': 0,
            'transporterId': 1,
            'message': 'This product is in good order',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 1500,
            'role': 'manufacturer',
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 1,
            'product_serial': 50002000,
            'name': 'Biscuit',
            'manufacturerId': 0,
            'transporterId': 1,
            'message': 'This product is in good order',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 2500,
            'role': 'manufacturer',
        }
    ]
}
transportation = {
    'transactions':
    [
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 0,
            'product_serial': 50001000,
            'name': 'maggi',
            'transporterId': 1,
            'retailerId': 2,
            'shopping_id': 101,
            'message': 'Product in good order. Shipped',
            'digital signature': 'approved',
            'flagged': 'N',
            'amount': 1500,
            'role': 'transporter',
        },
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 1,
            'product_serial': 50002000,
            'name': 'Biscuit',
            'transporterId': 1,
            'retailerId': 2,
            'shopping_id': 102,
            'message': 'Product damaged',
            'digital signature': 'retailer review',
            'flagged': 'Y',
            'amount': 2500,
            'role': 'transporter',
        }
    ]
}

retailer = {
    'transactions':
    [
        {
            'timestamp': datetime.now().timestamp(),
            'product_id': 0,
            'product_serial': 50001000,
            'name': 'maggi',
            'retailerId': 2,
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
            'product_id': 1,
            'product_serial': 50002000,
            'name': 'Biscuit',
            'retailerId': 2,
            'from': 'Retailer X',
            'to': 'Retail shelf',
            'receiving_id': 400,
            'message': 'Product damaged',
            'digital signature': 'Not approved',
            'flagged': 'Y',
            'amount': 2500,
            'role': 'retailer',
        },

    ]
}
