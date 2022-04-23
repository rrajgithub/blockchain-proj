
import json


f1 = open('product_data.json')
product=json.load(f1)
f2 = open('agent_data.json')
agent=json.load(f2)



n = 10
# d1 = dict(input().split() for _ in range(n))
# d2 = dict(input().split() for _ in range(n))

lis1=["timestamp", "product_id", "product_serial", "name", "MFD", "Best before in days", "Reputation", "digital signature", "flagged", "amount"]
lis2=["timestamp", "name", "agent_id", "member since", "Supervisor", "Good delivery", "Bad delivery", "Reputation", "digital signature", "flagged"]

print("\n",lis1,"\n\nEnter Product details: ")

# ip1 = list(input().split("\n"))

# ip2 = list(input().split("\n"))
#ip2 = list(input().split() for _ in range(n))
# print(ip1)

d1=dict()
d2=dict()

# k=0
for i, j in zip(lis1, range(len(lis1))):
    print("Enter " + lis1[j] + " -: ", end=" ")
    ip=input()
    if i=="product_id" or i=="product_serial" or i=="Reputation" or i=="amount" or i=="Best before in days":
        d1[i]=int(ip)
    else:
        d1[i]=ip
    # k=k+1
# k=0
# print("\n",lis2,"\n\nenter space separated input of agent : ")
print("\n",lis2,"\n\nEnter Agent details: ")
for i, j in zip(lis2, range(len(lis2))):
    print("Enter " + lis2[j] + " -: ", end=" ")
    ip=input()
    if i=="agent_id" or i=="Good delivery" or i=="Bad delivery" or i=="Reputation":
        d2[i]=int(ip)
    else:
        d2[i]=ip
    #k=k+1


product.append(d1)
agent.append(d2)



out_file1 = open("product_data.json", "w") 
json.dump(product, out_file1,indent=3) 
out_file2 = open("agent_data.json", "w") 
json.dump(agent, out_file2,indent=3) 
















