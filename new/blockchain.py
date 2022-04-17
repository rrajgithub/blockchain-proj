from datetime import datetime
import bchain

#using the standard JSON format to store data in each block i.e, within {}
def main():

  manufacturer = {
    'transactions':
        [
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':1,
            'product_serial':50001000,
            'name': 'cotton pants',
            'from': 'Manufacturer X',
            'to': 'Transportation X',
            ##'shipping_id': 100,
            'message': 'This product is in good order',
            'digital signiture': 'approved',
            'flagged':'N'
            },
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':2,
            'product_serial':50002000,
            'name': 'cotton shirt',
            'from': 'Manufacturer X',
            'to': 'Transportation X',
            ##'shipping_id' = 101,
            'message': 'This product is in good order',
            'digital signiture': 'approved',
            'flagged':'N'
            },
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':2,
            'product_serial':50002001,
            'name': 'cotton shirt',
            'from': 'Manufacturer X',
            'to': 'Transportation X',
            ##'shipping_id' = 102,
            'message': 'The product is in good order',
            'digital signiture': 'approved',
            'flagged':'N'
            },
        ]
  }

  transportation={
    'transactions':
        [
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':1,
            'product_serial':50001000,
            'name': 'cotton pants',
            'from': 'Transportation X',
            'to': 'Retailer X',
            'shipping_id': 100,
            'message': 'Product in good order. Shipped',
            'digital signiture': 'approved',
            'flagged':'N'
            },
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':2,
            'product_serial':50002000,
            'name': 'cotton shirt',
            'from': 'Transportation X',
            'to': 'Retailer X',
            'shipping_id': 101,
            'message': 'This product is in good order. Shipped',
            'digital signiture': 'approved',
            'flagged':'N'
            },
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':2,
            'product_serial':50002001,
            'name': 'cotton shirt',
            'from': 'Transportation X',
            'to': 'Retailer X',
            'shipping_id': 102,
            'message': 'Product damaged',
            'digital signiture': 'retailer review',
            'flagged':'Y'
            },
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':4,
            'product_serial':50002005,
            'name': 'cotton shirt',
            'from': 'Transportation X',
            'to': 'Retailer X',
            'shipping_id': 102,
            'message': 'Product damaged',
            'digital signiture': 'retailer review',
            'flagged':'Y'
            },
        ] 
  }

  retailer = {
    'transactions':
        [
           {
           'timestamp':datetime.now().timestamp(),
            'product_id':1,
            'product_serial':50001000,
            'name': 'cotton pants',
            'from': 'Retailer X',
            'to': 'Retail Shelf',
            'shipping_id': 400,
            'message': 'Product in good order. Received',
            'digital signiture': 'approved',
            'flagged':'N'
            },
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':2,
            'product_serial':50002000,
            'name': 'cotton shirt',
            'from': 'Retailer X',
            'to': 'Retail Shelf',
            'shipping_id': 400,
            'message': 'Product Good',
            'digital signiture': 'approved',
            'flagged':'N'
            },
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':2,
            'product_serial':50002001,
            'name': 'cotton shirt',
            'from': 'Retailer X',
            'to': 'RTV',
            'shipping_id': 401,
            'message': 'Box Damaged',
            'digital signiture': 'rejected',
            'flagged':'Y'
            },
        ]
  }


  B = bchain.Blockchain()
  B.add(manufacturer)
  B.add(transportation)
  B.add(retailer)
  B.getTransaction('all')

if __name__ == "__main__":
  main()