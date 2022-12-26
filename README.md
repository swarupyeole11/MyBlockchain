# MyBlockchain
In this program I have created my own blockchain using Python programming.

Follwing rules were kept in mind while develpoing the code :

1) The hash was generated using the hashlib library in python
2) The hash was ensured to nbe unique by oroviding current blockdata and the previous block has as the data to genrate hash for new block
3) It was ensured that the basic essential prooperties of the blockchain nodes i.e the current node stores data fot the previous node was achieved in the code 
4) The code can be seen in the file main.py.


Sample Image : 

![image](https://user-images.githubusercontent.com/76248886/209536718-e6c65f5c-3c83-4bb0-b8b2-cf26d7f8ea7c.png)



## Detailed Explantion 

A blockchain is a distributed, decentralized, public ledger that records transactions on multiple computers so that the record cannot be altered retroactively without the alteration of all subsequent blocks and the consensus of the network.

The code first imports the hashlib library, which provides a number of cryptographic hash functions. The genHash function uses the SHA-256 hash function from hashlib to create a hash of the input data. The hash is returned as a hexadecimal string.

The Block class represents a block in the blockchain. It has three fields: data, hash, and prevHash. The data field stores the data or transactions stored in the block. The hash field stores the hash of the block, and the prevHash field stores the hash of the previous block in the chain.

The Blockchain class represents the blockchain itself. It has a single field, chain, which is a list of Block objects. The Blockchain class has an __init__ method that is called when a new Blockchain object is created. This method creates a "genesis" block, which is the first block in the chain, and initializes the chain field with this block.

The Blockchain class also has an addBlock method, which adds a new block to the end of the chain. This method calculates the hash of the new block using the genHash function and the data and previous hash of the block. It then creates a new Block object with this data and adds it to the end of the chain list.

Finally, the code creates a new Blockchain object and adds several blocks to it. It then prints the contents of each block in the chain using the __dict__ attribute, which returns the contents of the object as a dictionary.




