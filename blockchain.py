import bchain
import data as db
import smart as z
import product_profiles as pp
import agent_profiles as ap

def main(): 
    
    B = bchain.Blockchain()
    a = B.add(db.manufacturer)
    b = B.add(db.transportation)
    c = B.add(db.retailer)
    # d = B.add(pp.productProfiles)
    # d = B.add(ap.agentProfiles)
    B.getTransactions('all')


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
