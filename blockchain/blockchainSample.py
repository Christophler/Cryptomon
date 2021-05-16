
import hashlib
from block import Block
from blockData import BlockData

# initialize blockchain
blockchain = []

# Create block data
block1Data = BlockData(1211, "Chris")
block2Data = BlockData(1334, "Henry")

# Create blocks
block1 = Block(block1Data, None)
block2 = Block(block2Data, block1.getHash())

# Add blockchain
blockchain.append(block1)
blockchain.append(block2)

# Print block data
for i in range(len(blockchain)):
    # block is block object. See block.py
    block = blockchain[i]
    print("============== Block " + str((i+1)) + " ==============")
    print("Hash: " + str(block.getHash()))
    print("Data: " + str(block.getBlockData().getTuple()))
