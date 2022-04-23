import bchain
import data as db
import smart as z
import json

def main(): 
    

    read_product = open("product_data.json", "r+")
    pp = json.load(read_product, strict=False)

    read_agent = open("agent_data.json", "r+")
    ap = json.load(read_agent, strict=False)

    print("Initial Product details -:")
    for each in pp:
        print(json.dumps(each, indent=3))

    print()
    print("Initial Agent details -:")
    for each in ap:
        print(json.dumps(each, indent=3))

    read_agent.close()
    read_product.close()
    print()

    B = bchain.Blockchain()
    print('**************************************Transactions of Manufacturer**************************************')
    B.add(db.manufacturer)
    print('**************************************Transactions of Transporter*************************************')
    B.add(db.transportation)
    print('**************************************Transactions of Retailer************************************')
    B.add(db.retailer)
    # B.getTransactions('all')


print("\n")

print("manufacturer total : Rs.", z.mtot)
print("transportation total : Rs.", z.ttot)
print("retailer total : Rs.", z.rtot)

print("\nGood products : ")

for x in z.good:
    print("id : ",x)

print("\nDamaged products : ")

for x in z.bad:
    print("id : ",x)


print("\n")
if __name__ == "__main__":
    main()
