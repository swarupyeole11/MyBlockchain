import hashlib
def genHash(data):
   result = hashLib.sha256(data.encode())
   return result.hexdigest()


class Block: #The fields of each new block being created 
   def __init__(self,data,hash,prevHash):
     self.data=data;
     self.hash=hash;
     self.prevHash=prevHash;



class Blockchain:
   def __init__(self):
    hashLast = genHash('gen_last')
    hashStart = genHash('gen_hash')

    genesis=Block('Intial_Block',hashStart,hashLast)
    self.chain = [genesis]  #defined a list in which the blocks will get stored 


def addBlock(self,data):
   prevHash = chain[-1].hash #hash of last block of blockchain
   hash = genHash(data+prevHash)
   block = Block(data,hash,prevHash)