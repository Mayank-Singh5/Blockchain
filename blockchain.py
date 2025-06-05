from time import time
from json import dumps
from hashlib import sha256
from datetime import datetime

class Block:

    def __init__(self,index,timestamp,data,prev_hash,nonce=1):

        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = nonce  
        self.hash = self.generate_hash()
        
    def generate_hash(self):    

        block_dict = {
            "Index" : self.index,
            "Timestamp" : str(self.timestamp),  
            "Data" : self.data,
            "Previous Hash" : self.prev_hash,
            "Nonce" : self.nonce
        }

        hash_str = dumps(block_dict,sort_keys=True).encode()
        
        t1 = time()
        while not sha256(hash_str).hexdigest().startswith("00"):
            self.nonce += 1
            block_dict["Nonce"] = self.nonce
            hash_str = dumps(block_dict,sort_keys=True).encode()
        t2 = time()
        
        print(f"Time required for mining : {t2-t1}")
        self.hash = sha256(hash_str).hexdigest()

        return self.hash
        
    def regenerate_hash(self):

        block_data = {
            "Index" : self.index,
            "Timestamp" : str(self.timestamp),
            "Data" : self.data,
            "Previous Hash" : self.prev_hash,
            "Nonce" : self.nonce
        }

        return sha256(dumps(block_data, sort_keys=True).encode()).hexdigest()
            
    def __str__(self):

        return f"""Index : {self.index}
Timestamp : {self.timestamp}
Data : {self.data}
Previous Hash : {self.prev_hash}
Hash : {self.hash}
Nonce : {self.nonce}"""
        
class Blockchain:

    def __init__(self):
    
        self.chain = [Block(0, datetime.now(), "Genesis Block", '0'*64)]
    
    def add_block(self, data):
  
        current_index = len(self.chain)
        prev_block_hash = self.chain[-1].hash
        new_block = Block(current_index, datetime.now(), data, prev_block_hash)
        self.chain.append(new_block)
        
    def is_valid(self):
  
        genesis = self.chain[0]
        if (genesis.index != 0 or 
            genesis.prev_hash != '0'*64 or 
            genesis.data != "Genesis Block" or
            genesis.hash != genesis.regenerate_hash()):
            return False
            
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.index != previous_block.index + 1:
                return False

            if current_block.hash != current_block.regenerate_hash():
                return False
                
            if current_block.prev_hash != previous_block.hash:
                return False
                
        return True