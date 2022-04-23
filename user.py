
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

print("\n",lis1,"\n\nenter space separated input of product : ")

ip1 = list(input().split(" "))
print("\n",lis2,"\n\nenter space separated input of agent : ")
ip2 = list(input().split(" "))
#ip2 = list(input().split() for _ in range(n))
# print(ip1)

d1=dict()
d2=dict()

k=0
for i in lis1:
    if i=="product_id" or i=="product_serial" or i=="Reputation" or i=="amount" or i=="Best before in days":
        d1[i]=int(ip1[k])
    else:
        d1[i]=ip1[k]
    k=k+1
k=0
for i in lis2:
    if i=="agent_id" or i=="Good delivery" or i=="Bad delivery" or i=="Reputation":
        d2[i]=int(ip2[k])
    else:
        d2[i]=ip2[k]
    k=k+1


product.append(d1)
agent.append(d2)



out_file1 = open("product_data.json", "w") 
json.dump(product, out_file1,indent=3) 
out_file2 = open("agent_data.json", "w") 
json.dump(agent, out_file2,indent=3) 
















