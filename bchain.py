from hashlib import sha256
import json
from datetime import datetime
import agent_profiles as ap
import product_profiles as pp

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
        for each in transactions:
            product, agent, score, product_reputation, agent_reputation = {}, {}, 0, 0.00, 0.00

            # select agent as per role
            if each['role'] == 'manufacturer':
                agent = ap.agentProfiles[each['manufacturerId']]
                print('manufacturer')
            elif each['role'] == 'transporter':
                agent = ap.agentProfiles[each['transporterId']]
                print('transporter')
            elif each['role'] == 'retailer':
                agent = ap.agentProfiles[each['retailerId']]
                print('retailer')
            else:
                assert(False)

            # selct product using id
            product = pp.productProfiles[each['product_id']]



            if each['flagged'] == 'N':
                # agent score
                score = agent['Good delivery'] + 1

                # calculate product reputation
                tsm = product['timestamp']
                manufacture_date = datetime.fromtimestamp(tsm)
                cur_date = datetime.now()
                tmedelta = cur_date - manufacture_date
                days_passed = tmedelta.days
                days_for_expiry = product['Best before in days']
                product_reputation = ((days_for_expiry - days_passed)/days_for_expiry)*100
                product['Reputation'] = product_reputation

            else:
                # agent score
                score = agent['Good delivery'] - 1

                # calculate product reputation
                product['Reputation'] -= 5

            # calculate agent reputation based on score
            print("agent score = ", score)
            agent_reputation = (agent['Good delivery']/(agent['Good delivery'] + agent['Bad delivery']))*100
            agent['Reputation'] = agent_reputation

            print("agent reputation",agent_reputation)
            print('product reputation',product['Reputation'])
            print('Transcation added successfully!!')
            print('Agent details -:')
            print(agent)
            print('Product details -:')
            print(product)
            print("\n")

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
