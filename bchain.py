from codecs import ignore_errors
from distutils.log import error
from email.policy import strict
from hashlib import sha256
import json
from datetime import datetime

from numpy import block


class Block:
    def __init__(self, index, previous_hash, current_transactions, timestamp, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.current_transactions = current_transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        first_hash = sha256(block_string.encode()).hexdigest()
        second_hash = sha256(block_string.encode()).hexdigest()
        return second_hash

    def __str__(self):
        return str(self.__dict__)


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.genesis_block()

    def __str__(self):
        return str(self.__dict__)

    def genesis_block(self):
        genesis_block = Block(
            "Genesis", 0x0, [3, 4, 5, 6, 7], 'datetime.now().timestamp()', 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block.hash)
        self.transactions.append(str(genesis_block.__dict__))
        return genesis_block

    def getLastBlock(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        difficulty = 1
        block.nonce = 0
        compute_hash = block.compute_hash()
        while not(compute_hash.endswith('0' * difficulty) and ('55' * difficulty) in compute_hash):
            block.nonce += 1
            compute_hash = block.compute_hash()
        return compute_hash

    def add(self, data):
        block = Block(len(self.chain), self.chain[-1], data, 'datetime.now().timestamp()', 0)
        block.hash = self.proof_of_work(block)
        self.chain.append(block.hash)
        self.transactions.append(block.__dict__)
        self.calculateReputation(data['transactions'])
        return json.loads(str(block.__dict__).replace('\'', '\"'))

    def calculateReputation(self, transactions):
        read_product = open("product_data.json", "r+")
        pp = json.load(read_product, strict=False)

        read_agent = open("agent_data.json", "r+")
        ap = json.load(read_agent, strict=False)


        for each in transactions:
            product, agent, product_reputation, agent_reputation = {}, {}, 0.00, 0.00
            product_condition = "Good"

            # select agent as per role
            if each['role'] == 'manufacturer':
                agent = ap[each['manufacturerId'] - 1]
                # print('Manufacturer -:')
            elif each['role'] == 'transporter':
                agent = ap[each['transporterId'] - 1]
                # print('Transporter -:')
            elif each['role'] == 'retailer':
                agent = ap[each['retailerId'] - 1]
                # print('Retailer -:')
            else:
                assert(False)


            product = pp[each['product_id'] - 1]
            # product = pp["1"]
            good_deliveries, bad_deliveries = agent["Good delivery"], agent["Bad delivery"]



            if each['flagged'] == 'N':
                # agent score
                # score = agent['Good delivery'] + 1
                agent["Good delivery"] += 1
                good_deliveries = agent["Good delivery"]

                data = product["MFD"].split()
                temp = [int(each) for each in data]
                # print(temp)
                manufacture_date = datetime(temp[2], temp[1], temp[0])
                cur_date = datetime.now()
                # print(manufacture_date)
                tmedelta = cur_date - manufacture_date
                days_passed = tmedelta.days
                days_for_expiry = product['Best before in days']
                product_reputation = ((days_for_expiry - days_passed)/days_for_expiry)*100
                if product_reputation < 0 :
                    product_reputation = 0
                product['Reputation'] = product_reputation

            else:
                # agent score
                # score = agent['Bad delivery'] - 1
                agent["Bad delivery"] += 1
                bad_deliveries = agent["Bad delivery"]

                product_condition = "Bad"

                # calculate product reputation
                if product['Reputation'] < 5 :
                    product['Reputation'] = 0
                else:
                    product['Reputation'] -= 5

            # calculate agent reputation based on score
            print("Product condition on delivery = ", product_condition)
            print("Agent ID = ", agent["agent_id"])
            # print("Agent good deliveries = ", good_deliveries)
            # print("Agent bad deliveries = ", bad_deliveries)
            agent_reputation = (agent['Good delivery']/(agent['Good delivery'] + agent['Bad delivery']))*100
            agent['Reputation'] = agent_reputation
            print("Agent reputation",agent_reputation)

            print('Product ID = ', product["product_id"])
            print('Product reputation',product['Reputation'])
            print('Transcation added successfully!!')
            print('Agent details -:')
            print(json.dumps(agent, indent=3))
            print('Product details -:')
            # print("all products = '\n",pp)
            print(json.dumps(product, indent=3))
            print("\n")
            # read_product.write([{"name":"shivam"}])
            # read_product.close()
        write_product = open("product_data.json", "w")
        json.dump(pp, write_product, indent=2)
        write_agent = open("agent_data.json", "w")
        json.dump(ap, write_agent, indent=2)
        print("data written successfully")


    def getTransactions(self, id):
        labels = ['manufacturer', 'transportation',
                  'retailer', 'product_profile', 'agent']
        while True:
            try:
                if id == 'all':
                    for i in range(len(self.transactions)-1):
                        print('{}:\n{}\n'.format(labels[i], json.dumps(self.transactions[i+1], indent=3)))
                        if self.transactions[i+1] :
                            self.transactions[i+1]
                    break
                elif type(id) == int:
                    print(self.transactions[id])
                    break
            except Exception as e:
                print(e)
