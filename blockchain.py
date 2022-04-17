import bchain
import data as db

def main(): 
    
    B = bchain.Blockchain()
    a = B.add(db.manufacturer)
    b = B.add(db.transportation)
    c = B.add(db.retailer)
    d = B.add(db.product_profile)
    d = B.add(db.agent)
    B.getTransactions('all')


if __name__ == "__main__":
    main()
