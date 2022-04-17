from datetime import datetime
import bchain


def main():
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
                    'flagged': 'N'
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
                    'flagged': 'N'
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
                    'flagged': 'N'
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
                    'flagged': 'Y'
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
                    'flagged': 'N'
                },
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 2,
                    'product_serial': 50002000,
                    'name': 'cotton shirt',
                    'from': 'Retailer X',
                    'to': 'Retail shelf',
                    'receiving_id': 400,
                    'message': 'Product good',
                    'digital signature': 'approved',
                    'flagged': 'N'
                },
                {
                    'timestamp': datetime.now().timestamp(),
                    'product_id': 2,
                    'product_serial': 50002001,
                    'name': 'cotton shirt',
                    'from': 'Retailer X',
                    'to': 'RTV',
                    'receiving_id': 401,
                    'message': 'Box damaged',
                    'digital signature': 'rejected',
                    'flagged': 'Y'
                }
            ]
    }

    B = bchain.Blockchain()
    a = B.add(manufacturer)
    b = B.add(transportation)
    c = B.add(retailer)
    B.getTransactions('all')


if __name__ == "__main__":
    main()
